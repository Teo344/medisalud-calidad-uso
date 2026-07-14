from __future__ import annotations

import csv
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "data" / "encuesta_satisfaccion.csv"

SEDES = ["Quito", "Guayaquil", "Cuenca", "Ambato", "Manta"]
ROLES = ["Medico", "Enfermeria", "Admision", "Farmacia", "Paciente", "Gerencia"]
COMENTARIOS = {
    1: "La experiencia fue muy frustrante y no pude completar la tarea con confianza.",
    2: "El sistema funciono, pero requirio demasiados intentos y apoyo.",
    3: "La experiencia fue aceptable, aunque hay puntos de mejora.",
    4: "El sistema permitio completar la tarea con pocas fricciones.",
    5: "La experiencia fue clara, rapida y confiable.",
}


def generar_encuesta(total_respuestas: int = 150) -> list[dict[str, object]]:
    random.seed(25022)
    filas: list[dict[str, object]] = []

    for respuesta_id in range(1, total_respuestas + 1):
        sede = random.choices(SEDES, weights=[34, 30, 14, 11, 11], k=1)[0]
        rol = random.choices(ROLES, weights=[22, 18, 12, 7, 37, 4], k=1)[0]

        # Simula una satisfaccion moderada, afectada por fricciones en portal y HCE.
        puntaje_csat = random.choices([1, 2, 3, 4, 5], weights=[8, 18, 34, 28, 12], k=1)[0]

        filas.append(
            {
                "respuesta_id": respuesta_id,
                "sede": sede,
                "rol": rol,
                "puntaje_csat": puntaje_csat,
                "comentario": COMENTARIOS[puntaje_csat],
            }
        )

    return filas


def main() -> None:
    filas = generar_encuesta()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", newline="", encoding="utf-8") as archivo:
        writer = csv.DictWriter(archivo, fieldnames=filas[0].keys())
        writer.writeheader()
        writer.writerows(filas)

    print(f"Se generaron {len(filas)} respuestas en {OUTPUT}")


if __name__ == "__main__":
    main()
