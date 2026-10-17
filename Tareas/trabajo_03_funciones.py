#EJERCICIO 1: Estadísticas de una lista
""" def estadisticas(lista):
    maximo = 0
    minimo = 101010
    promedio = sum(lista) / len(lista)
    for numero in lista:
        #Si el valor de la posición actual es mayor al máximo, guarda ese valor
        if numero > maximo:
            maximo = numero

        if numero < minimo:
            minimo = numero
    return maximo, minimo, promedio
#Programa principal
numeros = [10, 20, 30, 40, 50]

mayor, menor, promedio = estadisticas(numeros)

print(f'El número mayor es {mayor}, el menor es {menor} y el promedio es {promedio}') """

#EJERCICIO 2: Buscar un elemento
""" def buscar(lista, valor):
    for nombre in lista:
        if nombre == valor:
            return True
    return False

#Programa principal
alumnos = ["Ana", "Luis", "Carlos", "Pedro","Maria Luisa", "César"]
nombre = input('Ingrese el nombre a buscar: ')
resultado = buscar(alumnos, nombre)
print(resultado) """

#EJERCICIO 3: Eliminar duplicados
""" def eliminar_duplicados(lista):
    return set(lista)

#Programa principal
numeros = [1, 2, 2, 3, 3, 3, 4]
print(eliminar_duplicados(numeros)) """

#EJERCICIO 4: Frecuencia de elementos
""" def contar_frecuencia(lista):
    frecuencia = {}

    for elemento in lista:
        #Consultar si el elemento ya está en el diccionario o no
        if elemento in frecuencia: #El elemento ya fue cargado
            frecuencia[elemento] += 1
        else:
            frecuencia[elemento] = 1
    return frecuencia

#Programa principal
lista = ["a", "b", "a", "c", "a", "b"]
resultado = contar_frecuencia(lista)

print(resultado) """

#EJERCICIO 5: Promedio de notas
def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Return"

#Programa principal
notas = [70, 80, 90, 60]
promedio = calcular_promedio(notas)
print(f'El promedio del alumno es {promedio}')
print(f'El estado del alumno es: {estado(promedio)}')

#EJERCICIO 6: Agenda telefónica
agenda = {
    "Juan": "098111111",
    "Ana": "098222222"
}
#FUNCIONES
def agregar_contacto():
    nombre = input('Ingrese el nombre: ')
    numero = input('Ingrese el número telefónico: ')

    agenda[nombre] = numero

    print('Contacto agregado correctamente...')

def buscar_contacto():
    nombre = input('Ingrese el nombre a buscar: ')
    if nombre in agenda:
        print(f'Teléfono de {nombre}: {agenda[nombre]}')
    else:
        print('Contacto no encontrado...')

def mostrar_contactos():
    if len(agenda) == 0:
        print('La agenda está vacía')
    else:
        print('\n*** Contactos *** ')
        for nombre,telefono in agenda.items():
            print(f'{nombre}: {telefono}')

#Programa principal
while True:
    print('\n === AGENDA TELEFÓNICA ===')
    print('1. Agregar contacto')
    print('2. Buscar contacto')
    print('3. Mostrar contactos')
    print('4. Salir')

    opcion = input('Seleccione una opción:')
    #Llama a la funcion en base a la opcion de menu seleccionado
    if opcion == '1':
        agregar_contacto()
    elif opcion == '2':
        buscar_contacto()
    elif opcion == '3':
        mostrar_contactos()
    elif opcion == '4':
        #Sale del programa
        print('Saliendo del programa...')
    else:
        print('Opción inválida')
