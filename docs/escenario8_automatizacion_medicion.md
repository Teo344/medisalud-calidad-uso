# Escenario 8 - Automatizacion de la Medicion

## Objetivo

Construir un pipeline en Python para calcular automaticamente metricas de Calidad en Uso segun ISO/IEC 25022 para MediSalud HIS, usando datos validados de logs, encuestas e incidentes.

## Archivos generados

| Archivo | Proposito |
| --- | --- |
| `scripts/generar_logs_hce.py` | Genera logs sinteticos de registro de HCE para 5 dias y 5 sedes. |
| `scripts/generar_encuesta_satisfaccion.py` | Genera 150 respuestas simuladas de satisfaccion CSAT. |
| `scripts/metricas_iso25022.py` | Calcula las metricas automatizadas de Calidad en Uso. |
| `scripts/exportar_reporte.py` | Exporta los indicadores a `dashboards/indicadores.json`. |
| `.github/workflows/medicion_calidad.yml` | Automatiza la medicion semanal en GitHub Actions. |
| `data/logs_hce.csv` | Dataset generado de 3.150 eventos HCE. |
| `data/encuesta_satisfaccion.csv` | Dataset generado de 150 respuestas CSAT. |
| `dashboards/indicadores.json` | Archivo JSON final para alimentar dashboards. |

## Pipeline implementado

1. Generacion de datos base:
   - Logs HCE con `evento_id`, `timestamp`, `sede`, `medico_id`, `tiempo_segundos` y `completada`.
   - Encuesta CSAT con `respuesta_id`, `sede`, `rol`, `puntaje_csat` y `comentario`.
2. Carga y validacion de columnas requeridas.
3. Calculo de metricas ISO/IEC 25022.
4. Desagregacion de eficiencia por sede para Cobertura de Contexto.
5. Exportacion de indicadores a JSON.
6. Configuracion de GitHub Actions para ejecutar el pipeline semanalmente o bajo demanda.

## Metricas calculadas

| Caracteristica ISO/IEC 25022 | Metrica | Formula aplicada | Umbral |
| --- | --- | --- | --- |
| Efectividad | Completitud de registro de HCE | registros completados / registros intentados | >= 0,95 |
| Eficiencia | Tiempo promedio de registro de HCE | promedio de `tiempo_segundos` | <= 8 segundos |
| Satisfaccion | CSAT normalizado | promedio CSAT / 5 | >= 0,80 |
| Libertad de Riesgo | Tasa de errores de facturacion | incidentes de facturacion / 8.500 transacciones | <= 0,01 |
| Cobertura de Contexto | Sedes que cumplen eficiencia | sedes con tiempo promedio <= 8s / sedes evaluadas | = 1,00 |

## Resultados obtenidos

| Caracteristica | Valor | Umbral | Estado | Detalle |
| --- | ---: | ---: | --- | --- |
| Efectividad | 0,9651 | 0,95 | Cumple | 3.040 de 3.150 registros completados. |
| Eficiencia | 7,43 s | 8,00 s | Cumple | Tiempo promedio de registro HCE. |
| Satisfaccion | 0,6253 | 0,80 | No cumple | CSAT promedio 3,13 sobre 5. |
| Libertad de Riesgo | 0,0500 | 0,01 | No cumple | 425 incidentes de facturacion sobre 8.500 transacciones. |
| Cobertura de Contexto | 1,0000 | 1,00 | Cumple | 5 de 5 sedes cumplen el umbral de eficiencia. |

## Eficiencia por sede

| Sede | Eventos | Tiempo promedio (s) | Porcentaje completado |
| --- | ---: | ---: | ---: |
| Ambato | 450 | 7,48 | 0,9600 |
| Cuenca | 450 | 7,40 | 0,9578 |
| Guayaquil | 900 | 7,37 | 0,9711 |
| Manta | 450 | 7,52 | 0,9622 |
| Quito | 900 | 7,43 | 0,9667 |

## Interpretacion

El sistema cumple las metricas operativas de HCE para Efectividad y Eficiencia: la proporcion de notas completadas supera el 95% y el tiempo promedio queda por debajo de 8 segundos. Tambien cumple Cobertura de Contexto porque todas las sedes evaluadas se mantienen dentro del umbral de eficiencia.

Los principales problemas aparecen en Satisfaccion y Libertad de Riesgo. El CSAT normalizado de 0,6253 indica que la experiencia percibida por los usuarios no alcanza el nivel esperado. La tasa de errores de facturacion de 5,0% supera ampliamente el limite de 1%, por lo que debe priorizarse por su impacto economico, reputacional y operativo.

## Ejecucion local

Desde la raiz del repositorio:

```bash
python scripts/generar_logs_hce.py
python scripts/generar_encuesta_satisfaccion.py
python scripts/metricas_iso25022.py
python scripts/exportar_reporte.py
```

El resultado final queda en:

```text
dashboards/indicadores.json
```

## Automatizacion con GitHub Actions

El archivo `.github/workflows/medicion_calidad.yml` ejecuta el pipeline cada lunes a las 06:00 UTC y tambien permite ejecucion manual con `workflow_dispatch`.

El flujo realiza estos pasos:

1. Descarga el repositorio.
2. Configura Python 3.11.
3. Instala `pandas` y `numpy`.
4. Genera logs HCE y encuesta CSAT.
5. Calcula metricas ISO/IEC 25022.
6. Exporta `dashboards/indicadores.json`.
7. Publica el JSON como artefacto del workflow.

## Preguntas de discusion

### 1. Que ventajas ofrece programar la medicion en GitHub Actions frente a ejecutarla manualmente cada trimestre?

GitHub Actions permite que la medicion sea repetible, trazable y automatica. Reduce errores humanos, conserva historial de ejecuciones y facilita detectar desviaciones de calidad sin esperar a una revision trimestral. Ademas, convierte la medicion de calidad en uso en una practica continua, alineada con DevOps y mejora continua.

### 2. Que riesgo existe si el umbral `UMBRAL_TIEMPO_TAREA` queda hardcodeado en el script?

El riesgo es que el valor quede oculto dentro del codigo y sea dificil de auditar o ajustar cuando cambien los requerimientos del negocio. Si el umbral pasa de 8 a 6 segundos, por ejemplo, se requeriria modificar codigo fuente en vez de cambiar una configuracion. En un entorno profesional conviene mover los umbrales a un archivo externo, como YAML, JSON o variables de entorno.

## Conclusion parcial

El escenario 8 transforma las metricas definidas para MediSalud HIS en un pipeline ejecutable y reutilizable. La automatizacion permite pasar de mediciones manuales aisladas a un proceso continuo, capaz de alimentar dashboards y apoyar decisiones de mejora basadas en evidencia.
