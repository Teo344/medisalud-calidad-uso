from __future__ import annotations

import csv
import random
from datetime import datetime, timedelta
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "logs_hce.csv"

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
MEDICOS_POR_SEDE = 12
FECHA_INICIO = datetime(2025, 11, 3, 7, 0, 0)
DIAS = 5


def generar_logs() -> list[dict[str, object]]:
    random.seed(42)
    filas: list[dict[str, object]] = []
    evento_id = 1

    for dia in range(DIAS):
        fecha_dia = FECHA_INICIO + timedelta(days=dia)
        for sede in SEDES:
            n_eventos = 180 if sede in ("Quito", "Guayaquil") else 90

            for _ in range(n_eventos):
                hora = random.randint(7, 18)
                minuto = random.randint(0, 59)
                timestamp = fecha_dia.replace(hour=hora, minute=minuto)

                es_hora_pico = 10 <= hora <= 12
                tiempo_base = random.gauss(6.5, 1.5)
                if es_hora_pico:
                    tiempo_base += random.gauss(4.0, 2.0)

                tiempo_segundos = max(1.5, round(tiempo_base, 2))
                completada = random.random() < 0.96
                medico_id = f"MED-{sede[:3].upper()}-{random.randint(1, MEDICOS_POR_SEDE):02d}"

                filas.append(
                    {
                        "evento_id": evento_id,
                        "timestamp": timestamp.isoformat(),
                        "sede": sede,
                        "medico_id": medico_id,
                        "tiempo_segundos": tiempo_segundos,
                        "completada": int(completada),
                    }
                )
                evento_id += 1

    return filas


def main() -> None:
    filas = generar_logs()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=filas[0].keys())
        writer.writeheader()
        writer.writerows(filas)

    print(f"Se generaron {len(filas)} eventos en {OUTPUT}")


if __name__ == "__main__":
    main()
