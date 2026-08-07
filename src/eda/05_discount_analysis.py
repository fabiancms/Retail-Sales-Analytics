"""
==========================================================
Proyecto: Retail Sales Analytics
Archivo : 05_discount_analysis.py

Descripción:
Análisis de descuentos y rentabilidad.

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

IMAGE_FOLDER = PROJECT_ROOT / "images" / "discounts"

# ==========================================================
# Cargar datos
# ==========================================================

df = pd.read_csv(INPUT_FILE)



# ==========================================================
# Distribución de Descuentos
# ==========================================================

discount_distribution = (
    df.groupby("Discount", as_index=False)
        .size()
        .rename(columns={"size": "Cantidad"})
)

print("\nDistribución de Descuentos:")
print(discount_distribution)


# ==========================================================
# Gráfico - Distribución de Descuentos
# ==========================================================

plt.figure(figsize=(10, 6))

plt.bar(
    (discount_distribution["Discount"] * 100).astype(int).astype(str) + "%",
    discount_distribution["Cantidad"]
)

plt.title("Distribución de Descuentos", fontsize=16, fontweight="bold")
plt.xlabel("Descuento", fontsize=12)
plt.ylabel("Cantidad de Registros", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

for i, value in enumerate(discount_distribution["Cantidad"]):
    plt.text(
        i,
        value,
        f"{value}",
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.ylim(0, max(discount_distribution["Cantidad"]) * 1.08)

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "01_discount_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Gráfico - Descuento vs Ganancia
# ==========================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Discount"],
    df["Profit"],
    alpha=0.5
)

plt.title("Relación entre Descuento y Ganancia", fontsize=16, fontweight="bold")
plt.xlabel("Descuento", fontsize=12)
plt.ylabel("Ganancia (USD)", fontsize=12)

plt.xticks(
    [0, 0.2, 0.4, 0.6, 0.8],
    ["0%", "20%", "40%", "60%", "80%"]
)

plt.grid(linestyle="--", alpha=0.4)

plt.axhline(
    y=0,
    color="red",
    linestyle="--",
    linewidth=1.5
)

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "02_discount_vs_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# ==========================================================
# Top 10 Productos con Mayores Pérdidas
# ==========================================================

loss_products = (
    df.groupby("Product Name", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit")
        .head(10)
)

print("\nTop 10 Productos con Mayores Pérdidas:")
print(loss_products)


# ==========================================================
# Gráfico - Top 10 Productos con Mayores Pérdidas
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    loss_products["Product Name"],
    loss_products["Profit"]
)

plt.title("Top 10 Productos con Mayores Pérdidas", fontsize=16, fontweight="bold")
plt.xlabel("Ganancia (USD)", fontsize=12)
plt.ylabel("Producto", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)


for i, value in enumerate(loss_products["Profit"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        ha="left",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "03_top10_loss_products.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# ==========================================================
# Conclusiones
# ==========================================================

most_common_discount = discount_distribution.loc[
    discount_distribution["Cantidad"].idxmax()
]

worst_product = loss_products.iloc[0]

print("\n========== CONCLUSIONES ==========")

print(
    f"- El descuento más utilizado es el {int(most_common_discount['Discount'] * 100)}%, "
    f"con {most_common_discount['Cantidad']} registros."
)

print(
    "- A medida que aumentan los descuentos, se observa una mayor presencia "
    "de transacciones con ganancias bajas o pérdidas."
)

print(
    f"- El producto con mayores pérdidas es "
    f"'{worst_product['Product Name']}' "
    f"(${worst_product['Profit']:,.0f})."
)

print(
    "- Se recomienda revisar la estrategia de descuentos para productos con "
    "baja rentabilidad."
)

