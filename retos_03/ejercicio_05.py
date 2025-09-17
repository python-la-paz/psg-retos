## 5. 

productos=input ("4 Productos (separados por comas): ").strip().split(",")
#--
precios=input ("4 Precios (separados por comas): ").strip().split(",")
#--
precios_float=[]
precios_float.append(float(precios[0]))
precios_float.append(float(precios[1]))
precios_float.append(float(precios[2]))
precios_float.append(float(precios[3]))
#--
precios_ordenados=sorted(precios_float)
productos_ordenados=[]
productos_ordenados.append(productos[precios_float.index(precios_ordenados[0])])
productos_ordenados.append(productos[precios_float.index(precios_ordenados[1])])
productos_ordenados.append(productos[precios_float.index(precios_ordenados[2])])
productos_ordenados.append(productos[precios_float.index(precios_ordenados[3])])
#--
total_de_compra=sum (precios_float)
producto_mas_caro=productos[precios_float.index(max(precios_float))]
producto_mas_barato=productos[precios_float.index(min(precios_float))]
#--
print(f"Total de la compra: {total_de_compra}\nProducto más caro: {producto_mas_caro}\nProducto más barato: {producto_mas_barato}\nProductos ordenados por precio: {", ".join(productos_ordenados)}")