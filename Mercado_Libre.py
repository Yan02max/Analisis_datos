import pandas as pd

data = {
    "Producto": ["Laptop", "Laptop", "Mouse", "Mouse", "Tablet", "Tablet", "Laptop", "Mouse"],
    "Region": ["Norte", "Sur", "Norte", "Sur", "Norte", "Sur", "Sur", "Norte"],
    "Ventas": [1000, 800, 200, 150, 500, 400, 950, 220],
    "Costo": [700, 600, 100, 90, 300, 250, 620, 110]
}

df = pd.DataFrame(data)
df["Ganancias"] = df["Ventas"] - df["Costo"]
df["Margen"] = (df["Ganancias"] / df["Ventas"]) * 100
df_region = df.groupby("Region") [["Ventas","Ganancias"]].sum()
df_mas_ganancias = df_region["Ganancias"].idxmax()
df_margen = df.groupby("Producto") [["Margen"]].mean()
df_mas_margen = df_margen["Margen"].idxmax()

print("Tabla de ventas:\n", df)
print("\n¿Qué región tiene mayor ganancia total?:",df_mas_ganancias)
print(f"¿Qué producto tiene mejor margen promedio?: {df_mas_margen}")


df_dos = pd.DataFrame(data)
df_dos.loc[(df_dos["Region"] == "Sur") & (df_dos["Producto"] == "Laptop"), "Ventas"] *= 1.20
df_dos["Ganancias"] = df_dos["Ventas"] - df_dos["Costo"]
df_dos["Margen"] = (df_dos["Ganancias"] / df_dos["Ventas"]) * 100
df_Margen = df_dos.groupby("Producto") [["Margen"]].mean()
df_mas_Margen = df_Margen["Margen"].idxmax()

print(f"\nTabla de ventas (Laptop) con 20%:\n {df_dos}")
print(f"\n¿Ahora cuál producto tiene mejor margen promedio?: {df_mas_Margen}\n")



