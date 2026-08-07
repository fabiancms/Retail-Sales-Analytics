"""
==========================================================
Proyecto: Retail Sales Analytics
Archivo : 01_sales_analysis.py

Descripción:
Análisis de ventas y ganancias.

Autor: Fabian Medina
==========================================================
"""

# ==========================================================
# Importación de librerías
# ==========================================================

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================================
# Configuración
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parents[2]

INPUT_FILE = PROJECT_ROOT / "data" / "processed" / "Superstore_Clean.csv"

IMAGE_FOLDER = PROJECT_ROOT / "images" / "sales"

# ==========================================================
# Cargar datos
# ==========================================================

df = pd.read_csv(INPUT_FILE)

# ==========================================================
# KPIs generales
# ==========================================================

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()
average_ticket = total_sales / total_orders

print("\n========== KPIs GENERALES ==========")
print(f"Ventas Totales      : ${total_sales:,.2f}")
print(f"Ganancia Total      : ${total_profit:,.2f}")
print(f"Número de Órdenes   : {total_orders}")
print(f"Número de Clientes  : {total_customers}")
print(f"Ticket Promedio     : ${average_ticket:,.2f}")

# ==========================================================
# Ventas por año
# ==========================================================

sales_by_year = (
    df.groupby("Year", as_index=False)["Sales"]
    .sum()
    .sort_values("Year")
)

print("\nVentas por año:")
print(sales_by_year)

# ==========================================================
# Gráfico - Ventas por año
# ==========================================================

plt.figure(figsize=(10, 6))

plt.plot(
    sales_by_year["Year"],
    sales_by_year["Sales"],
    marker="o",
    linewidth=2.5,
    markersize=8
)

plt.title(
    "Ventas por Año",
    fontsize=16,
    fontweight="bold"
)

plt.xlabel("Año", fontsize=12)
plt.ylabel("Ventas (USD)", fontsize=12)

plt.xticks(sales_by_year["Year"])

plt.grid(
    linestyle="--",
    alpha=0.4
)

# Mostrar el valor de cada punto
for x, y in zip(sales_by_year["Year"], sales_by_year["Sales"]):
    plt.text(
        x,
        y,
        f"${y:,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "01_sales_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Ganancias por año
# ==========================================================

profit_by_year = (
    df.groupby("Year", as_index=False)["Profit"]
    .sum()
    .sort_values("Year")
)

print("\nGanancias por año:")
print(profit_by_year)

# ==========================================================
# Gráfico - Ganancias por año
# ==========================================================

plt.figure(figsize=(10, 6))

plt.plot(
    profit_by_year["Year"],
    profit_by_year["Profit"],
    marker="o",
    linewidth=2.5,
    markersize=8
)

plt.title("Ganancias por Año", fontsize=16, fontweight="bold")
plt.xlabel("Año", fontsize=12)
plt.ylabel("Ganancias (USD)", fontsize=12)

plt.xticks(profit_by_year["Year"])

plt.grid(linestyle="--", alpha=0.4)

for x, y in zip(profit_by_year["Year"], profit_by_year["Profit"]):
    plt.text(
        x,
        y,
        f"${y:,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "02_profit_by_year.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Ventas por mes
# ==========================================================

df["Year_Month"] = pd.to_datetime(df["Order Date"]).dt.strftime("%Y-%m")

sales_by_month = (
    df.groupby("Year_Month", as_index=False)["Sales"]
      .sum()
)

print("\nVentas por mes:")
print(sales_by_month.head())

# ==========================================================
# Gráfico - Ventas por mes
# ==========================================================

plt.figure(figsize=(12, 6))

plt.plot(
    sales_by_month["Year_Month"],
    sales_by_month["Sales"],
    linewidth=2.5
)

plt.title("Ventas por Mes", fontsize=16, fontweight="bold")
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ventas (USD)", fontsize=12)

plt.xticks(rotation=45)

plt.grid(linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "03_sales_by_month.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Crear columna Año-Mes
# ==========================================================

df["Year_Month"] = pd.to_datetime(df["Order Date"]).dt.strftime("%Y-%m")



# ==========================================================
# Ganancias por mes
# ==========================================================

profit_by_month = (
    df.groupby("Year_Month", as_index=False)["Profit"]
        .sum()
)

print("\nGanancias por mes:")
print(profit_by_month.head())


# ==========================================================
# Gráfico - Ganancias por mes
# ==========================================================

plt.figure(figsize=(12, 6))

plt.plot(
    profit_by_month["Year_Month"],
    profit_by_month["Profit"],
    linewidth=2.5
)

plt.title("Ganancias por Mes", fontsize=16, fontweight="bold")
plt.xlabel("Mes", fontsize=12)
plt.ylabel("Ganancias (USD)", fontsize=12)

plt.xticks(rotation=45)

plt.grid(linestyle="--", alpha=0.4)

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "04_profit_by_month.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Conclusiones
# ==========================================================

print("\n========== CONCLUSIONES ==========")

print("- Las ventas presentan una tendencia creciente durante el periodo analizado.")
print("- El año 2017 registró el mayor volumen de ventas.")
print("- Las ganancias también muestran un crecimiento general, aunque con variaciones mensuales.")
print("- Se recomienda analizar las categorías y productos que impulsaron el crecimiento de las ventas.")


