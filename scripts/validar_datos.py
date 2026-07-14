from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"

TIEMPO_MIN = 0.0
TIEMPO_MAX = 120.0
CSAT_MIN = 1
CSAT_MAX = 5


def validar_logs_hce(df: pd.DataFrame) -> None:
    print("=== Validacion: logs_hce.csv ===\n")

    print("Valores nulos por columna:")
    print(df.isnull().sum().to_string())

    fuera_de_rango = df[(df["tiempo_segundos"] < TIEMPO_MIN) | (df["tiempo_segundos"] > TIEMPO_MAX)]
    print(f"\nEventos con tiempo_segundos fuera de rango (<{TIEMPO_MIN} o >{TIEMPO_MAX}): {len(fuera_de_rango)}")
    if len(fuera_de_rango):
        print(fuera_de_rango.to_string(index=False))

    duplicados = df.duplicated(subset=["evento_id"]).sum()
    print(f"\nEventos duplicados (evento_id repetido): {duplicados}")

    print("\nResumen estadistico de tiempo_segundos:")
    print(df["tiempo_segundos"].describe().to_string())

    print("\nEventos por sede:")
    print(df["sede"].value_counts().to_string())

    print("\nProporcion de notas completadas:")
    print(df["completada"].mean().round(4))


def validar_encuesta(df: pd.DataFrame) -> None:
    print("\n\n=== Validacion: encuesta_satisfaccion.csv ===\n")

    print("Valores nulos por columna:")
    print(df.isnull().sum().to_string())

    fuera_de_rango = df[(df["puntaje_csat"] < CSAT_MIN) | (df["puntaje_csat"] > CSAT_MAX)]
    print(f"\nRespuestas con puntaje_csat fuera de rango (<{CSAT_MIN} o >{CSAT_MAX}): {len(fuera_de_rango)}")

    duplicados = df.duplicated(subset=["respuesta_id"]).sum()
    print(f"\nRespuestas duplicadas (respuesta_id repetido): {duplicados}")

    print("\nResumen estadistico de puntaje_csat:")
    print(df["puntaje_csat"].describe().to_string())

    print("\nRespuestas por sede:")
    print(df["sede"].value_counts().to_string())

    print("\nRespuestas por rol:")
    print(df["rol"].value_counts().to_string())


def main() -> None:
    logs = pd.read_csv(DATA_DIR / "logs_hce.csv")
    encuesta = pd.read_csv(DATA_DIR / "encuesta_satisfaccion.csv")

    validar_logs_hce(logs)
    validar_encuesta(encuesta)


if __name__ == "__main__":
    main()
