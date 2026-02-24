import numpy as np



ventas = np.array([1500, 300, 400, 250])
costos = np.array([1000, 150, 250, 200])

Ganancias_productos = ventas - costos
margen_productos = (Ganancias_productos / ventas) * 100

print(f"El producto con mayor ganancia es el numero {np.argmax(Ganancias_productos) +1}")
print(f"El producto con mayor margen es: {np.argmax(margen_productos) +1}")

