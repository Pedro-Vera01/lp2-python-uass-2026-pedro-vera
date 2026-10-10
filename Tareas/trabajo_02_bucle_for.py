#EJERCICIO 1: Solicite un número entero positivo e imprima todos los números desde 1 hasta dicho número utilizando un ciclo for

""" numero = int(input('Ingrese un número positivo: '))
for i in range(1, numero + 1):
    print(i) """

#EJERCICIO 2: Solicite un número entero positivo N y calcule la suma de todos los números desde 1 hasta N

""" suma = 0
numero = int(input('Ingrese un número positivo: '))

for i in range(1, numero + 1):
    suma += i
print(f'La suma de todos los números hasta {numero} es: ',suma) """

#EJERCICIO 3: Solicite un número entero e imprima su tabla de multiplicar del 1 al 10 utilizando un ciclo for

""" numero = int(input('Ingrese un número positivo: '))

for i in range(1, 11):
    multi = numero * i
    print(f'{numero} x {i} = {multi}')"""

#Solicite una palabra o frase e indique cuántas vocales contiene utilizando un ciclo for

""" palabra = input('Ingrese una frase o palabra: ')
vocales = 'aeiouAEIOU'
contador = 0

for letra in palabra:
    if letra in vocales:
        contador += 1
print(f'La frase/palabra tiene {contador} vocales') """

#Solicite un número entero positivo y genere un triángulo de asteriscos utilizando un ciclo for.

numero = int(input('Ingrese un número positivo: '))
x = '*'
for i in range(1, numero + 1):
    print(x * i)