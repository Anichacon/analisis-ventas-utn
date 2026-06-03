import pandas as pd

ventas = pd.read_excel("datos/dataset.xlsx")

print(ventas)

ventas_totales = (ventas["Cantidad"] * ventas["Precio"]).sum()

print("Ventas totales:", ventas_totales)

producto_mas_vendido = ventas["Producto"].mode()[0]

print("Producto más vendido:", producto_mas_vendido)