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
""" def calcular_promedio(notas):
    promedio = sum(notas) / len(notas)
    return promedio

def estado(promedio):
    if promedio >= 60:
        return "Aprobado"
    else:
        return "Reprobado"

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
        break
    else:
        print('Opción inválida') """

#EJERCICIO 7: Producto más caro
""" productos = [
    ("Teclado", 150000),
    ("Mouse", 80000),
    ("Monitor", 1200000) ]

def producto_mas_caro(productos):
    nombre_caro = ""
    precio_caro = 0

    for nombre, precio in productos:
        if precio > precio_caro:
            nombre_caro = nombre
            precio_caro = precio
    return nombre_caro, precio_caro

#Programa principal
nombre, precio = producto_mas_caro(productos)

print(f'Producto: {nombre}')
print(f'Precio: {precio}')
 """
#EJERCICIO 8: Inventario de productos
""" inventario = {
    "Teclado": 10,
    "Mouse": 5,
    "Monitor": 2
}
#FUNCIONES
def agregar_stock():
    producto = input('Ingrese el producto: ')
    cantidad = int(input('Ingrese la cantidad a agregar: '))
    inventario[producto] += cantidad
    print(f'Stock actualizado: {producto} = {inventario[producto]}')

def vender_producto():
    producto = input('Ingrese el producto a vender: ')
    cantidad = int(input('Ingrese la cantidad a vender: '))

    if cantidad > inventario[producto]:
        print(f'Stock insuficiente. Disponible: {inventario[producto]}')
    else:
        inventario[producto] -= cantidad
        print(f'Venta registrada. Stock restante de {producto}: {inventario[producto]}')

def consultar_stock():
    producto = input('Ingrese el producto a consultar: ')

    if producto in inventario:
        print(f'Stock de {producto}: {inventario[producto]}')
    else:
        print('Producto no encontrado...')

#Programa principal
while True:
    print('\n === INVENTARIO DE PRODUCTOS ===')
    print('1- Agregar stock')
    print('2- Vender producto')
    print('3- Consultar stock')
    print('4- Salir')

    opcion = input('Seleccione una opción: ')

    if opcion == '1':
        agregar_stock()
    elif opcion == '2':
        vender_producto()
    elif opcion == '3':
        consultar_stock()
    elif opcion == '4':
        print('Muchas gracias por su compra!!')
        print('Saliendo del programa...')
        break
    else:
        print('Opción inválida')
 """
#EJERCICIO 9: Ranking de alumnos
alumnos = [
    ("Juan", 85),
    ("Ana", 95),
    ("Pedro", 70)
]
#FUNCIONES
def mejor_alumno(alumnos):
    nombre_mejor = ""
    nota_mejor = 0

    for nombre, nota in alumnos:
        if nota > nota_mejor:
            nombre_mejor = nombre
            nota_mejor = nota
    return nombre_mejor, nota_mejor

def peor_alumno(alumnos):
    nombre_peor, nota_peor = alumnos[0]

    for nombre, nota in alumnos:
        if nota < nota_peor:
            nombre_peor = nombre
            nota_peor = nota
    return nombre_peor, nota_peor

def promedio_general(alumnos):
    total = 0

    for nombre, nota in alumnos:
        total += nota
    return total / len(alumnos)

#Programa principal
nombre, nota = mejor_alumno(alumnos)
print(f'Mejor alumno: {nombre} ({nota})')

nombre, nota = peor_alumno(alumnos)
print(f'Peor alumno: {nombre} ({nota})')

print(f'Promedio general: {promedio_general(alumnos)}')
