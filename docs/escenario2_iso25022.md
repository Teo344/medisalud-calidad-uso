# Escenario 2 - Comprension de ISO/IEC 25022

## Objetivo

Clasificar los incidentes reportados de MediSalud HIS segun las cinco caracteristicas de Calidad en Uso definidas en ISO/IEC 25022:

- Efectividad
- Eficiencia
- Satisfaccion
- Libertad de Riesgo
- Cobertura de Contexto

La clasificacion se realizo sobre el dataset `incidentes_2025_iso_25022.csv`, que contiene 3.000 incidentes con los campos `id`, `fecha`, `modulo`, `descripcion`, `rol_usuario` y `sede`.

## Criterios de clasificacion

| Caracteristica ISO/IEC 25022 | Criterio aplicado en MediSalud HIS |
| --- | --- |
| Efectividad | El usuario no logra completar su objetivo o el resultado queda incompleto/incorrecto. |
| Eficiencia | La tarea puede completarse, pero con mayor tiempo, esfuerzo o consumo de recursos. |
| Satisfaccion | El incidente afecta la comodidad, confianza o percepcion del usuario. |
| Libertad de Riesgo | El incidente puede producir impacto clinico, economico, de privacidad o seguridad. |
| Cobertura de Contexto | El problema aparece bajo un contexto especifico: dispositivo, canal, sede, app movil o condicion operativa. |

## Resultados generales

| Caracteristica ISO/IEC 25022 | Incidentes | Porcentaje |
| --- | ---: | ---: |
| Efectividad | 1.609 | 53,6% |
| Libertad de Riesgo | 604 | 20,1% |
| Eficiencia | 360 | 12,0% |
| Cobertura de Contexto | 243 | 8,1% |
| Satisfaccion | 184 | 6,1% |
| **Total** | **3.000** | **100,0%** |

La mayor parte de incidentes corresponde a **Efectividad**, porque muchos reportes describen tareas que no se completan correctamente: datos que no cargan, citas que no se reflejan, documentos que no se adjuntan o procesos que fallan. La segunda categoria mas frecuente es **Libertad de Riesgo**, asociada a errores de privacidad, medicacion, facturacion e inventario.

## Distribucion por modulo

| Caracteristica ISO/IEC 25022 | App Movil | Facturacion | Farmacia | HCE | Imagenologia | Laboratorio | Portal Citas | Reportes Gerenciales | Telemedicina |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Cobertura de Contexto | 122 | 0 | 0 | 47 | 37 | 0 | 37 | 0 | 0 |
| Efectividad | 80 | 94 | 99 | 458 | 86 | 136 | 314 | 53 | 289 |
| Eficiencia | 37 | 35 | 34 | 111 | 28 | 30 | 38 | 16 | 31 |
| Libertad de Riesgo | 0 | 261 | 125 | 153 | 0 | 0 | 46 | 19 | 0 |
| Satisfaccion | 39 | 35 | 0 | 0 | 0 | 0 | 110 | 0 | 0 |

## Ejemplos de clasificacion

| ID | Modulo | Incidente | Caracteristica | Justificacion |
| ---: | --- | --- | --- | --- |
| 1210 | HCE | Historial de alergias no carga al abrir la ficha del paciente | Efectividad | El medico no obtiene informacion necesaria para completar la atencion de forma correcta. |
| 1134 | Imagenologia | Tiempo de carga de estudios de imagen supera los 18s | Eficiencia | La tarea sigue siendo posible, pero requiere mas tiempo del aceptable. |
| 2017 | Portal Citas | Formulario confuso, abandono de registro antes de completar la cita | Satisfaccion | La interfaz genera frustracion y reduce la percepcion positiva del usuario. |
| 3846 | HCE | Datos de otro paciente visibles brevemente al abrir un expediente | Libertad de Riesgo | Expone informacion sensible y genera riesgo de privacidad y seguridad del paciente. |
| 2196 | Portal Citas | Boton de confirmar cita no responde en dispositivos moviles | Cobertura de Contexto | El problema depende del contexto de uso: dispositivos moviles. |

## Analisis del incidente tipo 1005

El incidente "Datos de otro paciente visibles brevemente" corresponde principalmente a **Libertad de Riesgo** y no a **Efectividad**.

Aunque tambien es un error del sistema, el punto central no es si el usuario completo o no la tarea. El problema principal es que se expone informacion clinica de otra persona, lo que puede causar riesgos de privacidad, confidencialidad, seguridad del paciente y cumplimiento normativo. Por eso, segun ISO/IEC 25022, se clasifica como Libertad de Riesgo.

## Preguntas de discusion

### 1. Puede un sistema ser efectivo pero no eficiente?

Si. Por ejemplo, un medico puede lograr abrir la ficha clinica y registrar una nota de evolucion, pero si el sistema tarda mas de 20 segundos en cargar o guardar, la tarea se completa con un consumo excesivo de tiempo. En ese caso hay efectividad, pero baja eficiencia.

### 2. Por que la Cobertura de Contexto es relevante para una red hospitalaria con sedes en cinco ciudades?

Porque MediSalud opera en Quito, Guayaquil, Cuenca, Ambato y Manta, con usuarios, dispositivos, conectividad y condiciones operativas distintas. Un sistema puede funcionar bien en un hospital principal, pero fallar en app movil, tablet, telemedicina o sedes con menor conectividad. La calidad en uso debe comprobarse en todos esos contextos reales, no solo en un ambiente ideal.

## Entregables generados

- Tabla completa clasificada: `data/incidentes_2025_clasificados_iso25022.csv`
- Script reproducible de clasificacion: `scripts/clasificar_incidentes_iso25022.py`

## Conclusion parcial

ISO/IEC 25022 permite transformar reportes ambiguos de usuarios en evidencia estructurada de Calidad en Uso. En MediSalud HIS, la prioridad inicial deberia estar en reducir incidentes de Efectividad en HCE, Portal Citas y Telemedicina, y atender con urgencia los casos de Libertad de Riesgo en Facturacion, HCE y Farmacia por su impacto potencial sobre pacientes y organizacion.
