# Los strings o cadena de caracteres se colocan utilizando las comillas ' ' o " "

nombre = 'Pepe'

apellido = 'Gonzales'

mensaje = f'Hola {nombre}, {apellido}' 
#Para 'formatear' una variable y que nos permita insertar variables dentro de los strings se utiliza una 'f' antes de abrir comillas.

print(mensaje)

print(f'hola {nombre}, {apellido} :D')

# Podemos hacer una suma

num1 = 10

num2 = 5

print(f'La suma de {num1} + {num2} = {num1 + num2}')

# === Otra forma de hacerlo ===

num3 = 14

num4 = 6

resultado = num3 + num4

print(f'La suma de 14 + 6 = {resultado}')