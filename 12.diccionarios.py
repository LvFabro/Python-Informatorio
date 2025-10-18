print(""" #### DICCIONARIOS #### """)

# Los diccionarios se definen con llaves y dentro contienen 2 secciones CLAVES y VALORES
# Por ejemplo, la Clave seria 'nombre' y el valor de esa clave sería 'Pablo'

estudiante = {
    'nombre' : 'Pablo',
    'edad' : 21,
    'materias' : {
        'Python' : {
            'clase 1' : 'fundamentos',
            'clase 2' : 'Instalacion de python',
            'clase 3' : 'variables y tipos de datos'
        }
    }
}
print(f'El nombre del estudiantes es: {estudiante["nombre"]}')
print(f'La edad del estudiantes es: {estudiante["edad"]}')
print(f'De sus materias posee: {estudiante["materias"]}')
print(f'Su primera clase daran: {estudiante["materias"]["Python"]["clase 1"]}')

""" ### MÉTODOS #### """

print(f'Claves del diccionario: {estudiante.keys()}')
print(f'Claves del diccionario en forma de lista: {list(estudiante.keys())[2]}')