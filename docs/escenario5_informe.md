# Escenario 5 — Mapeo de Características de Calidad

**Asignatura:** Aseguramiento de la Calidad del Software
**Norma de referencia:** ISO/IEC 25022 (Measurement of Quality in Use)
**Caso de estudio:** Red Hospitalaria MediSalud Ecuador — Sistema MediSalud HIS
**Grupo:** Grupo 4 — Consultores externos de Calidad de Software
**Entregable asociado:** `escenario5_matriz_mapeo.xlsx`

---

## 1. Objetivo del escenario

Construir la matriz de mapeo que vincula cada tarea *Usuario–Tarea–Contexto* definida en el
Escenario 4 con las cinco características de ISO/IEC 25022, y **priorizar** cuáles se medirán en
el programa de MediSalud. La matriz es el insumo directo del Escenario 6 (diseño de métricas),
donde solo se desarrollan en profundidad las tareas de prioridad 1 y 2.

---

## 2. Dependencias e insumos utilizados

Antes de resolver el Escenario 5 se verificó su dependencia. El escenario **no es
autocontenido**: su Ficha de Laboratorio exige explícitamente las *fichas Usuario–Tarea–Contexto
del Escenario 4*. Los insumos empleados fueron:

| Insumo | Origen | Para qué se usó |
|---|---|---|
| 3 fichas Usuario–Tarea–Contexto | Escenario 4 (`escenario4_atributos_calidad.md`) | Núcleo de las tareas de la matriz y sus características ISO/IEC 25022 |
| Procesos críticos y objetivos de negocio | Escenario 1 (`escenario1_analisis_inicial.md`) | Justificar Impacto y Frecuencia; completar hasta 6 tareas |
| Incidentes reales | `incidentes_2025_iso_25022.csv` (3.000 registros) | Fundamentar Impacto/Frecuencia con evidencia, no con percepción |
| Requerimientos no funcionales (RNF-01…05) | Caso de estudio | Anclar el Impacto de cada tarea a un requerimiento medible |

---

## 3. Qué se hizo y por qué

### 3.1. Selección de las 6 tareas

El Escenario 5 exige **un mínimo de 6 tareas**, pero el Escenario 4 definió solo 3 fichas. Para
resolver esto sin inventar tareas arbitrarias:

- Las **tareas 1–3** son exactamente las tres fichas del Escenario 4 (registro de HCE,
  agendamiento de citas y facturación con seguro). Son el núcleo priorizado.
- Las **tareas 4–6** completan los **6 procesos críticos identificados en el Escenario 1**
  (telemedicina, dispensación en farmacia y reportes gerenciales). Así, cada fila de la matriz
  corresponde a uno de los seis procesos críticos del negocio, sin duplicados ni relleno.

De este modo el entregable respeta el insumo real (Escenario 4) y a la vez cumple el requisito
formal del Escenario 5.

### 3.2. Impacto y Frecuencia fundamentados en datos

El mensaje de fondo del caso MediSalud es pasar *de la percepción a la evidencia*. Por eso, en
lugar de asignar Impacto y Frecuencia "a ojo", ambas columnas se justifican con tres fuentes
objetivas: (1) el volumen real de incidentes por módulo del CSV, (2) los RNF asociados, y (3) los
objetivos de negocio. El ranking de incidentes reales fue:

| Módulo | Incidentes | Módulo | Incidentes |
|---|---|---|---|
| HCE | 769 | Farmacia | 258 |
| Portal Citas | 545 | Laboratorio | 166 |
| Facturación | 425 | Imagenología | 151 |
| Telemedicina | 320 | Reportes Gerenciales | 88 |
| App Móvil | 278 | | |

### 3.3. Regla de priorización

Se aplicó la matriz de doble entrada Impacto × Frecuencia del Escenario 5.1.2, extendida para
cubrir los tres niveles de prioridad:

- **Prioridad 1 — Crítica:** Impacto Alto **y** Frecuencia Alta. Se mide desde el inicio.
- **Prioridad 2 — Importante:** Impacto Alto con Frecuencia Media; o Impacto Medio con
  Frecuencia Media/Alta. Se mide en el programa base.
- **Prioridad 3 — Diferible:** Impacto Bajo, o Frecuencia Baja. Se mide en fases posteriores.

### 3.4. Automatización de la prioridad

La columna **Prioridad** no se escribió a mano: se calcula con una fórmula a partir de las celdas
de Impacto y Frecuencia. La columna **Clasificación** deriva de la prioridad. Esto evita
inconsistencias humanas y hace la matriz reutilizable: si el equipo ajusta un Impacto o una
Frecuencia, la prioridad se recalcula sola.

---

## 4. Contenido del archivo Excel

El archivo `escenario5_matriz_mapeo.xlsx` tiene tres hojas:

1. **Matriz de Mapeo** — el entregable principal: las 6 tareas con Proceso, Usuario primario,
   Impacto, Frecuencia, Característica(s) ISO/IEC 25022, Prioridad y Clasificación, más la
   leyenda de la regla de priorización.
2. **Justificación** — por qué cada tarea recibe su nivel de Impacto y de Frecuencia, con
   referencia a RNF, objetivos e incidentes reales.
3. **Datos de Respaldo** — los conteos de incidentes por módulo extraídos del CSV, que sustentan
   la priorización con evidencia.

### Resultado de la matriz

| # | Tarea | Impacto | Frecuencia | Prioridad | Clasificación |
|---|---|---|---|---|---|
| 1 | Registrar nota de evolución clínica (HCE) | Alto | Alta | 1 | Crítica |
| 2 | Agendar cita en portal/app | Alto | Alta | 1 | Crítica |
| 3 | Facturar consulta con seguro | Alto | Media | 2 | Importante |
| 4 | Completar teleconsulta | Medio | Media | 2 | Importante |
| 5 | Dispensar medicamento (Farmacia) | Medio | Media | 2 | Importante |
| 6 | Generar/consultar reporte gerencial | Bajo | Baja | 3 | Diferible |

---

## 5. Cómo usar el archivo

1. **Leer la matriz** en la hoja *Matriz de Mapeo*. Las tareas de prioridad 1 y 2 (filas 1–5) son
   las que pasan al Escenario 6 para diseñar métricas.
2. **Ajustar valores, si se requiere:** las celdas de las columnas *Impacto* y *Frecuencia* tienen
   una **lista desplegable** (Alto/Medio/Bajo y Alta/Media/Baja). Al cambiar una de ellas, la
   *Prioridad* y la *Clasificación* se recalculan automáticamente, y el color de la celda de
   prioridad cambia (verde = 1, ámbar = 2, gris = 3).
3. **Consultar el sustento:** cada decisión de Impacto/Frecuencia está explicada en la hoja
   *Justificación*, y los datos que la respaldan están en *Datos de Respaldo*.
4. **Si se edita en LibreOffice/Excel:** al abrir el archivo las fórmulas ya vienen calculadas;
   cualquier cambio en Impacto o Frecuencia recalcula en el momento.

> **Decisión que conviene revisar:** la tarea 3 (Facturación con seguro) quedó con Frecuencia
> **Media**, porque no toda consulta usa seguro. Si en la operación real este proceso es de alto
> volumen, basta cambiar la celda a **Alta** en el desplegable y la tarea pasará a Prioridad 1.

---

## 6. Preguntas de Discusión

### 6.1. ¿Qué riesgo corre una organización que intenta medir absolutamente todo desde el primer día de un programa de calidad en uso?

Intentar medirlo todo de golpe es, paradójicamente, la forma más rápida de no medir nada útil. Los
riesgos concretos son:

- **Dispersión de recursos.** Instrumentar logs, encuestas y auditorías para las cinco
  características en todas las tareas consume tiempo de TI y presupuesto que MediSalud no tiene
  asignado; el esfuerzo se reparte tan fino que ninguna métrica queda bien construida.
- **Ruido y baja calidad del dato.** Muchos indicadores calculados sobre datos aún no depurados
  (recuérdese el Escenario 7: "calidad del dato antes que calidad del indicador") generan cifras
  poco confiables que contradicen entre sí y erosionan la credibilidad del programa ante la
  Dirección.
- **Parálisis por análisis.** Con decenas de indicadores compitiendo por atención, la Gerencia de
  Calidad no sabe dónde actuar primero; el programa produce tableros, pero no decisiones.
- **Pérdida de foco en el negocio.** Medir tareas de bajo impacto al mismo nivel que el registro
  de HCE diluye la señal de los problemas realmente críticos (riesgo clínico, financiero,
  reputacional).

Por eso la práctica profesional —y esta matriz— recomienda un despliegue **incremental**:
empezar por las tareas de alto impacto y alta frecuencia (prioridad 1), demostrar valor con pocos
indicadores sólidos y extender la medición por fases. Es el mismo principio que rige la
observabilidad de software en la industria: primero se instrumenta lo que más duele.

### 6.2. ¿Por qué «Consultar historial de resultados» tiene menor prioridad pese a tener alta frecuencia?

Porque **la prioridad no depende de la frecuencia por sí sola, sino de la combinación Impacto ×
Frecuencia**, y esa tarea tiene un impacto de negocio bajo:

- Es una tarea de **lectura**, no de transacción: si falla, el usuario simplemente reintenta o
  refresca. No hay riesgo clínico inmediato (como una demora en el registro de HCE), ni riesgo
  financiero (como una factura duplicada), ni riesgo de integridad de datos.
- **No tiene un RNF asociado** ni está ligada a un objetivo de negocio prioritario, a diferencia
  del registro de HCE (RNF-01), el agendamiento (RNF-02) o la facturación (RNF-03).
- La alta frecuencia **amplifica** un problema solo cuando ese problema tiene consecuencias
  serias. Una molestia menor repetida muchas veces sigue siendo una molestia menor: incomoda,
  pero no compromete la seguridad del paciente ni las finanzas de la red.

Por eso la matriz de doble entrada pondera el eje de impacto: una tarea de **frecuencia alta pero
impacto bajo** cae en **Prioridad 3 (diferible)**. En el entregable, este mismo principio explica
que "Generar/consultar reporte gerencial" (tarea 6), pese a ser una consulta habitual de la
gerencia, quede en prioridad 3: alto volumen relativo de uso, pero bajo impacto y sin RNF que
obligue a medirla desde el inicio.

---

## 7. Conclusión parcial

La matriz traduce las fichas del Escenario 4 en un plan de medición **priorizado y sustentado en
evidencia**, no en percepción. Queda claro que un programa de Calidad en Uso sostenible se
construye de forma incremental, empezando por las tareas de mayor impacto y frecuencia. Las cinco
tareas de prioridad 1 y 2 son el insumo directo del Escenario 6, donde se les diseñarán métricas
formales ISO/IEC 25022 (fórmula, variables, unidad, umbral e interpretación).
