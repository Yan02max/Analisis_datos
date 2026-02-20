import pandas as pd
import numpy as np

data = {
    "Producto": ["Laptop", "Laptop", "Mouse", "Mouse", "Tablet", "Tablet"],
    "Region": ["Norte", "Sur", "Norte", "Sur", "Norte", "Sur"],
    "Ventas": [1000, 800, 200, 150, 500, 400],
    "Costo": [700, 600, 100, 90, 300, 250]
}

df = pd.DataFrame(data)
df.loc[(df["Region"] == "Sur") & (df["Producto"] == "Laptop"), "Ventas"] *= 1.44
df["Ganancias"] = df["Ventas"] - df["Costo"]
df_region = df.groupby("Region")[["Ventas", "Ganancias"]].sum()
df_productos = df.groupby(["Region", "Producto"]).sum()

region_mas_ventas = df_region["Ventas"].idxmax()
region_mas_ganancias = df_region["Ganancias"].idxmax()

# Impreciones
print(f"\n{df_productos}")
print(f"\nQué región vende más: {region_mas_ventas}")
print(f"Qué región es más rentable: {region_mas_ganancias}\n")


