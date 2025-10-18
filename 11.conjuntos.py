print(""" #### CONJUNTOS #### """)

# Se definen entre llaves. 
# # No permiten duplicados. 
# # No son ordenados (no tienen indice). 
# # Son mutables (se pueden agregar, modificar y eliminar datos).

colores = {'rojo', 'verde', 'azul'}
print(f'valor: {colores}, tipo: {type(colores)}')

colores.add('amarillo')
print(f'valor: {colores}, tipo: {type(colores)}')

colores.add('magenta')
print(f'valor: {colores}, tipo: {type(colores)}')
