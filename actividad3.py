"""
Arranco la variable del nombre de la materia con cadenas vacías al
inicio del algoritmo para que el programa no la tome como indefinida
"""
nombre_asig = ""

"""
El programa solamente pide el nombre del/la estudiante y
define la cantidad de asignaturas, en este caso 5
"""
nombre = input("Ingresá tu nombre completo: ")
asignaturas = 5

# Inicializo el contador en 1 y la suma en 0
cont = 1
suma = 0
while cont <= asignaturas:
    # Dentro del bucle se solicita el nombre de la materia y su respectiva nota
    nombre_asig = input(f'Ingresá el nombre de la {cont}° asignatura: ')
    nota = float(input(f'¿Qué calificación obtuviste en {str(nombre_asig)}?: '))
    """
    A cada nota que ingresa por teclado, se guardará en la suma 
    para luego promediar las 5 materias totales y al contador se
    le suma un punto por vuelta hasta llegar al límite asignado inicialmente
    """
    suma += nota
    cont += 1

""" 
Se calcula el promedio de la suma de las notas obtenidas en el 5° semestre 
por la X cantidad de notas y luego muestra el promedio al estudiante
"""
promedio = suma / asignaturas
print(f'Hola {nombre}, en el 5° semestre tenés un promedio de {promedio}')

# Mi nota: Nombre: Fernán Pietrantuono. Promedio: 4.26
