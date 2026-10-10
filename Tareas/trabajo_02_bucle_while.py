#EJERCICIO 1: Solicite un número entero positivo e imprima todos los números desde 1
#hasta dicho número utilizando un ciclo while

""" numero = int(input('Ingrese un número: '))
i = 1
while i <= numero:
    print(i)
    i += 1 """

#EJERCICIO 2 Solicite números al usuario y acumule la suma.
#El programa debe finalizar cuando el usuario ingrese el valor 0.
#Al finalizar, muestre la suma total

""" numero = int(input('Ingrese un número: '))
contador = 0

while numero != 0:
    contador = numero + contador
    numero = int(input('Ingrese otro número (0 para terminar): '))
print('La suma total de los números es: ' ,contador) """

#EJERCICIO 3: Solicite una contraseña al usuario.
# Mientras la contraseña ingresada sea diferente de: python123
#debe volver a solicitarla.
#Cuando la contraseña sea correcta, muestre: Acceso concedido

""" contraseña = 'python123'
usuario = input('Ingrese su contraseña: ')

while usuario != contraseña:
    print('Contraseña incorrecta...')
    usuario = input('Vuelva a ingresar su contraseña:')
print('Acceso concedido') """

#EJERCICIO 4: Solicite la cantidad de estudiantes presentes en cada clase.
#El ingreso finalizará cuando el usuario introduzca el valor -1.
#Al finalizar, mostrar:
#Total de asistencias registradas.
#Cantidad de clases ingresadas.
#Promedio de asistencia

