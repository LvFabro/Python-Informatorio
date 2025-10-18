print(""" #### TUPLAS #### """)

# Se definen con parentesis. Son ordenadas, porque poseen indexación (tienen indices que parten desde el 0)
# Son inmutables (a diferencia de las Listas, estas no se pueden agregar, modificar ni eliminar valores)

#            0          1         2
tupla = ('manzana', 'banana', 'naranja')
print(f'valor: {tupla}, tipo: {type(tupla)}')

print(f'Primer elemento: {tupla[0]}')
print(f'Ultimo elemento: {tupla[-1]}')
print(f'Elemento "Banana": {tupla[1]}')

print(f'longitud de la tupla: {len(tupla)}')

print(f'Veces que aparece "frutillas" en la tupla: {tupla.count("frutillas")}')
print(f'Veces que aparece "manzana" en la tupla: {tupla.count("manzana")}')

print(f'Indice de "naranja": {tupla.index("naranja")}')
