import pandas as pd
import numpy as np

data = {
    "Producto": ["Tablet", "Smartphone", "Audifonos", "Smartwatch", "Camara"],
    "Ventas": [800, 2000, 600, 900, 500],
    "Costo": [500, 1400, 300, 700, 350]
}

df = pd.DataFrame(data)
print(df)

df["Ganancias"] = df["Ventas"] - df["Costo"]


df["Margen"] = (df["Ganancias"] / df["Ventas"]) * 100
df["Participacion %"] = (df["Ventas"] / df["Ventas"].sum()) * 100
df["Clasificacion"] = np.where(df["Margen"] >= 40, "Alta",
                    np.where(df["Margen"] >= 25, "Media", "Baja"))
print("\n",df)
mayor_ganacias = df["Ganancias"].max()
mayor_margen = df["Margen"].max()
producto_riesgo = df.loc[df["Participacion %"].idxmax()]

# Impresiones
print(f"\nProducto con mayor ganancia: {mayor_ganacias}")
print(f"Producto con mayor margen: {mayor_margen}")
print(f"\nProducto que más riesgo genera por concentración:\n{producto_riesgo}\n")

