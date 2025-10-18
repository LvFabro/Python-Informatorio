""" #### FUNCIONES #### """
""" la función (redondeando) es un bloque de codigo 
que en vez de escribirlo muchas veces, lo definimos y vamos llamando, 
mas practico y ordenado para leer todo el codigo general.. """

# ------- Ejemplo sencillo de una función --------

""" def saludo(nombre):
    print(f'hola {nombre}')
    return 
    
saludo('Fabri') """

# -------------------------------------------------

""" notas = [10, 8, 4, 7]

total_notas = 0

for nota in notas:
    total_notas += nota

print( '========= Calculo de notas ==========' )
    
print(f'Total de notas adquiridas: {len(notas)}')    
print(f'Suma total de todas las notas: {total_notas}')  
promedio = total_notas / len(notas)
print(f'Promedio total de: {promedio} puntos' )

print( '========= Calculo de notas ==========' ) """

# -------------------------------------------------

# Ejemplo practico de una funcion junto a lo que retorna y a su llamado.

""" def promedio(items):
    total = 0
    
    for item in items:
        total += item
        
    return total / len(items)

print(f'Promedio total de notas: {promedio([10, 8, 4, 7])}') """

# -----------------------------------------------

#   > parametros <
def suma(a, b):
    resultado = a + b  
    return resultado

print(f'La suma de los numeros 10 y 5 es: {suma(10, 5)}')
                                        # > argumentos <