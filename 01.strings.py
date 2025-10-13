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

#--------------------------------------------

texto = 'cinco'

print(len(texto)) # el MÉTODO .len() cuenta los caracteres de la variable
        #    12345678910 
texto_dos = 'Hola Info 🚀' # A esta variable le aplicaremos un 'Slicing' que se hace utilizando Corchetes

subcadena = texto_dos[5:10] #se coloca el índice antes de donde se quiere, y luego uno después de hasta donde se quiere cortar.

print(subcadena)

# Tambien podemos agregar un tercer parametro en los corchetes

cadena_invertida = print(texto_dos[:: -1]) #  [valor de inicio : valor final : como quiero que avance, de uno en uno o de dos en dos, etc]

# Si coloco un -1 invierte todo el texto

cadena_mayuscula = texto_dos.upper() #Este método transforma todo el string en mayusculas
print(cadena_mayuscula)

cadena_minuscula = texto_dos.lower() #Este método transforma todo el string en minusculas
print(cadena_minuscula)

nombre_dos = 'diego oscar'
cadena_capitalizada = nombre_dos.capitalize() # Este método transforma la primer letra de la palabra en mayúscula
print(cadena_capitalizada)

cadena_tabulada = '\tHola\tInfo' # el \t tabula en esa parte del string
print(cadena_tabulada)