#EJERCICIO 1: Solicite un número entero positivo e imprima todos los números desde 1
#hasta dicho número utilizando un ciclo while

numero = int(input('Ingrese un número: '))
i = 1
while i <= numero:
    print(i)
    i += 1

#EJERCICIO 2 Solicite números al usuario y acumule la suma.
#El programa debe finalizar cuando el usuario ingrese el valor 0.
#Al finalizar, muestre la suma total

numero = int(input('Ingrese un número: '))
contador = 0

while numero != 0:
    contador = numero + contador
    numero = int(input('Ingrese otro número (0 para terminar): '))
    
print('La suma total de los números es: ' ,contador)

#EJERCICIO 3: Solicite una contraseña al usuario.
# Mientras la contraseña ingresada sea diferente de: python123
#debe volver a solicitarla.
#Cuando la contraseña sea correcta, muestre: Acceso concedido

contraseña = 'python123'
usuario = input('Ingrese su contraseña: ')

while usuario != contraseña:
    print('Contraseña incorrecta...')
    usuario = input('Vuelva a ingresar su contraseña:')
print('Acceso concedido')

#EJERCICIO 4: Solicite la cantidad de estudiantes presentes en cada clase.
#El ingreso finalizará cuando el usuario introduzca el valor -1.
#Al finalizar, mostrar:
#Total de asistencias registradas.
#Cantidad de clases ingresadas.
#Promedio de asistencia

asistencia = int(input('Ingrese la cantidad de estudiantes presentes: '))
suma_asist = 0
cant_clases = 0

while asistencia != -1:
    suma_asist += asistencia
    cant_clases += 1
    asistencia = int(input('Ingrese la cantidad de estudiantes presentes en otra clase (-1 para terminar): '))

promedio = suma_asist / cant_clases
print(f'Total de asistencias registradas: {suma_asist}')
print(f'Cantidad de clases ingresadas: {cant_clases}')
print(f'Promedio de asistencia: {promedio}')

#EJERCICIO 5: Caja registradora
# Solicite el precio de los productos comprados.
# El ingreso finalizará cuando el usuario ingrese 0.
# Al finalizar mostrar:
# Cantidad de productos.
# Monto total de la compra.

precio = float(input('Ingrese el precio del producto: '))
cantidad = 0
monto_total = 0

while precio != 0:
    cantidad += 1
    monto_total += precio
    precio = float(input('Ingrese el precio de otro producto (0 para terminar): '))

print(f'Cantidad de productos: {cantidad}')
print(f'Monto total de la compra: {monto_total}')
