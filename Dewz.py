import pandas as pd
import numpy as np

data = {
    "Cliente": ["A", "A", "B", "C", "D", "D", "E", "F"],
    "Producto": ["Laptop", "Laptop", "Mouse", "Mouse", "Tablet", "Tablet", "Laptop", "Mouse"],
    "Region": ["Norte", "Sur", "Norte", "Sur", "Norte", "Sur", "Sur", "Norte"],
    "Ventas": [1000, 800, 200, 150, 500, 400, 950, 220],
    "Costo": [700, 600, 100, 90, 300, 250, 620, 110]
}

# Frase 1 
df = pd.DataFrame(data)
df["Ganancias"] = df["Ventas"] - df["Costo"]
df["Margen"] = (df["Ganancias"] / df["Ventas"])

resumen = df.groupby(["Producto", "Region"]).agg({"Ventas": "sum", 
                                                  "Ganancias": "sum", 
                                                  "Margen": "mean"})
mas_rentable = resumen["Ganancias"].idxmax()
menos_margen = resumen["Margen"].idxmin()
resumen = resumen.sort_values(by="Ganancias", ascending=False)
condiciones = [resumen["Margen"] > 0.30,resumen["Margen"] < 0.20,]
resultados = ["Alta Rentabilidad", "Baja Rentabilidad"]
resumen["Clasificacion"] = np.select(condiciones, resultados, default="Rentabilidad Media")
ventas_clientes = df.groupby("Cliente").agg({"Ganancias": "sum", 
                                             "Ventas": "count", 
})
ventas_clientes["CLV_simple"] = ventas_clientes["Ganancias"] 
q1 = ventas_clientes["CLV_simple"].quantile(0.33)
q2 = ventas_clientes["CLV_simple"].quantile(0.66)
condiciones = [
    ventas_clientes["CLV_simple"] <= q1,
    (ventas_clientes["CLV_simple"] > q1) & (ventas_clientes["CLV_simple"] <= q2),
    ventas_clientes["CLV_simple"] > q2
]
valores = ["Bajo Valor", "Medio Valor", "Alto Valor"]
ventas_clientes["Segmento"] = np.select(condiciones, valores)


print(ventas_clientes)

