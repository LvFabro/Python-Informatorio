""" #### BUCLES #### """

# Bucle While -> PERMITE EJECUTAR UNA PORCION DE CODIGIO MIENTRAS LA CONDICION ESPECIFICADA RESULTE VERDADERA

""" i = 0
numero = 0

while i < 5:
    i += 1
    numero += 1
    print(numero) """
    
# UNA VEZ QUE i VALE MÁS QUE 5 EL CICLO SE TERMINA -> Por eso es necesario establecer una variable que actue como limite para que el bucle tenga un fin.

# Bucle con detencion impuesta por el usuario:

while True:
    print('Hola Info')
    respuesta = input('¿Desea Continuar? (S/N) o x: ')
    respuesta.lower()
    
    if respuesta == 'no':
        print('novemos')
        break
    
    elif respuesta == 'x': 
        print('Hola X')
        continue