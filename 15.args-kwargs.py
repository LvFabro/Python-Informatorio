""" #### ARGS Y KWARS #### """


# *ARGS : Permiten pasar a una función un número indeterminado/dinámico de argumentos de TIPO Posicionales
""" #   > parametros <
def suma(*args):
    print(args)
    resultado = sum(args)
    return resultado


print(f'La suma de los numeros 10 y 5 es: {suma(5, 5, 5)}')
                                        # > argumentos < """

# **KWARGS : Permite pasar a una funcion un numero indeterminado/dinamico de argumentos de TIPO Nombrados (van a tener una CLAVE y un VALOR)

""" def ver_persona(**kwargs):
    print(kwargs)
    print(type(kwargs))
"""

""" def ver_persona(**kwargs):
    
    for key, value in kwargs.items():
        print(f'Clave: {key} | Valor: {value}')
        
ver_persona(nombre = 'Pablo', edad = 28, altura = 1.75) """

