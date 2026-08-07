"""
==========================================================
Proyecto: Retail Sales Analytics
Archivo : 02_data_cleaning.py

Descripción:
Limpieza y transformación del conjunto de datos.

Autor: Fabian Medina
==========================================================
"""

# ==========================================================
# Importación de librerías
# ==========================================================

import pandas as pd
from pathlib import Path

# ==========================================================
# Configuración
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "raw" / "Superstore.csv"
OUTPUT_FILE = PROJECT_ROOT / "data" / "processed" / "Superstore_Clean.csv"

# ==========================================================
# Cargar datos
# ==========================================================

df = pd.read_csv(INPUT_FILE, encoding="latin-1")

# ==========================================================
# Conversión de fechas
# ==========================================================

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])


# ==========================================================
# Validaciones
# ==========================================================

print("\nTipos de datos:")
print(df.dtypes)

# ==========================================================
# Validación de calidad de datos
# ==========================================================

print("\nRegistros duplicados:", df.duplicated().sum())

print("\nValores nulos:")
print(df.isnull().sum())


# ==========================================================
# Creación de nuevas columnas
# ==========================================================

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.month
MESES = {
    1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril",
    5: "Mayo", 6: "Junio", 7: "Julio", 8: "Agosto",
    9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"
}

df["Month Name"] = df["Month"].map(MESES)
df["Quarter"] = df["Order Date"].dt.quarter

print("\nNuevas columnas creadas:")
print(df[["Order Date", "Year", "Month", "Month Name", "Quarter"]].head())


# ==========================================================
# Exportar datos limpios
# ==========================================================

df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")

print(f"\nDataset exportado correctamente en:\n{OUTPUT_FILE}")