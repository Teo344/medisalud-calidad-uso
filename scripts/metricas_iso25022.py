from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

UMBRAL_TIEMPO_TAREA = 8.0
UMBRAL_TASA_ERROR_FACT = 0.01
UMBRAL_EFECTIVIDAD = 0.95
UMBRAL_SATISFACCION = 0.80
TOTAL_TRANSACCIONES_FACTURACION = 8500


def _leer_csv(nombre: str) -> pd.DataFrame:
    ruta = DATA_DIR / nombre
    if not ruta.exists():
        raise FileNotFoundError(f"No existe el archivo requerido: {ruta}")
    return pd.read_csv(ruta)


def _leer_incidentes() -> pd.DataFrame:
    candidatos = [
        DATA_DIR / "incidentes_2025.csv",
        DATA_DIR / "incidentes_2025_iso_25022.csv",
        DATA_DIR / "incidentes_2025_clasificados_iso25022.csv",
    ]
    for ruta in candidatos:
        if ruta.exists():
            return pd.read_csv(ruta)
    raise FileNotFoundError("No se encontro un CSV de incidentes en data/.")


def _validar_columnas(df: pd.DataFrame, columnas: set[str], nombre: str) -> None:
    faltantes = columnas.difference(df.columns)
    if faltantes:
        raise ValueError(f"{nombre} no contiene columnas requeridas: {sorted(faltantes)}")


def cargar_datos() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    logs = _leer_csv("logs_hce.csv")
    encuesta = _leer_csv("encuesta_satisfaccion.csv")
    incidentes = _leer_incidentes()

    _validar_columnas(
        logs,
        {"evento_id", "timestamp", "sede", "medico_id", "tiempo_segundos", "completada"},
        "logs_hce.csv",
    )
    _validar_columnas(
        encuesta,
        {"respuesta_id", "sede", "rol", "puntaje_csat", "comentario"},
        "encuesta_satisfaccion.csv",
    )
    _validar_columnas(incidentes, {"id", "fecha", "modulo", "descripcion"}, "incidentes")

    return logs, encuesta, incidentes


def metrica_efectividad(logs: pd.DataFrame) -> dict[str, object]:
    total = len(logs)
    completadas = int(logs["completada"].sum())
    valor = round(completadas / total, 4) if total else 0.0
    return {
        "nombre": "Completitud de registro de HCE",
        "caracteristica": "Efectividad",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_EFECTIVIDAD,
        "cumple": valor >= UMBRAL_EFECTIVIDAD,
        "detalle": f"{completadas} de {total} registros completados",
    }


def metrica_eficiencia(logs: pd.DataFrame) -> dict[str, object]:
    valor = round(float(logs["tiempo_segundos"].mean()), 2)
    return {
        "nombre": "Tiempo promedio de registro de HCE",
        "caracteristica": "Eficiencia",
        "valor": valor,
        "unidad": "segundos",
        "umbral": UMBRAL_TIEMPO_TAREA,
        "cumple": valor <= UMBRAL_TIEMPO_TAREA,
        "detalle": "Promedio de tiempo_segundos en logs_hce.csv",
    }


def metrica_eficiencia_por_sede(logs: pd.DataFrame) -> pd.DataFrame:
    return (
        logs.groupby("sede", as_index=False)
        .agg(
            eventos=("evento_id", "count"),
            tiempo_promedio_segundos=("tiempo_segundos", "mean"),
            porcentaje_completado=("completada", "mean"),
        )
        .round({"tiempo_promedio_segundos": 2, "porcentaje_completado": 4})
    )


def metrica_satisfaccion(encuesta: pd.DataFrame) -> dict[str, object]:
    promedio_csat = float(encuesta["puntaje_csat"].mean())
    valor = round(promedio_csat / 5, 4)
    return {
        "nombre": "Indice de satisfaccion CSAT normalizado",
        "caracteristica": "Satisfaccion",
        "valor": valor,
        "unidad": "proporcion 0-1",
        "umbral": UMBRAL_SATISFACCION,
        "cumple": valor >= UMBRAL_SATISFACCION,
        "detalle": f"CSAT promedio {promedio_csat:.2f} sobre 5",
    }


def metrica_libertad_riesgo(
    incidentes: pd.DataFrame,
    total_transacciones: int = TOTAL_TRANSACCIONES_FACTURACION,
) -> dict[str, object]:
    incidentes_facturacion = incidentes[incidentes["modulo"] == "Facturacion"]
    valor = round(len(incidentes_facturacion) / total_transacciones, 4)
    return {
        "nombre": "Tasa de errores de facturacion",
        "caracteristica": "Libertad de Riesgo",
        "valor": valor,
        "unidad": "proporcion",
        "umbral": UMBRAL_TASA_ERROR_FACT,
        "cumple": valor <= UMBRAL_TASA_ERROR_FACT,
        "detalle": f"{len(incidentes_facturacion)} incidentes de facturacion / {total_transacciones} transacciones",
    }


def metrica_cobertura_contexto(logs: pd.DataFrame) -> dict[str, object]:
    eficiencia_sede = metrica_eficiencia_por_sede(logs)
    sedes_cumplen = int(
        (eficiencia_sede["tiempo_promedio_segundos"] <= UMBRAL_TIEMPO_TAREA).sum()
    )
    total_sedes = len(eficiencia_sede)
    valor = round(sedes_cumplen / total_sedes, 4) if total_sedes else 0.0
    return {
        "nombre": "Cobertura de contexto por sede",
        "caracteristica": "Cobertura de Contexto",
        "valor": valor,
        "unidad": "proporcion de sedes que cumplen eficiencia",
        "umbral": 1.0,
        "cumple": valor >= 1.0,
        "detalle": f"{sedes_cumplen} de {total_sedes} sedes cumplen tiempo <= {UMBRAL_TIEMPO_TAREA}s",
    }


def generar_reporte() -> tuple[dict[str, dict[str, object]], pd.DataFrame]:
    logs, encuesta, incidentes = cargar_datos()
    reporte = {
        "efectividad": metrica_efectividad(logs),
        "eficiencia": metrica_eficiencia(logs),
        "satisfaccion": metrica_satisfaccion(encuesta),
        "libertad_riesgo": metrica_libertad_riesgo(incidentes),
        "cobertura_contexto": metrica_cobertura_contexto(logs),
    }
    return reporte, metrica_eficiencia_por_sede(logs)


def main() -> None:
    reporte, eficiencia_sede = generar_reporte()

    print("=== Reporte de Calidad en Uso - MediSalud HIS ===\n")
    for metrica in reporte.values():
        estado = "CUMPLE" if metrica["cumple"] else "NO CUMPLE"
        print(
            f"{metrica['nombre']}: {metrica['valor']} {metrica['unidad']} "
            f"(umbral: {metrica['umbral']}) -> {estado}"
        )
        print(f"  {metrica['detalle']}")

    print("\n=== Eficiencia por sede (Cobertura de Contexto) ===")
    print(eficiencia_sede.to_string(index=False))


if __name__ == "__main__":
    main()
