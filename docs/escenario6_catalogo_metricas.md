# Escenario 6 — Diseño de Métricas

## Objetivo

Documentar formalmente, siguiendo la anatomía de métrica de ISO/IEC 25022, las cinco métricas de
Calidad en Uso de MediSalud HIS. Las fichas de este catálogo no se diseñan en abstracto: describen
exactamente las funciones ya implementadas en `scripts/metricas_iso25022.py` (Escenario 8), de
modo que exista una correspondencia uno a uno entre lo documentado aquí y lo que el pipeline
calcula en producción.

## Insumos utilizados

- Tareas priorizadas 1 y 2 del Escenario 5 (registro de HCE, agendamiento, facturación con
  seguro).
- Umbrales normativos del caso de estudio: RNF-01 (≤ 8 s), RNF-02 (agendamiento sin errores),
  RNF-03 (≤ 1 % de errores de facturación).
- Implementación real: `scripts/metricas_iso25022.py`.

---

## Ficha 1 — Completitud de registro de HCE

| Campo | Contenido |
|---|---|
| Nombre | Completitud de registro de HCE |
| Característica | Efectividad |
| Propósito | Verificar que las notas de evolución clínica registradas por los médicos se completan y guardan correctamente, sin pérdida de datos ni fallos del sistema. |
| Fórmula | X = completadas / total |
| Variables | `completadas`: número de eventos de `logs_hce.csv` con `completada = 1`. `total`: número total de eventos registrados en el periodo (`evento_id`). |
| Unidad | Proporción (0–1) |
| Rango deseado | ≥ 0,95 |
| Fuente de datos | `data/logs_hce.csv`, columna `completada`, generado por `scripts/generar_logs_hce.py` |
| Frecuencia de medición | Semanal, vía `.github/workflows/medicion_calidad.yml` (cada lunes 06:00 UTC) |
| Responsable | Gerencia de Calidad y Aseguramiento; ejecución técnica automatizada (Escenario 8) |

---

## Ficha 2 — Tiempo promedio de registro de HCE

| Campo | Contenido |
|---|---|
| Nombre | Tiempo promedio de registro de HCE |
| Característica | Eficiencia |
| Propósito | Determinar si el tiempo que un médico tarda en registrar una nota de evolución clínica cumple RNF-01. |
| Fórmula | X = (Σ tiempo_segundos) / n |
| Variables | `tiempo_segundos`: duración en segundos de cada evento (`logs_hce.csv`). `n`: número total de eventos. |
| Unidad | Segundos |
| Rango deseado | ≤ 8,00 s |
| Fuente de datos | `data/logs_hce.csv`, columna `tiempo_segundos` |
| Frecuencia de medición | Semanal, mismo pipeline que la Ficha 1 |
| Responsable | Gerencia de Calidad y Aseguramiento, con corresponsabilidad de Gerencia de Tecnología por el desempeño técnico subyacente |

---

## Ficha 3 — Índice de satisfacción CSAT normalizado

| Campo | Contenido |
|---|---|
| Nombre | Índice de satisfacción CSAT normalizado |
| Característica | Satisfacción |
| Propósito | Medir la percepción de utilidad, confianza y comodidad de los usuarios de MediSalud HIS mediante encuesta CSAT. |
| Fórmula | X = (Σ puntaje_csat / n) / 5 |
| Variables | `puntaje_csat`: calificación 1–5 de cada encuestado (`encuesta_satisfaccion.csv`). `n`: número de encuestados. |
| Unidad | Proporción (0–1), normalizada desde escala Likert 1–5 |
| Rango deseado | ≥ 0,80 |
| Fuente de datos | `data/encuesta_satisfaccion.csv`, generado por `scripts/generar_encuesta_satisfaccion.py` |
| Frecuencia de medición | La recolección de encuestas es periódica y no continua (ver Escenario 7, Pregunta de Discusión 2); el pipeline recalcula el índice semanalmente sobre las respuestas acumuladas disponibles |
| Responsable | Gerencia de Calidad y Aseguramiento, con apoyo del Call Center para la distribución de la encuesta |

---

## Ficha 4 — Tasa de errores de facturación

| Campo | Contenido |
|---|---|
| Nombre | Tasa de errores de facturación |
| Característica | Libertad de Riesgo |
| Propósito | Detectar la proporción de transacciones de facturación asociadas a incidentes de riesgo económico (cobro duplicado, discrepancias) sobre el total de transacciones procesadas. |
| Fórmula | X = incidentes_facturacion / total_transacciones |
| Variables | `incidentes_facturacion`: registros del CSV de incidentes con `modulo = "Facturacion"`. `total_transacciones`: transacciones de facturación procesadas en el periodo. |
| Unidad | Proporción (0–1) |
| Rango deseado | ≤ 0,01 (RNF-03) |
| Fuente de datos | CSV de incidentes en `data/` (ver Escenario 7 sobre el archivo fuente autorizado) + `total_transacciones` |
| Frecuencia de medición | Semanal |
| Responsable | Departamento de Admisión y Facturación, con seguimiento de Gerencia de Calidad |

**Nota obligatoria sobre esta ficha:** el valor de `total_transacciones` está fijado en el código
como la constante `TOTAL_TRANSACCIONES_FACTURACION = 8500`, sin que exista un archivo o fuente de
datos real que lo respalde. Es un supuesto de simulación para fines del taller y debe
reemplazarse por el conteo real de transacciones del periodo antes de usar esta métrica en
producción; de lo contrario, la tasa calculada no representa el riesgo real del sistema.

---

## Ficha 5 — Cobertura de contexto por sede

| Campo | Contenido |
|---|---|
| Nombre | Cobertura de contexto por sede |
| Característica | Cobertura de Contexto |
| Propósito | Verificar que el cumplimiento del umbral de eficiencia (RNF-01) se sostiene de manera uniforme en las cinco sedes de la red, y no solo en el promedio nacional. |
| Fórmula | X = sedes_que_cumplen_eficiencia / total_sedes, donde una sede cumple si su tiempo promedio de `tiempo_segundos` ≤ 8,00 s |
| Variables | `sedes_que_cumplen_eficiencia`: sedes cuyo promedio de `tiempo_segundos` agrupado por `sede` es ≤ 8,00 s. `total_sedes`: 5 (Quito, Guayaquil, Cuenca, Ambato, Manta). |
| Unidad | Proporción de sedes (0–1) |
| Rango deseado | = 1,00 |
| Fuente de datos | `data/logs_hce.csv`, agrupado por columna `sede` |
| Frecuencia de medición | Semanal |
| Responsable | Gerencia de Tecnología (desempeño por sede), con seguimiento de Gerencia de Calidad |

---

## Preguntas de Discusión

### 1. ¿Por qué es importante fijar de antemano el rango deseado y no solo calcular el valor de la métrica?

Sin un umbral definido antes de medir, el valor calculado es solo un número sin criterio de
juicio: un CSAT de 0,6253 o una tasa de errores de facturación de 0,0500 no dicen por sí mismos si
la situación es aceptable o crítica. Fijar el rango deseado antes de la medición —como se hizo aquí
con RNF-01, RNF-03 y el umbral interno de CSAT (0,80)— convierte el valor en una decisión binaria
(cumple / no cumple) y evita el sesgo de ajustar el umbral después de ver el resultado para que
parezca favorable. Es precisamente lo que permite que `dashboards/indicadores.json` distinga, sin
ambigüedad, que Efectividad y Eficiencia cumplen mientras que Satisfacción y Libertad de Riesgo no.

### 2. ¿Qué diferencia existe entre una métrica de Eficiencia y un simple cronómetro de tiempo de respuesta del servidor?

Un cronómetro de tiempo de respuesta mide latencia técnica de una petición HTTP o de una consulta
a base de datos, sin considerar si el usuario efectivamente completó una tarea con sentido de
negocio. La métrica de Eficiencia de ISO/IEC 25022 mide el tiempo total que un médico invierte en
completar la tarea "registrar una nota de evolución clínica" —incluyendo validaciones de
formulario, reintentos y tiempo de lectura de la interfaz—, y solo adquiere significado cuando se
compara contra un umbral de negocio (RNF-01). Un servidor puede responder en 200 ms y, aun así, el
médico tardar 15 segundos en completar la tarea por fricciones de interfaz; ese segundo número, no
el primero, es el que importa para la Calidad en Uso.

---

## Conclusión Parcial

El catálogo documenta formalmente las cinco métricas que el pipeline del Escenario 8 ya calcula,
cerrando la brecha entre diseño normativo y código ejecutable. Queda señalado un punto de
seguimiento obligatorio (el total de transacciones de facturación simulado) que debe resolverse
con datos reales antes de considerar el programa de medición apto para producción.
