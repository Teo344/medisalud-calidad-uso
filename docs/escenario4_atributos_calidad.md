# Escenario 4 — Identificación de Atributos de Calidad en Uso

## Objetivo

Definir tareas representativas de usuario, con su contexto de uso y sus atributos de Calidad en
Uso asociados, para tres procesos críticos de MediSalud HIS, siguiendo el modelo
**Usuario–Tarea–Contexto** exigido por ISO/IEC 25022 antes de diseñar cualquier métrica.

## Criterio de selección de los procesos

De los 6 procesos críticos identificados en el Escenario 1, se seleccionaron los siguientes tres,
en función de dos criterios: (1) impacto directo sobre los objetivos del negocio y los RNF
definidos en el caso de estudio, y (2) volumen de incidentes reales ya clasificados en el
Escenario 2 (`data/incidentes_2025_clasificados_iso25022.csv`).

| Proceso seleccionado | Justificación de la selección |
|---|---|
| Atención médica y registro de HCE | Módulo con más incidentes de Efectividad (458) de todo el sistema; sujeto a RNF-01. |
| Agendamiento de citas por el paciente | Segundo módulo con más incidentes de Efectividad (314) y con incidentes propios de Satisfacción (110) y Cobertura de Contexto (37); sujeto a RNF-02. |
| Facturación de una consulta con seguro médico | Módulo con más incidentes de Libertad de Riesgo (261) de todo el sistema; sujeto a RNF-03 y al Objetivo de Negocio #2. |

Se descartaron, para este escenario, Farmacia, Telemedicina y Reportes Gerenciales: los dos
primeros ya están cubiertos parcialmente por RNF-05 y se retomarán en escenarios posteriores: el
Reto Final Integrador está explícitamente dedicado a Telemedicina 2.0; Reportes Gerenciales no
tiene RNF asociado ni volumen de incidentes significativo.

---

## Ficha 1 — Atención médica y registro de HCE

| Campo | Contenido |
|---|---|
| **Proceso** | Atención médica y registro de historia clínica |
| **Usuario primario** | Médico tratante |
| **Tarea representativa** | Registrar una nota de evolución clínica completa de un paciente |
| **Contexto de uso** | Consulta externa, horario 10:00–12:00 (hora pico), sede de alto volumen (Quito o Guayaquil), red interna del hospital, carga alta de usuarios concurrentes |
| **Atributos de Calidad en Uso relevantes** | Completitud de la nota (Efectividad); tiempo de tarea (Eficiencia); percepción de fluidez durante la consulta (Satisfacción); exposición accidental de datos de otro paciente (Libertad de Riesgo) |

**Cómo se derivó la tarea:** partiendo de la distribución de incidentes por módulo del Escenario 2,
HCE concentra 458 casos de Efectividad, 153 de Libertad de Riesgo, 111 de Eficiencia y 47 de
Cobertura de Contexto — es, en volumen, el módulo más problemático de todo el sistema. De esos
cuatro grupos se descarta acotar la tarea a "Cobertura de Contexto" (HCE no depende tanto del
dispositivo como Portal Citas) y se prioriza la combinación Efectividad–Eficiencia porque ambas
comparten la misma unidad de trabajo observable: el guardado de una nota de evolución. Esta es la
razón por la que la tarea se define como "registrar una nota de evolución clínica" y no como
"usar el módulo de HCE": solo la primera formulación permite distinguir, evento por evento, un
intento de un éxito, algo indispensable para calcular X = A/B en el Escenario 6.

**Cómo se derivó el contexto:** RNF-01 exige cumplimiento en el 90 % de los casos, lo que obliga a
observar la tarea bajo la condición donde es más probable que falle, no bajo la condición
promedio. La Problemática Actual del caso de estudio ubica esa condición en la franja 10:00–12:00
y en las sedes de mayor volumen (Quito y Guayaquil, que además concentran más médicos activos según
la Tabla 2 de perfiles). Fijar el contexto en la hora valle o en una sede pequeña habría producido
una ficha técnicamente válida pero inútil para el objetivo real del programa de medición: detectar
el escenario donde el RNF-01 está en mayor riesgo de incumplirse (ver Pregunta de Discusión 2).

**Atributo adicional no evidente en una primera lectura:** el incidente 3846 (datos de otro
paciente visibles brevemente) ocurre dentro de este mismo flujo de registro de HCE, no en un
proceso aparte. Por eso se incorpora Libertad de Riesgo como cuarto atributo de la ficha, aunque
el enunciado original de la tarea solo mencione tiempo y completitud: la tarea observada en
producción expone un riesgo que no aparece si solo se mide velocidad y completitud de la nota.

---

## Ficha 2 — Agendamiento de citas por el paciente

| Campo | Contenido |
|---|---|
| **Proceso** | Agendamiento y admisión de pacientes |
| **Usuario primario** | Paciente (portal web / app móvil) |
| **Tarea representativa** | Agendar una cita médica disponible en máximo 3 pasos, sin errores de disponibilidad |
| **Contexto de uso** | App móvil o portal web, fuera de horario laboral, conexión de datos móviles variable, cualquier sede de la red |
| **Atributos de Calidad en Uso relevantes** | Tasa de éxito de agendamiento (Efectividad); percepción de facilidad del formulario (Satisfacción); funcionamiento correcto en dispositivos móviles (Cobertura de Contexto) |

**Justificación de la tarea:** la formulación coincide de forma literal con RNF-02 ("máximo 3
pasos, sin errores de disponibilidad"), lo que permite construir después una métrica de
Efectividad directamente comparable contra ese requerimiento. El incidente 1002 (Escenario 2)
confirma que el fallo real observado ocurre exactamente en este punto: el usuario no logra
agendar tras varios intentos.

**Justificación del contexto:** se incluye explícitamente "app móvil" y "conexión de datos
móviles variable" porque el incidente 2196 (botón de confirmar cita no responde en dispositivos
móviles) y el incidente 2017 (formulario confuso, abandono de registro) son de Cobertura de
Contexto y Satisfacción respectivamente, y ambos dependen del dispositivo/canal usado, no del
horario. Esto valida por qué la Cobertura de Contexto es un atributo relevante para esta tarea y
no para la Ficha 1.

---

## Ficha 3 — Facturación de una consulta con seguro médico

| Campo | Contenido |
|---|---|
| **Proceso** | Facturación y gestión de seguros/reaseguros |
| **Usuario primario** | Personal de admisión |
| **Tarea representativa** | Facturar una consulta con seguro médico sin generar cobro duplicado |
| **Contexto de uso** | Módulo de facturación, horario de alta afluencia (mañana), integración con el sistema de la aseguradora externa, cualquier sede |
| **Atributos de Calidad en Uso relevantes** | Tasa de errores de facturación (Libertad de Riesgo); completitud de la transacción en un solo intento (Efectividad) |

**Justificación de la tarea:** se prioriza la Libertad de Riesgo por encima de la Efectividad
porque el riesgo dominante en este proceso no es que el usuario no logre facturar, sino que
facture *incorrectamente* (doble cobro, factura duplicada), tal como documentan los incidentes de
Facturación (261 casos de Libertad de Riesgo, el valor más alto de todo el sistema según el
Escenario 2). Esto es consistente con el criterio ya aplicado en el análisis del incidente 1005:
un error del sistema no siempre se clasifica como Efectividad si su consecuencia principal es un
riesgo económico o de integridad del dato.

**Justificación del contexto:** se fija "integración con el sistema de la aseguradora externa"
porque la dependencia de un sistema externo es la condición operativa que distingue esta tarea de
una facturación particular simple, y es la que introduce el riesgo de duplicidad al reintentar un
pago (RNF-03, Objetivo de Negocio #2).

---

## Preguntas de Discusión

### 1. ¿Por qué es incorrecto definir una tarea como «usar el sistema HIS» en lugar de «registrar una nota de evolución clínica»?

Porque «usar el sistema HIS» no tiene un criterio de inicio, fin ni éxito observable: agrupa
tareas heterogéneas (registrar HCE, facturar, agendar, dispensar medicamentos) que tienen
usuarios, tiempos y riesgos distintos. La fórmula general de ISO/IEC 25022 (X = A/B) exige poder
contar con precisión qué cuenta como "intento" y qué cuenta como "éxito"; sin una tarea acotada no
es posible definir A ni B de forma consistente, y cualquier métrica calculada sobre "usar el
sistema" mezclaría fenómenos distintos en un solo número sin significado accionable.

### 2. ¿Qué ocurre si se mide la eficiencia sin haber definido el contexto de uso (por ejemplo, sin diferenciar hora pico de hora valle)?

El promedio resultante queda contaminado: los tiempos normales de hora valle diluyen la
degradación real que ocurre en hora pico, produciendo un valor promedio que puede aparentar
cumplimiento del RNF-01 (≤ 8 segundos) aun cuando, en el peor momento del día —precisamente el más
crítico clínicamente—, el sistema esté incumpliendo el umbral de forma sistemática. El resultado
es una falsa sensación de conformidad: la Gerencia de Calidad concluiría que "el sistema funciona
bien en promedio" mientras los médicos siguen reportando lentitud real durante la franja de mayor
carga asistencial.

## Conclusión Parcial

Las tres fichas Usuario–Tarea–Contexto quedan acotadas a tareas medibles, con usuario y contexto
explícitos, y justificadas tanto por los RNF del caso de estudio como por evidencia real de
incidentes ya clasificada en el Escenario 2. Estas fichas son el insumo directo del Escenario 5,
donde se construirá la matriz de priorización tarea–característica–prioridad a partir de estas
mismas tres tareas.
