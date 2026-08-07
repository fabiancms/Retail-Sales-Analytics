"""==========================================================
Proyecto: Retail Sales Analytics
Archivo : 01_data_loading.py

Descripción:
Carga del conjunto de datos y exploración inicial.

Autor: Fabian Medina"""

# ==========================================================
# Importación de librerías
# ==========================================================

import pandas as pd
from pathlib import Path

# ==========================================================
# Configuración
# ==========================================================

# Ruta raíz del proyecto
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Ruta del archivo de datos
DATA_FILE = PROJECT_ROOT / "data" / "raw" / "Superstore.csv"

# ==========================================================
# Cargar el dataset
# ==========================================================

if not DATA_FILE.exists():
    raise FileNotFoundError(f"No se encontró el archivo: {DATA_FILE}")

df = pd.read_csv(DATA_FILE, encoding="latin-1")

# ==========================================================
# Exploración inicial
# ==========================================================

print("\nPrimeras 5 filas:")
print(df.head())

print("\nDimensiones del dataset:")
print(df.shape)

print("\nInformación general:")
print(df.info())

# ==========================================================
# Análisis de la estructura del dataset
# ==========================================================

print("\nNombres de las columnas:")
print(df.columns.tolist())

print("\nValores nulos por columna:")
print(df.isnull().sum())

print("\nEstadísticas descriptivas:")
print(df.describe())