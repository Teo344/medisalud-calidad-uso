from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "incidentes_2025_iso_25022.csv"
DEFAULT_OUTPUT = ROOT / "data" / "incidentes_2025_clasificados_iso25022.csv"


RISK_KEYWORDS = (
    "datos de otro paciente",
    "dosis incorrecta",
    "interaccion medicamentosa",
    "medicamento controlado",
    "vencimiento de lote",
    "doble cobro",
    "factura duplicada",
    "factura generada con el nombre",
    "copago",
    "reembolso",
    "discrepancia entre el monto",
    "discrepancia entre el reporte financiero",
    "nota de credito",
    "bono de consulta",
    "inventario del sistema no coincide",
    "duplicidad de codigos",
)

EFFICIENCY_KEYWORDS = (
    "tarda",
    "tiempo de respuesta",
    "tiempo de carga",
    "retraso",
    "supera los",
    "consumo elevado",
)

SATISFACTION_KEYWORDS = (
    "formulario confuso",
    "abandono",
    "no envia la confirmacion",
    "notificaciones push no llegan",
    "notificacion de recordatorio",
    "factura electronica no llega",
    "correo electronico",
)

CONTEXT_KEYWORDS = (
    "dispositivos moviles",
    "desde la app",
    "app no permite",
    "aplicacion se cierra",
    "biometria falla",
    "version desactualizada",
    "tablet",
    "datos moviles",
)


def classify(description: str) -> tuple[str, str]:
    text = description.lower()

    if any(keyword in text for keyword in RISK_KEYWORDS):
        return (
            "Libertad de Riesgo",
            "El incidente puede generar impacto clínico, económico, de privacidad o seguridad para el paciente o la organización.",
        )

    if any(keyword in text for keyword in EFFICIENCY_KEYWORDS):
        return (
            "Eficiencia",
            "El usuario puede intentar completar la tarea, pero el problema incrementa tiempo, esfuerzo o consumo de recursos.",
        )

    if any(keyword in text for keyword in CONTEXT_KEYWORDS):
        return (
            "Cobertura de Contexto",
            "El problema aparece en un contexto específico de uso, dispositivo, canal o condición operativa.",
        )

    if any(keyword in text for keyword in SATISFACTION_KEYWORDS):
        return (
            "Satisfacción",
            "El incidente afecta la comodidad, confianza o percepción positiva del usuario aunque no siempre bloquee la tarea principal.",
        )

    return (
        "Efectividad",
        "El incidente impide o degrada la completitud/precisión con que el usuario alcanza su objetivo principal.",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Clasifica incidentes MediSalud segun las caracteristicas ISO/IEC 25022."
    )
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    required = {"id", "fecha", "modulo", "descripcion", "rol_usuario", "sede"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Faltan columnas requeridas: {sorted(missing)}")

    classified = df["descripcion"].map(classify)
    df["caracteristica_iso25022"] = classified.map(lambda item: item[0])
    df["justificacion"] = classified.map(lambda item: item[1])

    args.output.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(args.output, index=False, encoding="utf-8")

    summary = (
        df.groupby("caracteristica_iso25022")
        .size()
        .rename("incidentes")
        .sort_values(ascending=False)
    )
    print(summary.to_string())
    print(f"\nArchivo generado: {args.output}")


if __name__ == "__main__":
    main()
