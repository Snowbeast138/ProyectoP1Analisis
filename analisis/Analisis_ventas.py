import csv 
import pandas as pd


ventas = pd.DataFrame()

with open('./datos/ventas.csv', mode='r') as file:
        reader = csv.reader(file)
        columns = next(reader)  
        ventas = pd.DataFrame(reader, columns=columns)

ventas["precio_unitario"] = pd.to_numeric(ventas["precio_unitario"])
ventas["cantidad"] = pd.to_numeric(ventas["cantidad"])
ventas["importe"] = ventas["precio_unitario"] * ventas["cantidad"]

venta_mas_importe = ventas.loc[ventas["importe"].idxmax()]
print("Venta mayor importe:\n",venta_mas_importe)
print("--------------------------------")
venta_menor_importe = ventas.loc[ventas["importe"].idxmin()]
print("Venta menor importe:\n",venta_menor_importe)
print("--------------------------------")
venta_mas_cantidad = ventas.loc[ventas["cantidad"].idxmax()]
print("Venta con mayor cantidad:\n",venta_mas_cantidad)
print("--------------------------------")
venta_menor_cantidad = ventas.loc[ventas["cantidad"].idxmin()]
print("Venta con menor cantidad:\n",venta_menor_cantidad)
print("--------------------------------")
promedio_importe = ventas["importe"].mean()
print("Promedio de importe:", promedio_importe)

print(ventas.to_string())