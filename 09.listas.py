print(""" #### Listas #### """)

# se definen con corchetes y dentro los valores con su tipo de dato
#           0     1    2    3     4
lista = ['info', 10, 1.75, True, []]
print(f'valor: {lista}, tipo: {type(lista)}')

# Son ordenadas (contienen un indice que parte desde el 0)
# Son mutables: (agregar, modificar y eliminar su contenido)

# --------- Búsqueda de elementos ----------
#          0  1  2  3  4
numeros = [1, 2, 3, 4, 5]

numeros[0]
numeros[-1]
numeros[2]

print(f'primero elemento: {numeros[0]}')
print(f'ultimo elemento: {numeros[-1]}')
print(f'tercer elemento: {numeros[2]}')

# --------- Slicing de listas ----------

print(f'Primeros 3 elementos (1, 2, 3): {numeros[:3]}')
print(f'Ultimos 2 elementos (5, 4): {numeros[:2:-1]}')
print(f'Elementos (2, 3, 4): {numeros[1:4]}')
