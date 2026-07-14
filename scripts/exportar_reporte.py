from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

from metricas_iso25022 import ROOT, generar_reporte


OUTPUT = ROOT / "dashboards" / "indicadores.json"


def main() -> None:
    reporte, eficiencia_sede = generar_reporte()
    salida = {
        "generado_en": datetime.now(timezone.utc).isoformat(),
        "sistema": "MediSalud HIS",
        "norma": "ISO/IEC 25022",
        "metricas": reporte,
        "eficiencia_por_sede": eficiencia_sede.to_dict(orient="records"),
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w", encoding="utf-8") as archivo:
        json.dump(salida, archivo, indent=2, ensure_ascii=False)

    print(f"Reporte exportado a {OUTPUT}")


if __name__ == "__main__":
    main()
