print(""" #### OPERADORES LOGICOS #### """)

a = 10
b = 3
c = 20

#           True   y   True
resultado = a > b and a < c
print(f'a > b and a < c: {resultado}')

#           True   o   False
resultado = a > b or a < 5
print(f'a > b or a < 5: {resultado}')

resultado = not a < 10
print(f'not a < 10: {resultado}')

esta_autenticado = False
if not esta_autenticado:
    print('Por favor, inicia sesion')