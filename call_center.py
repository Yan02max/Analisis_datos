import pandas as pd
import numpy as np

datos = {
    "Nombre": ["Mariana Perez", "Robert Ortiz", "Miguel Luna", "Antonia Cabrera", "Cersar Rojas", "Dariel Baez"],
    "Region": ["Norte", "Este", "Norte", "Este", "Norte", "Este"],
    "Llamadas Total": [45, 59, 30, 60, 25, 57],
    "Perdidas": [23, 10, 15, 27, 5, 30]
    }

df = pd.DataFrame(datos)
df["Confirmadas"] = df["Llamadas Total"] - df["Perdidas"]
df["Margen"] = df["Confirmadas"] / df["Llamadas Total"]
df_region = df.groupby(["Region", "Nombre"]) [["Llamadas Total", "Confirmadas", "Perdidas"]].sum()
df_mas_llamada = df_region["Llamadas Total"].idxmax()
df_mas_confirmada = df_region["Confirmadas"].idxmax()
df_mas_perdidas = df_region["Perdidas"].idxmax()

# Impresiones
print(f"\n{df_region}")
print(f"\nCual fue el empleado de mas llamada en total: {df_mas_llamada}")
print(f"Cual fue el empleado de mas llamada confirmadas: {df_mas_confirmada}")
print(f"Cual fue el empleado de mas llamada perdidas: {df_mas_perdidas}")