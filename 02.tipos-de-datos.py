print("#### DATOS PRIMITIVOS ####")

nombre = 'Juan' #STRINGS
print(f'valor: {nombre}, tipo: {type(nombre)}') 

numero_entero = 17 # numerico ENTERO
print(f'valor: {numero_entero}, tipo: {type(numero_entero)}')

numero_decimal = 2.5 # numerico DECIMAL / FLOTANTE
print(f'valor: {numero_decimal}, tipo: {type(numero_decimal)}')

booleano = True # booleano TRUE / FALSE
print(f'valor: {booleano}, tipo: {type(booleano)}')

complejo = complex(2, 3) # complejo
print(f'valor: {complejo}, tipo: {type(complejo)}')

# ----------------------------------------------------------

print("#### ESTRUCTURAS DE DATOS / DE REFERENCIA ####")

lista = ['manzana', 'banana', 'naranja', 'frutillas'] #LAS LISTAS O ARRAYS SE DEFINEN CON CORCHETES
print(f'valor: {lista}, tipo: {type(lista)}')


tupla = ('manzana', 'naranja', 'frutilla') #LAS TUPLAS SE DEFINEN CON PARENTESIS
print(f'valor: {tupla}, tipo: {type(tupla)}')


set_mio = {'manzana', 'banana', 'naranja'} #SE DEFINEN CON LLAVES COMO LOS DICCIONARIOS PERO LOS VALORES SE ESCRIBEN COMO EN LAS LISTAS
print(f'valor: {set_mio}, tipo: {type(set_mio)}')

diccionario = {
    'nombre' : 'Adrian',
    'edad' : 12,
    'altura' : 1.65 
}

print(f'valor: {diccionario}, tipo: {type(diccionario)}')