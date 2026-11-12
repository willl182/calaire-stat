"""Reconstruye los archivos de S1 previos a la revisión interrumpida de sol y verifica que,
aplicando las 27 ediciones del registro de sesión, se obtienen exactamente los archivos actuales.
Uso: python3 reconstruir.py  (escribe *.verif en una carpeta temporal y compara con *.pre_sol.*)"""
import json,os,re,sys,tempfile
HERE=os.path.dirname(os.path.abspath(__file__))
src=os.path.expanduser('~/.claude/projects/-home-w421-w421-calaire-stat/c024f627-1c29-4798-aae3-38e80c4752a1.jsonl')
reads={}; orig={}; edits={}; order=[]
for line in open(src):
    d=json.loads(line); m=d.get('message',{}); ts=d.get('timestamp','')
    if not isinstance(m,dict) or not isinstance(m.get('content'),list): continue
    for b in m['content']:
        if b.get('type')=='tool_use' and b['name']=='Edit' and b['id'] not in edits:
            edits[b['id']]=(ts,b['input']); order.append(b['id'])
        if b.get('type')=='tool_use' and b['name']=='Read': reads[b['id']]=b['input']['file_path']
        if b.get('type')=='tool_result' and b.get('tool_use_id') in reads:
            f=reads[b['tool_use_id']]
            if f in orig or any(e['file_path']==f for _,e in edits.values()): continue
            c=b.get('content')
            if isinstance(c,list): c=''.join(x.get('text','') for x in c if isinstance(x,dict))
            orig[f]=c
E=[edits[i] for i in order]
files=sorted({e['file_path'] for _,e in E})
out={}
for f in files:
    lines=[]
    for l in orig[f].split('<system-reminder>')[0].split('\n'):
        mm=re.match(r'^\s*(\d+)\t(.*)$',l,re.S)
        if mm and int(mm.group(1))==len(lines)+1: lines.append(mm.group(2))
    cur=open(f).read(); ok=False
    for t in ('\n'.join(lines)+'\n','\n'.join(lines)):
        x=t
        try:
            for ts,e in E:
                if e['file_path']!=f: continue
                assert e['old_string'] in x
                x=x.replace(e['old_string'],e['new_string']) if e.get('replace_all') else x.replace(e['old_string'],e['new_string'],1)
        except AssertionError: continue
        if x==cur: ok=True; out[f]=t; break
    print(f.split('/')[-1], 'original reconstruido y verificado' if ok else 'NO coincide', sum(e['file_path']==f for _,e in E),'ediciones')
for f,t in out.items():
    b=os.path.basename(f); pre=os.path.join(HERE,b.replace('.md','.pre_sol.md').replace('.py','.pre_sol.py'))
    print('  ',b,'= copia guardada' if os.path.exists(pre) and open(pre).read()==t else '!= copia guardada')
