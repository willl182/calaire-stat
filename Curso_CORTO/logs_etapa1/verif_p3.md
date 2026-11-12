# Verificación — punto 3, etapa 1

**Veredicto: CON OBSERVACIONES**

El punto 3 está resuelto en lo esencial, pero la escena nueva en M02 usa «MAD» antes de definirla y contradice la tabla de niveles del propio capítulo. Conviene corregirlo antes de cerrar el punto.

## Cumplimiento de la tarea

El plan pide subir a M02 el tratamiento de Grubbs y Dixon «o al menos un puente hacia él». Se hizo lo segundo, y es aceptable:

- `M02_libreto.md:92–100` — Escena B6 nueva. Introduce una regla descriptiva (IQR con cercas 1,5·IQR) y una distancia a la mediana, presenta los valores atípicos como candidatos a investigar, prohíbe borrarlos sin causa documentada y remite a M4 para Grubbs y Dixon.
- `M04_libreto.md:180` — Solo cambia la primera frase de I5, que ahora enlaza con M2. El resto de I5 (ejemplo, G = 2,4374, Q = 0,8214, tabla 2.10/2.11) queda igual que en el origen.

No hay cambios en `calc/` respecto del origen, así que no hacía falta reejecutar scripts. Los números de M04 I5 no se tocaron.

## Hallazgos

1. **MAD usado antes de definirse, y fuera del nivel que lo introduce** — `M02_libreto.md:96`. B6 dice «La mediana y la MAD ayudan…» en el nivel B. La MAD se define recién en la escena I1 (`M02_libreto.md:146`), y la tabla de niveles la coloca en el nivel I (`M02_libreto.md:10`: «Nivel I añade… mediana y MAD»). Corregir: o bien describir la MAD en B6 con su definición, o bien quitar la mención y dejar solo la cerca IQR, que es lo que el nivel B necesita.
2. **Cita a Otto sin entrada bibliográfica en M02** — `M02_libreto.md:98` cita «[Crowder 2020 §4.3; Otto §2.2]». La bibliografía de M02 (`M02_libreto.md:230–233`) solo tiene Crowder. Añadir la entrada de Otto o retirar esa cita.
3. **Tabla de niveles no recoge la regla IQR** — `M02_libreto.md:9` lista «detección gráfica de valores inusuales sin eliminación automática» para el nivel B, pero B6 introduce además una regla numérica de cercas 1,5·IQR. Ampliar esa celda o quedar en que es una convención de lectura de la caja (ya explicada en `M02_libreto.md:48`).
4. **Referencia de líneas obsoleta en el log** — `logs_etapa1/cambios_p3.md` dice «M02_libreto.md:80–92». La escena ahora está en `92–100`, porque los cambios del punto 1 añadieron líneas antes. No afecta al contenido, pero el log debe actualizarse.
5. **Atribución de Crowder reutilizada sin el matiz** — `M02_libreto.md:98`. B5 advierte que el soporte de Crowder §4.3 es «limitado a análisis exploratorio, no a esta atribución específica». B6 cita la misma sección sin esa advertencia. Es un matiz menor, pero es la misma sección y la misma cautela.

## Coherencia con el texto vecino

- B5 (`M02_libreto.md:84–90`) y B6 se encadenan bien: la inspección visual señala y no decide, y la conservación del dato aparece en ambas.
- La pregunta al grupo de B6 (`M02_libreto.md:100`) es coherente con el ejemplo de M4 I5.
- En M4 I5 la frase nueva («En M2 vimos…») enlaza con B6 sin contradicción. M03 (`M03_libreto.md:28`) posterga la declaración de atípicos a una etapa posterior, lo cual sigue siendo cierto.

## Lo que no se rompió

- Las otras modificaciones de M02 (prerrequisitos, punto de partida, líneas 8 y 16–19) son del punto 1 y quedan fuera de este veredicto.
- No aparecen referencias rotas a «escena B6» ni a I5 en M03, M05 o M06.

## Acciones sugeridas

Para pasar a APROBADO hacen falta solo los puntos 1 y 2: corregir la MAD en B6 y añadir o quitar la cita a Otto. Los puntos 3 a 5 son menores.
