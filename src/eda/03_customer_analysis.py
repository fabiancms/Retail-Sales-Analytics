"""
==========================================================
Proyecto: Retail Sales Analytics
Archivo : 03_customer_analysis.py

Descripción:
Análisis de clientes y segmentos.

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

IMAGE_FOLDER = PROJECT_ROOT / "images" / "customers"

# ==========================================================
# Cargar datos
# ==========================================================

df = pd.read_csv(INPUT_FILE)



# ==========================================================
# Top 10 Clientes por Ventas
# ==========================================================

sales_by_customer = (
    df.groupby("Customer Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
)

print("\nTop 10 Clientes por Ventas:")
print(sales_by_customer)



# ==========================================================
# Gráfico - Top 10 Clientes por Ventas
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    sales_by_customer["Customer Name"],
    sales_by_customer["Sales"]
)

plt.title("Top 10 Clientes por Ventas", fontsize=16, fontweight="bold")
plt.xlabel("Ventas (USD)", fontsize=12)
plt.ylabel("Cliente", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(sales_by_customer["Sales"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "01_top10_customers_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Top 10 Clientes por Ganancias
# ==========================================================

profit_by_customer = (
    df.groupby("Customer Name", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
)

print("\nTop 10 Clientes por Ganancias:")
print(profit_by_customer)



# ==========================================================
# Gráfico - Top 10 Clientes por Ganancias
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    profit_by_customer["Customer Name"],
    profit_by_customer["Profit"]
)

plt.title("Top 10 Clientes por Ganancias", fontsize=16, fontweight="bold")
plt.xlabel("Ganancias (USD)", fontsize=12)
plt.ylabel("Cliente", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(profit_by_customer["Profit"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "02_top10_customers_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Ventas por Segmento
# ==========================================================

sales_by_segment = (
    df.groupby("Segment", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
)

print("\nVentas por Segmento:")
print(sales_by_segment)


# ==========================================================
# Gráfico - Ventas por Segmento
# ==========================================================

plt.figure(figsize=(8, 6))

plt.bar(
    sales_by_segment["Segment"],
    sales_by_segment["Sales"]
)

plt.title("Ventas por Segmento", fontsize=16, fontweight="bold")
plt.xlabel("Segmento", fontsize=12)
plt.ylabel("Ventas (USD)", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

for i, value in enumerate(sales_by_segment["Sales"]):
    plt.text(
        i,
        value,
        f"${value:,.0f}",
        ha="center",
        va="bottom",
        fontsize=10
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "03_sales_by_segment.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Conclusiones
# ==========================================================

top_sales_customer = sales_by_customer.iloc[0]
top_profit_customer = profit_by_customer.iloc[0]
top_segment = sales_by_segment.iloc[0]

print("\n========== CONCLUSIONES ==========")

print(
    f"- El cliente con mayores ventas es "
    f"{top_sales_customer['Customer Name']} "
    f"(${top_sales_customer['Sales']:,.0f})."
)

print(
    f"- El cliente más rentable es "
    f"{top_profit_customer['Customer Name']} "
    f"(${top_profit_customer['Profit']:,.0f})."
)

print(
    f"- El segmento con mayores ventas es "
    f"{top_segment['Segment']} "
    f"(${top_segment['Sales']:,.0f})."
)

if top_sales_customer["Customer Name"] != top_profit_customer["Customer Name"]:
    print(
        "- El cliente con mayores ventas no coincide con el cliente más rentable, "
        "lo que indica que un mayor volumen de ventas no siempre genera la mayor ganancia."
    )
    
