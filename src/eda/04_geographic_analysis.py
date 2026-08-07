"""
==========================================================
Proyecto: Retail Sales Analytics
Archivo : 04_geographic_analysis.py

Descripción:
Análisis geográfico de las ventas.

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

IMAGE_FOLDER = PROJECT_ROOT / "images" / "geography"

# ==========================================================
# Cargar datos
# ==========================================================

df = pd.read_csv(INPUT_FILE)



# ==========================================================
# Ventas por Región
# ==========================================================

sales_by_region = (
    df.groupby("Region", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
)

print("\nVentas por Región:")
print(sales_by_region)


# ==========================================================
# Gráfico - Ventas por Región
# ==========================================================

plt.figure(figsize=(8, 6))

plt.bar(
    sales_by_region["Region"],
    sales_by_region["Sales"]
)

plt.title("Ventas por Región", fontsize=16, fontweight="bold")
plt.xlabel("Región", fontsize=12)
plt.ylabel("Ventas (USD)", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

for i, value in enumerate(sales_by_region["Sales"]):
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
    IMAGE_FOLDER / "01_sales_by_region.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Top 10 Estados por Ventas
# ==========================================================

sales_by_state = (
    df.groupby("State", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
)

print("\nTop 10 Estados por Ventas:")
print(sales_by_state)


# ==========================================================
# Gráfico - Top 10 Estados por Ventas
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    sales_by_state["State"],
    sales_by_state["Sales"]
)

plt.title("Top 10 Estados por Ventas", fontsize=16, fontweight="bold")
plt.xlabel("Ventas (USD)", fontsize=12)
plt.ylabel("Estado", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(sales_by_state["Sales"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "02_top10_states_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Top 10 Estados por Ganancias
# ==========================================================

profit_by_state = (
    df.groupby("State", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
)

print("\nTop 10 Estados por Ganancias:")
print(profit_by_state)



# ==========================================================
# Gráfico - Top 10 Estados por Ganancias
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    profit_by_state["State"],
    profit_by_state["Profit"]
)

plt.title("Top 10 Estados por Ganancias", fontsize=16, fontweight="bold")
plt.xlabel("Ganancias (USD)", fontsize=12)
plt.ylabel("Estado", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(profit_by_state["Profit"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "03_top10_states_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# ==========================================================
# Top 10 Ciudades por Ventas
# ==========================================================

sales_by_city = (
    df.groupby("City", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
)

print("\nTop 10 Ciudades por Ventas:")
print(sales_by_city)

# ==========================================================
# Gráfico - Top 10 Ciudades por Ventas
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    sales_by_city["City"],
    sales_by_city["Sales"]
)

plt.title("Top 10 Ciudades por Ventas", fontsize=16, fontweight="bold")
plt.xlabel("Ventas (USD)", fontsize=12)
plt.ylabel("Ciudad", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(sales_by_city["Sales"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "04_top10_cities_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Conclusiones
# ==========================================================

top_region = sales_by_region.iloc[0]
top_state_sales = sales_by_state.iloc[0]
top_state_profit = profit_by_state.iloc[0]
top_city = sales_by_city.iloc[0]

print("\n========== CONCLUSIONES ==========")

print(
    f"- La región con mayores ventas es "
    f"{top_region['Region']} "
    f"(${top_region['Sales']:,.0f})."
)

print(
    f"- El estado con mayores ventas es "
    f"{top_state_sales['State']} "
    f"(${top_state_sales['Sales']:,.0f})."
)

print(
    f"- El estado más rentable es "
    f"{top_state_profit['State']} "
    f"(${top_state_profit['Profit']:,.0f})."
)

print(
    f"- La ciudad con mayores ventas es "
    f"{top_city['City']} "
    f"(${top_city['Sales']:,.0f})."
)

if top_state_sales["State"] == top_state_profit["State"]:
    print(
        "- El estado con mayores ventas también es el más rentable."
    )
else:
    print(
        "- El estado con mayores ventas no coincide con el estado más rentable."
    )
    
    