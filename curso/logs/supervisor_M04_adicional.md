# S-M04-04 — control booleano de relevancia

El supervisor leyó el script de prácticas, línea 19: `descarta_magnitud=ci95[0]>-margin or ci95[1]<margin` devuelve True en B porque excluye −0,30 pero incluye +0,30. Si la etiqueta significa descartar magnitudes ≥0,30 en ambos sentidos, debe usar `and`, y dar False. La solución del libreto dice correctamente que no descarta magnitud relevante. Luna debe armonizar la etiqueta/booleano, añadir aserción False en este caso y registrar decisión, sin tocar referencias.
