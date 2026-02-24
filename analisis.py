import pandas as pd 
import numpy as np 

data = {
    "Producto": ["Laptop", "Mouse", "Teclado", "Monitor"],
    "Ventas": [1500, 300, 400, 250],
    "Costo": [1000, 150, 250, 200]
}
# Imprecion dataframe original
df = pd.DataFrame(data)
print(f"{df}\n")

# Formulas Matematicas De Negocios
ventas = df.columns[1]
df["Ganancias"] = df["Ventas"] - df["Costo"]
df["Margen"] = (df["Ganancias"] / df["Ventas"]) * 100
mayor_ganancia = df["Ganancias"].max()
mayor_margen = df["Margen"].max()
df["Participacion %"] = (df["Ventas"] / df["Ventas"].sum()) * 100
df["Clasificacion"] = np.where(df["Margen"] >= 45, "Alta Rentabilidad", 
                    np.where(df["Margen"] >= 30, "Media Rentabilidad", 
                    "Baja Rentabilidad") ) 
# Impreciones 
print(f"{df['Ventas']}\n")
print(f"{df}")
print(f"\nMayor Ganancias: {mayor_ganancia}")
print(f"Mayor Margen: {mayor_margen}\n")

