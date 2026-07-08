# MediSalud – Grupo 4

Repositorio de trabajo del **Taller Guiado Integral: Medición de la Calidad en Uso
mediante ISO/IEC 25022**, desarrollado sobre el caso de estudio empresarial
**Red Hospitalaria MediSalud Ecuador** y su sistema **MediSalud HIS**.

---

## 📌 Descripción del trabajo

Este repositorio documenta el recorrido completo de un programa de medición de
**Calidad en Uso** (ISO/IEC 25022), dentro del marco general **ISO/IEC 25000 (SQuaRE)**,
aplicado al sistema de Historia Clínica Electrónica de MediSalud. El equipo asume el rol
de **consultores externos de Calidad de Software** contratados por la Gerencia de Calidad
de MediSalud para:

1. Comprender el marco normativo (ISO/IEC 25010, 25022, SQuaRE).
2. Identificar atributos y características de Calidad en Uso relevantes para el caso.
3. Diseñar métricas, obtener datos y automatizar su medición con Python.
4. Construir indicadores (KPI), interpretarlos y presentarlos a nivel ejecutivo.
5. Proponer un plan de mejora continua.

El desarrollo se organiza en **12 escenarios**, cada uno con fundamento teórico y
actividad práctica de laboratorio, más un **Reto Final Integrador**.

---

## 👥 Equipo de trabajo

| Integrante | Contacto |
|---|---|
| Mateo Criollo | usuario1@ejemplo.com |
| Eduardo Garcia | usuario2@ejemplo.com |
| Mateo Iza | usuario3@ejemplo.com |
| Josue Guallichico | usuario4@ejemplo.com |


---

## 📁 Estructura del repositorio

```
MediSalud-Grupo4/
├── data/         # Datasets de trabajo (CSV, logs, JSON simulados de MediSalud HIS)
├── scripts/      # Scripts Python de medición y automatización
├── dashboards/   # Notebooks y tableros de visualización de indicadores
├── docs/         # Documentos de análisis, plantillas y entregables por escenario
├── reportes/     # Informes ejecutivos y reportes finales
├── venv/         # Entorno virtual local (no versionado)
├── .gitignore
└── README.md
```

---

## ⚙️ Configuración del entorno de trabajo

### Requisitos previos

- [Git](https://git-scm.com/)
- [Python 3.11+](https://python.org)
- Cuenta de GitHub con acceso al repositorio

### 1. Clonar el repositorio

```bash
git clone https://github.com/Teo344/MediSalud-Grupo4.git
cd MediSalud-Grupo4
```

### 2. Crear y activar el entorno virtual

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

**Windows (CMD):**

```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

> ✘ **Error frecuente:** `python3: command not found` en Windows.
> **Solución:** usar `python` en lugar de `python3`, y verificar que la casilla
> *"Add Python to PATH"* haya sido marcada durante la instalación del intérprete.

### 3. Instalar dependencias

```bash
python -m pip install --upgrade pip
pip install pandas numpy matplotlib plotly jupyter openpyxl
```

### 4. Verificar la instalación

```bash
python --version
pip list
```

### 5. Desactivar el entorno al finalizar la sesión de trabajo

```bash
deactivate
```

---

## 📄 Documentación por escenario

| Escenario | Documento |
|---|---|
| 1. Introducción al caso empresarial | [docs/analisis_inicial.md](docs/analisis_inicial.md) |

*(Esta tabla se irá completando con los entregables de cada escenario a medida que
avanza el taller.)*

---

## 📚 Marco normativo de referencia

- **ISO/IEC 25000** — Guía general SQuaRE
- **ISO/IEC 25010** — Modelo de Calidad (qué medir)
- **ISO/IEC 25022** — Medición de Calidad en Uso (cómo medir)
