print(""" #### OPERADORES DE PERTENENCIA #### """)

texto = 'Hola Info'
palabra = 'info'

resultado = palabra in texto # el 'in' buscará lo que contenga la variable 'palabra' dentro de todo lo que esté en 'texto'
print(resultado)

lista = [10, 40, 20, 55]

numero = 55

resultado = numero not in lista
print(f'Numero in lista: {resultado}')
