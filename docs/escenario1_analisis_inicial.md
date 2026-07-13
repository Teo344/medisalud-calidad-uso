# Análisis Inicial del Caso — MediSalud Ecuador

**Escenario 1 — Introducción al Caso Empresarial**
**Norma de referencia:** ISO/IEC 25022 (Measurement of Quality in Use)
**Grupo:** Grupo 4
**Rol asumido:** Consultores externos de Calidad de Software contratados por la Gerencia de Calidad de MediSalud

---

## 1. Contexto de partida

MediSalud Ecuador es una red hospitalaria privada que opera 4 hospitales, 12 centros
ambulatorios, un laboratorio clínico, una central de imagenología y un servicio de
telemedicina, sobre un único sistema núcleo: **MediSalud HIS**. Actualmente, las decisiones
de TI se toman **por percepción** ("el sistema funciona bien porque los servidores están
arriba"), sin evidencia medible sobre la experiencia real del usuario. Este análisis inicial
busca identificar, antes de aplicar cualquier norma, dónde está la brecha entre percepción
y evidencia.

---

## 2. Matriz de Análisis Inicial del Caso MediSalud

### Pregunta guía 1 — ¿Cuáles son los 3 procesos más críticos del negocio?

| # | Proceso crítico | Justificación |
|---|---|---|
| 1 | **Atención médica y registro de historia clínica (HCE)** | Es el proceso con mayor riesgo clínico: las quejas de lentitud en horas pico (10:00–12:00) pueden retrasar decisiones médicas urgentes. Afecta directamente al RNF-01 (registro ≤ 8s en el 90 % de los casos). |
| 2 | **Agendamiento y admisión de pacientes** | Es la puerta de entrada de los 38.000+ pacientes activos mensuales. El incremento del tiempo de espera para agendar citas vía portal impacta directamente la retención de usuarios (riesgo reputacional). |
| 3 | **Facturación y gestión de seguros/reaseguros** | Los errores de doble facturación reportados por el área financiera representan un riesgo financiero directo sobre el flujo de caja y la relación con aseguradoras. |

> *Nota:* La telemedicina (abandono de sesiones antes de completar el registro de síntomas)
> es un cuarto proceso relevante, pero se considera de criticidad secundaria frente a los
> tres anteriores por tratarse de un servicio aún en expansión (desde 2022) y no del núcleo
> histórico de la operación.

---

### Pregunta guía 2 — ¿Qué usuarios se ven más afectados por la problemática actual?

| Perfil de usuario | Usuarios activos | Cómo lo afecta la problemática actual |
|---|---|---|
| **Médico tratante** | 640 | Lentitud del módulo HCE en horas pico; riesgo de exposición breve de datos de otro paciente (incidente de seguridad). |
| **Paciente (portal/app)** | 38.000+ | Mayor tiempo de espera para agendar citas; abandono de sesiones de telemedicina antes de completar el registro de síntomas. |
| **Personal de admisión** | 210 | Errores de doble facturación que generan reprocesos y reclamos. |
| **Enfermería** | 910 | Afectada indirectamente por la lentitud general del HIS al registrar signos vitales y administración de medicamentos. |
| **Gerencia / Calidad** | 45 | No sufre el problema operativo directamente, pero carece de indicadores objetivos para tomar decisiones (es quien encarga este programa de medición). |

**Conclusión:** los más afectados en volumen son los **pacientes** (38.000+), pero los más
afectados en **criticidad clínica** son los **médicos tratantes**, ya que un retraso en el
registro de HCE puede tener consecuencias directas sobre la seguridad del paciente.

---

### Pregunta guía 3 — ¿Qué evidencia tiene hoy MediSalud sobre la calidad de su software?

- **Disponibilidad de servidores (uptime)**: es el único indicador que TI utiliza hoy para
  afirmar que "el sistema funciona correctamente".
- **Logs centralizados y métricas de infraestructura**, descritos explícitamente como
  *"aún incipientes, sin estandarizar"* — existen, pero no están consolidados ni orientados
  a la experiencia del usuario.
- **Quejas informales y anecdóticas** de médicos, personal de admisión y pacientes, recibidas
  por la Gerencia de Calidad, pero sin cuantificar ni sistematizar.

**Conclusión:** la evidencia actual es **técnica-operativa** (uptime, infraestructura) y
**anecdótica** (quejas), pero no existe ninguna evidencia centrada en el usuario real
realizando tareas reales — es decir, no existe medición de **Calidad en Uso**.

---

### Pregunta guía 4 — ¿Qué evidencia le falta?

MediSalud carece de datos objetivos y sistemáticos alineados a las cinco características
de ISO/IEC 25022:

| Característica ISO/IEC 25022 | Evidencia faltante |
|---|---|
| **Efectividad** | % de notas de evolución clínica completadas sin errores; % de citas agendadas exitosamente. |
| **Eficiencia** | Tiempo real de registro de HCE por consulta; tiempo de agendamiento por paciente. |
| **Satisfacción** | Encuestas de satisfacción por rol (médico, paciente, admisión). |
| **Libertad de Riesgo** | Registro formal de incidentes de exposición de datos (como el caso de datos de otro paciente visibles brevemente); tasa de errores de doble facturación. |
| **Cobertura de Contexto** | Comparación de desempeño del sistema entre sedes (Quito, Guayaquil, Cuenca, Ambato, Manta). |

**Conclusión general:** falta transformar quejas dispersas en **métricas normalizadas**,
siguiendo el ciclo que se trabajará en los siguientes escenarios del taller:

> Observar el uso real → Medir con métricas normalizadas → Construir indicadores → Interpretar → Actuar

---

## 3.  Conclusión Parcial

Este análisis inicial evidencia la brecha entre percepción y evidencia en MediSalud.
En el **Escenario 2** se formalizará el vocabulario técnico (las cinco características de
ISO/IEC 25022) para clasificar de manera rigurosa los problemas aquí identificados.
