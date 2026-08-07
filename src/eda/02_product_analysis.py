"""
==========================================================
Proyecto: Retail Sales Analytics
Archivo : 02_product_analysis.py

Descripción:
Análisis de categorías, subcategorías y productos.

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

IMAGE_FOLDER = PROJECT_ROOT / "images" / "products"

# ==========================================================
# Cargar datos
# ==========================================================

df = pd.read_csv(INPUT_FILE)



# ==========================================================
# Ventas por categoría
# ==========================================================

sales_by_category = (
    df.groupby("Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
)

print("\nVentas por categoría:")
print(sales_by_category)


# ==========================================================
# Gráfico - Ventas por categoría
# ==========================================================

plt.figure(figsize=(8, 6))

plt.bar(
    sales_by_category["Category"],
    sales_by_category["Sales"]
)

plt.title("Ventas por Categoría", fontsize=16, fontweight="bold")
plt.xlabel("Categoría", fontsize=12)
plt.ylabel("Ventas (USD)", fontsize=12)

plt.grid(axis="y", linestyle="--", alpha=0.4)

# Mostrar el valor sobre cada barra
for i, value in enumerate(sales_by_category["Sales"]):
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
    IMAGE_FOLDER / "01_sales_by_category.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Top 10 Subcategorías por Ventas
# ==========================================================

sales_by_subcategory = (
    df.groupby("Sub-Category", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
)

print("\nTop 10 Subcategorías por Ventas:")
print(sales_by_subcategory)



# ==========================================================
# Gráfico - Top 10 Subcategorías por Ventas
# ==========================================================

plt.figure(figsize=(10, 6))

plt.barh(
    sales_by_subcategory["Sub-Category"],
    sales_by_subcategory["Sales"]
)

plt.title("Top 10 Subcategorías por Ventas", fontsize=16, fontweight="bold")
plt.xlabel("Ventas (USD)", fontsize=12)
plt.ylabel("Subcategoría", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

# Invertir el eje para mostrar la mayor venta arriba
plt.gca().invert_yaxis()

# Mostrar valores
for i, value in enumerate(sales_by_subcategory["Sales"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "02_top10_subcategories_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

# ==========================================================
# Top 10 Productos por Ventas
# ==========================================================

sales_by_product = (
    df.groupby("Product Name", as_index=False)["Sales"]
        .sum()
        .sort_values("Sales", ascending=False)
        .head(10)
)

print("\nTop 10 Productos por Ventas:")
print(sales_by_product)

# ==========================================================
# Gráfico - Top 10 Productos por Ventas
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    sales_by_product["Product Name"],
    sales_by_product["Sales"]
)

plt.title("Top 10 Productos por Ventas", fontsize=16, fontweight="bold")
plt.xlabel("Ventas (USD)", fontsize=12)
plt.ylabel("Producto", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(sales_by_product["Sales"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "03_top10_products_sales.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()



# ==========================================================
# Top 10 Productos por Ganancias
# ==========================================================

profit_by_product = (
    df.groupby("Product Name", as_index=False)["Profit"]
        .sum()
        .sort_values("Profit", ascending=False)
        .head(10)
)

print("\nTop 10 Productos por Ganancias:")
print(profit_by_product)


# ==========================================================
# Gráfico - Top 10 Productos por Ganancias
# ==========================================================

plt.figure(figsize=(12, 7))

plt.barh(
    profit_by_product["Product Name"],
    profit_by_product["Profit"]
)

plt.title("Top 10 Productos por Ganancias", fontsize=16, fontweight="bold")
plt.xlabel("Ganancias (USD)", fontsize=12)
plt.ylabel("Producto", fontsize=12)

plt.grid(axis="x", linestyle="--", alpha=0.4)

plt.gca().invert_yaxis()

for i, value in enumerate(profit_by_product["Profit"]):
    plt.text(
        value,
        i,
        f"${value:,.0f}",
        va="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig(
    IMAGE_FOLDER / "04_top10_products_profit.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# ==========================================================
# Conclusiones
# ==========================================================

top_category = sales_by_category.iloc[0]
top_subcategory = sales_by_subcategory.iloc[0]
top_sales_product = sales_by_product.iloc[0]
top_profit_product = profit_by_product.iloc[0]

print("\n========== CONCLUSIONES ==========")

print(
    f"- {top_category['Category']} es la categoría con mayores ventas "
    f"(${top_category['Sales']:,.0f})."
)

print(
    f"- La subcategoría {top_subcategory['Sub-Category']} lidera las ventas "
    f"(${top_subcategory['Sales']:,.0f})."
)

print(
    f"- El producto con mayores ventas es "
    f"'{top_sales_product['Product Name']}' "
    f"(${top_sales_product['Sales']:,.0f})."
)

print(
    f"- El producto con mayor ganancia es "
    f"'{top_profit_product['Product Name']}' "
    f"(${top_profit_product['Profit']:,.0f})."
)