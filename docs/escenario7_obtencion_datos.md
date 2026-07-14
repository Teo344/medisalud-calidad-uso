# Escenario 7 — Obtención de Datos

## Objetivo

Identificar las fuentes de datos que alimentan las cinco métricas del Escenario 6 y validar su
calidad antes de que el pipeline de automatización del Escenario 8 las consuma.

## Fuentes de datos por característica

| Característica | Fuente real en el repositorio | Generador |
|---|---|---|
| Efectividad | `data/logs_hce.csv`, columna `completada` | `scripts/generar_logs_hce.py` |
| Eficiencia | `data/logs_hce.csv`, columna `tiempo_segundos` | `scripts/generar_logs_hce.py` |
| Satisfacción | `data/encuesta_satisfaccion.csv`, columna `puntaje_csat` | `scripts/generar_encuesta_satisfaccion.py` |
| Libertad de Riesgo | CSV de incidentes en `data/`, columna `modulo` | `scripts/clasificar_incidentes_iso25022.py` (Escenario 2) |
| Cobertura de Contexto | `data/logs_hce.csv`, agrupado por `sede` | `scripts/generar_logs_hce.py` |

### Archivo fuente autorizado para incidentes

`scripts/metricas_iso25022.py` busca, en orden, `incidentes_2025.csv`,
`incidentes_2025_iso_25022.csv` e `incidentes_2025_clasificados_iso25022.csv`, y usa el primero
que encuentra. En el estado actual del repositorio, esto resuelve a
`incidentes_2025_iso_25022.csv` (el archivo crudo del Escenario 2, sin las columnas
`caracteristica_iso25022` y `justificacion`). El resultado numérico es idéntico al que se
obtendría con el archivo clasificado, porque la clasificación no altera el conteo de incidentes
por módulo, solo agrega columnas descriptivas. Se declara `incidentes_2025_iso_25022.csv` como
archivo fuente autorizado para la métrica de Libertad de Riesgo, y
`incidentes_2025_clasificados_iso25022.csv` como el archivo de referencia para análisis cualitativo
(Escenario 2).

## Validación de datos

Se ejecutó `scripts/validar_datos.py` sobre los dos datasets generados para el programa de
medición. Resultados obtenidos:

### `data/logs_hce.csv` (3.150 eventos)

| Verificación | Resultado |
|---|---|
| Valores nulos | 0 en las 6 columnas |
| Eventos con `tiempo_segundos` fuera de rango (< 0 s o > 120 s) | 0 |
| Eventos duplicados (`evento_id`) | 0 |
| Rango de `tiempo_segundos` | mínimo 1,50 s — máximo 17,31 s |
| Media / mediana de `tiempo_segundos` | 7,43 s / 7,00 s |
| Distribución por sede | Quito 900, Guayaquil 900, Cuenca 450, Ambato 450, Manta 450 |
| Proporción de notas completadas | 0,9651 |

### `data/encuesta_satisfaccion.csv` (150 respuestas)

| Verificación | Resultado |
|---|---|
| Valores nulos | 0 en las 5 columnas |
| Respuestas con `puntaje_csat` fuera de rango (< 1 o > 5) | 0 |
| Respuestas duplicadas (`respuesta_id`) | 0 |
| Media / mediana de `puntaje_csat` | 3,13 / 3,00 |
| Distribución por sede | Quito 49, Guayaquil 44, Cuenca 27, Manta 18, Ambato 12 |
| Distribución por rol | Paciente 51, Médico 33, Enfermería 31, Admisión 17, Farmacia 9, Gerencia 9 |

### Interpretación de la validación

Ambos datasets están libres de nulos, duplicados y valores fuera de rango lógico, por lo que
quedan aptos para el cálculo automatizado del Escenario 8. El máximo observado de
`tiempo_segundos` (17,31 s) es más del doble del umbral RNF-01 (8 s) pero se mantiene dentro del
rango de sanidad definido (≤ 120 s): no se trata de un dato corrupto, sino de un evento real de
hora pico que la propia generación de datos simula de forma intencional, y que la métrica de
Eficiencia debe seguir capturando en el promedio, no descartar (ver Pregunta de Discusión 1).

## Preguntas de Discusión

### 1. ¿Qué consecuencias tendría calcular la métrica de tiempo de tarea sin antes eliminar los valores atípicos (outliers) causados por sesiones abandonadas?

Una sesión abandonada —el médico abre el formulario y lo deja inactivo antes de guardar, o un
error deja el evento a medio registrar— no representa el mismo fenómeno que una demora real de
registro completo. Si ese tipo de evento entra al promedio de `tiempo_segundos` sin distinguirse
de un registro válido, puede inflar artificialmente el tiempo promedio y hacer parecer que el
sistema incumple RNF-01 cuando en realidad el problema es de comportamiento de usuario, no de
desempeño del sistema; o, en sentido inverso, un evento truncado con tiempo artificialmente bajo
puede diluir una degradación real. En ambos casos la Gerencia de Calidad actuaría sobre una causa
equivocada. Por eso la validación debe distinguir explícitamente entre "evento con tiempo alto por
hora pico" (dato válido que sí debe promediarse, como se confirmó arriba) y "evento incompleto o
abandonado" (dato que debe excluirse o tratarse aparte antes de calcular Eficiencia).

### 2. ¿Por qué la fuente de datos de Satisfacción (encuestas) es cualitativamente distinta a la de Eficiencia (logs)? ¿Qué implica esto para su frecuencia de recolección?

Los logs de `tiempo_segundos` se generan automáticamente cada vez que un médico registra una
nota: son datos de comportamiento, continuos, exhaustivos y sin costo adicional de recolección.
El CSAT, en cambio, requiere que un usuario se detenga voluntariamente a responder una pregunta
subjetiva; es un dato de percepción, disperso en el tiempo, con tasa de respuesta limitada
(en este dataset, 150 respuestas frente a 3.150 eventos de HCE en el mismo periodo) y con costo de
recolección (diseño de encuesta, canal de distribución, fatiga del encuestado). Esta diferencia
implica que Eficiencia puede recalcularse con la misma frecuencia que se genera el log —incluso
diaria—, mientras que Satisfacción debe recolectarse con una cadencia más espaciada y con un
tamaño de muestra mínimo antes de considerar el promedio representativo; recalcular el CSAT
semanalmente sobre una muestra que apenas creció respecto a la semana anterior produciría un
indicador ruidoso y poco accionable.

## Entregables generados

- `scripts/validar_datos.py`: script reproducible de validación.
- Resultados de validación documentados en este archivo (sin nulos, sin duplicados, sin valores
  fuera de rango en ninguno de los dos datasets).

## Conclusión Parcial

Los dos datasets que alimentan el pipeline del Escenario 8 quedan validados y documentados antes
de su consumo automatizado, cerrando la brecha que existía entre "datos generados" y "datos
verificados". El hallazgo relevante no es la ausencia de errores de calidad del dato, sino la
necesidad de tratar explícitamente los valores de hora pico como datos válidos y no como ruido,
así como declarar formalmente el archivo fuente autorizado para incidentes de Facturación.
