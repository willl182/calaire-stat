"""Registro editorial de correcciones M08; ejecución única sobre el corte revisado."""
from pathlib import Path


def main():
    path = Path(__file__).resolve().parents[1] / 'M08_libreto.md'
    text = path.read_text()
    start = text.index('En el ejemplo **simulado** de presupuestos separados')
    end = text.index('> **[ERROR CRÍTICO]** No sumar', start)
    text = text[:start] + r'''Retomemos el ejemplo **simulado** de M06-B: seis días con ocho lecturas por día, $s_{\mathrm{entre}}=0{,}30$ y $s_r=0{,}24\ \mathrm{nmol/mol}$. Para un punto, la contribución de precisión es $u^2_{\mathrm{prec}}(\bar e)=0{,}30^2/6+0{,}24^2/48=0{,}0162\ (\mathrm{nmol/mol})^2$: sumamos la varianza entre días dividida por seis y la varianza de lectura dividida por cuarenta y ocho. Su raíz es $0{,}1273\ \mathrm{nmol/mol}$. Ahora completamos el presupuesto prometido en M06: añadimos una referencia común de $0{,}30$ y una corrección de $0{,}10\ \mathrm{nmol/mol}$, independientes de la precisión y entre sí, con sensibilidades unitarias. No reducimos esas dos componentes al promediar [GUM H.5 y 5.1.2; AX.4].

> **[PIZARRA]** $u_c(\bar e)=\sqrt{0{,}30^2+0{,}10^2+0{,}30^2/6+0{,}24^2/48}=0{,}3409\ \mathrm{nmol/mol}$.

Leemos: raíz de la varianza de referencia más la de corrección más las dos contribuciones de precisión del promedio. Este presupuesto completo del modelo aditivo no describe CALAIRE ni se suma al presupuesto inverso de B. Para una lectura de un día elegido al azar, sin los divisores del promedio, obtenemos $u_c=\sqrt{0{,}30^2+0{,}10^2+0{,}30^2+0{,}24^2}=0{,}4976\ \mathrm{nmol/mol}$. Para el uso futuro de la corrección media estimada, supongamos una nueva indicación media con incertidumbre total $0{,}25$ y una estabilidad entre calibración y uso de $0{,}18\ \mathrm{nmol/mol}$, independientes de todo lo anterior y entre sí. La incertidumbre de esa nueva indicación ya contiene su precisión propia: no añadimos otra componente diaria. Resulta $u_c=\sqrt{0{,}3409^2+0{,}25^2+0{,}18^2}\approx0{,}4595\ \mathrm{nmol/mol}$. Las tres cifras responden a resultados diferentes [GUM 4.1–4.2 y 5.1.2; GUM-6 11.4].

Si se justificara $k=2$, las incertidumbres expandidas del promedio y del uso futuro serían $0{,}6818$ y $0{,}9189\ \mathrm{nmol/mol}$; sin información sobre grados de libertad y distribución de estas componentes, no afirmamos cobertura exacta del 95 %. Omitir el efecto entre días daría solo $s_r/\sqrt{48}=0{,}0346\ \mathrm{nmol/mol}$ de precisión. Dividir $s_r$ por $\sqrt{576}$ daría $0{,}0100$, también incorrecto: mezcla los doce puntos y además ignora la estructura diaria. La acción es conservar los divisores del modelo y completar cada punto por separado, no buscar el menor número [GUM H.5; M06-B; AX.4].

Hay también que evitar contar la misma variación dos veces. Usemos ahora la recta simulada de M07-I, no el modelo aditivo anterior. Para una **lectura futura individual**, distinta de la indicación media con $u(y)=0{,}20$ de aquel ejemplo, fijamos $u(y)=s_{\mathrm{res}}=0{,}3946\ \mathrm{nmol/mol}$: el residual estima aquí toda la dispersión de esa lectura. Con los mismos parámetros, su covarianza y $y=250{,}50$, la inversión da $\hat x=249{,}900$ y $u(\hat x)=0{,}4256\ \mathrm{nmol/mol}$. Añadir otra vez $s_r=s_{\mathrm{res}}$ como precisión independiente produce $0{,}5800\ \mathrm{nmol/mol}$. La segunda cifra cuenta dos veces la dispersión futura; la incertidumbre de los parámetros permanece en ambas porque representa la estimación de la recta, no otra realización de la lectura futura. Revisen qué representa cada término antes de sumar [GUM 4.3.10; ISO 28037 §11.1.3; M07-I1].

''' + text[end:]
    anchor = 'Un número pequeño de grados de libertad es una señal'
    addition = r'''La aproximación de Student también requiere que la distribución de salida sea aproximadamente normal y que la incertidumbre estimada admita ese tratamiento. Muchos grados de libertad no corrigen una forma de distribución inadecuada. Si domina una componente rectangular de límites conocidos, un intervalo construido con t puede incluso salir de los límites posibles; no garantiza entonces la cobertura pretendida. Revisamos la distribución o escalamos al tratamiento numérico de M13 [GUM G.6.5].

> **[PREGUNTA AL GRUPO]** Si domina una componente rectangular de límites exactos, ¿bastan grados de libertad grandes para usar t? — *Respuesta esperada:* no; también debe ser adecuada la forma de la distribución de salida.

'''
    assert anchor in text
    text = text.replace(anchor, addition + anchor)
    anchor = '> **[EJEMPLO]** Cadena didáctica **simulada**:'
    addition = r'''Veamos además cómo una función transfiere la incertidumbre, sin esconder las sensibilidades en cifras ya equivalentes. Usamos como función del Level 2 los parámetros **simulados** de M07-I: $a=0{,}242857\ \mathrm{nmol/mol}$, $b=1{,}001429$, $u(a)=0{,}2856\ \mathrm{nmol/mol}$, $u(b)=0{,}0009433$ y $\operatorname{cov}(a,b)=-0{,}000222449\ \mathrm{nmol/mol}$. Este OLS no incluye incertidumbre de referencia; añadimos por separado una componente común del SRP de $0{,}28\ \mathrm{nmol/mol}$, representada como desplazamiento equivalente de la indicación del Level 2. Es independiente del ruido con que se estimaron los parámetros. Para $y=250{,}50$, la salida transferida es $z=(y-a)/b=249{,}900\ \mathrm{nmol/mol}$. Una comparación ideal de sensibilidad unitaria transfiere $z$ al cliente como $\hat x_{\mathrm{cliente}}=z+\delta_{\mathrm{cliente}}$, con corrección nominal cero. La incertidumbre propia del cliente se suministra en unidades de indicación del Level 2 como $0{,}42$; en la salida es $u(\delta_{\mathrm{cliente}})=0{,}42/b$. Este es otro modelo docente, no una ampliación de las cifras anteriores [GUM-6 8.4; ISO 28037 §11.1.3].

La sensibilidad al desplazamiento del SRP es $1/b=0{,}9986$, por lo que su contribución transferida es $0{,}28/b=0{,}2796\ \mathrm{nmol/mol}$. Conservamos el bloque de parámetros: $v_p=u^2(a)+z^2u^2(b)+2z\operatorname{cov}(a,b)=0{,}02595\ (\mathrm{nmol/mol})^2$. Leemos: varianza del intercepto más z al cuadrado por varianza de pendiente más dos z por covarianza. La incertidumbre de la salida del Level 2 es $\sqrt{0{,}28^2+v_p}/b=0{,}3226$ y la del cliente es $\sqrt{0{,}28^2+v_p+0{,}42^2}/b=0{,}5291\ \mathrm{nmol/mol}$. Así la salida del primer eslabón entra en el segundo con su incertidumbre; no se vuelve a sumar el SRP después de transferirla. Las cifras completas se reproducen en el script [GUM 5.1–5.2; AX.2; M07-I].

'''
    assert anchor in text
    text = text.replace(anchor, addition + anchor)
    text = text.replace('El máximo puntual es una construcción del ejemplo, no una regla de decisión de la GUM ni la aprobación de una CMC;', 'El máximo puntual combina el presupuesto de la calibración con el piso de declaración de una CMC aplicable; no es una regla de decisión de la GUM ni aprueba una CMC;')
    anchor = 'No confundamos una comparación puntual'
    addition = r'''Interpretemos el cruce. Para un servicio acreditado al que se aplica una CMC publicada, la incertidumbre informada al cliente no puede ser menor que esa CMC: por debajo de $81{,}35\ \mathrm{nmol/mol}$, el máximo obliga a declarar la CMC, aunque el presupuesto puntual dé menos. Por encima, $U(x)>\mathrm{CMC}(x)$: este presupuesto no respalda la CMC propuesta como incertidumbre alcanzable en esas condiciones. Hay que revisar la función propuesta o justificar una mejora real del presupuesto; no bajar $U$ por conveniencia. Mientras tanto, ese resultado requiere la incertidumbre mayor que sí sostiene el modelo. Como aquí la CMC solo es hipotética, el máximo es una ilustración y no autoriza declaración acreditada alguna [ILAC-P14, sin numeral, no disponible en docs/; CIPM MRA-G-13, sin numeral, no disponible en docs/].

> **[PREGUNTA AL GRUPO]** En $250\ \mathrm{nmol/mol}$, ¿podemos informar $1{,}80$ porque es la CMC propuesta? — *Respuesta esperada:* no; el presupuesto exige $U\approx3{,}052\ \mathrm{nmol/mol}$ y obliga a revisar el respaldo de la función propuesta.

'''
    assert anchor in text
    text = text.replace(anchor, addition + anchor)
    text = text.replace('se cita sin numeral y solo para la definición de CMC;', 'se cita sin numeral para la definición y el respaldo de CMC;')
    text += '\n- **ILAC-P14.** ILAC, *ILAC Policy for Measurement Uncertainty in Calibration*, ILAC-P14:09/2020 (no disponible en docs/; política de declaración de incertidumbre frente a CMC, sin numeral).\n'
    path.write_text(text)


if __name__ == '__main__':
    main()
