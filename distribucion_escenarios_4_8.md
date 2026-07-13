# Verificación de Escenarios 2-3 y Distribución de Escenarios 4-8

**Grupo 4** — Mateo Criollo, Eduardo Garcia, Mateo Iza, Josue Guallichico
**Base normativa:** ISO/IEC 25022 (Parte 2 — versión Ing. Diego Gamboa)

---

## 1. Verificación de lo ya realizado (Escenarios 2 y 3)

El nuevo documento (`taller_iso_25022_parte2`) introduce cambios menores en las fichas de
laboratorio de los Escenarios 2 y 3 frente a la versión anterior. Se verificó el trabajo ya
entregado contra estos cambios:

| Escenario | Cambio en el nuevo documento | Estado del entregable actual |
|---|---|---|
| 2 — Comprensión de ISO/IEC 25022 | Tiempo estimado baja de 3h a ±1h; el dataset de entrada se renombra a `incidentes_2025_iso_25022.csv` | ✅ Cumple. `docs/escenario2_iso25022.md` clasifica 3.000 incidentes, incluye distribución por módulo, ejemplos, análisis del incidente 1005 y preguntas de discusión respondidas. |
| 3 — Comprensión del Modelo SQuaRE | Herramientas ahora exigen diagrama digital (Draw.io/Miro, sin "papel y lápiz"); la investigación pasa de "máximo media página" a **mínimo 2 páginas** | ✅ Cumple y excede. `docs/Investigacion_Escenario3.pdf` es un informe de 6 páginas con marco teórico completo, 2 diagramas digitales (Figuras 1 y 2) y las 2 preguntas de discusión desarrolladas en profundidad. |

**Único punto de atención:** `scripts/clasificar_incidentes_iso25022.py` toma por defecto el
archivo de entrada desde `Path.home() / "Downloads" / "incidentes_2025_iso_25022.csv"`, es decir,
una ruta personal fuera del repositorio. Esto significa que si otro integrante del grupo clona el
repo, el script no funcionará hasta que copie ese CSV manualmente a su propia carpeta de
Descargas. Se recomienda mover ese archivo de entrada a `data/incidentes_2025_iso_25022.csv`
dentro del repo y actualizar `DEFAULT_INPUT` para que apunte ahí, garantizando reproducibilidad
para todo el equipo.

---

## 2. Contenido nuevo que trae este documento: Escenarios 4 a 8

La primera versión del taller solo detallaba hasta el Escenario 3. Este segundo documento agrega
el desarrollo completo de los Escenarios 4, 5, 6, 7 y 8, con fichas de laboratorio, plantillas y
scripts de Python ya especificados. Esta es la carga de trabajo a distribuir.

| # | Escenario | Duración | Entregable principal | Carpeta destino |
|---|---|---|---|---|
| 4 | Identificación de Atributos de Calidad en Uso | 3h | 3 fichas Usuario–Tarea–Contexto (HCE, agendamiento, facturación) | `docs/` |
| 5 | Mapeo de Características de Calidad | 2h | Matriz de priorización tarea–característica–prioridad (≥6 tareas) | `docs/` |
| 6 | Diseño de Métricas | 3h | Catálogo de 5 fichas de métrica (una por característica ISO 25022) | `docs/` |
| 7 | Obtención de Datos | 3h | Generador de logs (`generar_logs_hce.py`), encuesta CSAT, notebook de validación | `scripts/`, `data/` |
| 8 | Automatización de la Medición | 4h | Pipeline `metricas_iso25022.py` + exportación JSON + workflow GitHub Actions | `scripts/`, `dashboards/`, `.github/workflows/` |

**Total: 15 horas académicas.** Nótese que hay una dependencia secuencial fuerte: el Escenario 5
usa las fichas del 4; el 6 usa las tareas priorizadas del 5; el 7 obtiene los datos que el 6 exige
medir; y el 8 integra y automatiza todo lo anterior. Por eso la distribución no es "cada quien
su escenario en paralelo sin más", sino con puntos de entrega intermedios.

---

## 3. Distribución propuesta por integrante

| Integrante | Escenario a cargo | Rol en esa entrega | Fecha sugerida de entrega* |
|---|---|---|---|
| **Persona 1** | Escenario 4 (3h) | Redacta las 3 fichas Usuario–Tarea–Contexto en `docs/escenario4_atributos_calidad.md`, tomando como base los procesos críticos ya usados en el Escenario 1 | Día 1 |
| **Persona 2** | Escenario 5 (2h) | Construye la matriz de priorización en `docs/escenario5_mapeo_priorizacion.md`, usando como insumo directo las fichas de Mateo Criollo | Día 2 (tras Escenario 4) |
| **Persona 3** | Escenario 6 (3h) | Documenta las 5 fichas de métrica en `docs/escenario6_catalogo_metricas.md`, usando las tareas de prioridad 1 y 2 de la matriz de Mateo Iza | Día 3 (tras Escenario 5) |
| **Persona 4** | Escenario 7 (3h) | Implementa `scripts/generar_logs_hce.py`, genera `data/logs_hce.csv` y `data/encuesta_satisfaccion.csv`, y valida con `scripts/01_validacion_datos.ipynb` | Día 4 (tras Escenario 6, para saber qué variables generar) |
| **Todo el equipo** | Escenario 8 (4h) | Sesión conjunta: se integra el trabajo de los 4 escenarios anteriores en `scripts/metricas_iso25022.py` + `scripts/exportar_reporte.py` + `.github/workflows/medicion_calidad.yml`. Se sugiere que Josue Guallichico coordine por su experiencia previa con el script de Python del Escenario 2 | Día 5 (cierre) |

*Fechas relativas — ajustar según el cronograma real del curso.

### Por qué el Escenario 8 es grupal y no individual

A diferencia de los Escenarios 4-7, el pipeline de automatización **consume las salidas de los
cuatro escenarios anteriores** (tareas, métricas, datos, umbrales). Asignarlo a una sola persona
generaría un cuello de botella y el riesgo de que esa persona no entienda las decisiones tomadas
por los demás. Se recomienda una sesión conjunta de 4 horas donde cada integrante explica y
aporta la parte que le corresponde del pipeline.

---

## 4. Checklist de entregables por carpeta

- `docs/`: `escenario4_atributos_calidad.md`, `escenario5_mapeo_priorizacion.md`, `escenario6_catalogo_metricas.md`
- `scripts/`: `generar_logs_hce.py`, `01_validacion_datos.ipynb`, `metricas_iso25022.py`, `exportar_reporte.py`
- `data/`: `logs_hce.csv`, `encuesta_satisfaccion.csv`, `incidentes_2025_iso_25022.csv` (mover aquí, ver punto 1)
- `dashboards/`: `indicadores.json`
- `.github/workflows/`: `medicion_calidad.yml`
