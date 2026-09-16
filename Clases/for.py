#Iterar mediante ciclos FOR
#Iterar sobre una lista

#lenguajes = ['Python', 'Java','C++','JavaScript','PHP']
'''for (elemento) in lenguajes:
    print(elemento)'''

#Instrucciones para modiicar el flujo de un ciclo FOR
#Que el ciclo se rompa con la primera iteración con BREAK

#for (elemento) in lenguajes:
#        break
#print('El ciclo se rompió')

#romper el ciclo actual si el elemento es igual a C++

# for (elemento) in lenguajes:
#     if elemento == 'C++':
#       break
#     print(elemento)


# for (elemento) in lenguajes:
#     if elemento == 'PHP':
#         print(elemento)
#         break
#     print(elemento)


#Pasar al siguiente elemento de la lista cuando se cumpla una condición
#usando continue

#lenguajes = ['Python', 'Java','C++','JavaScript','PHP']

# for elemento in lenguajes:
#     if elemento == 'C++' or elemento == 'PHP':
#         continue
#     print(elemento)

#Iterar sobre una cadena de caracteres
# for letra in 'otorrinolaringologia':
#     print(letra)

#Iterar sobre numeros consecutivos 
#for numero in  range (1,51):
#    print(numero)

#cambiar el valor de aumento del rango (por defecto es 1)
#for numero in range (2,201,2):
#     print(numero)

#disminuir el valor del aumento del rango (por defecto es 1)
#for numero in range (100,0,-1):
#    print(numero)

#Otra forma
# for numero in reversed(range (1, 100)):
#     print(numero)

#Otra forma de iterar sobre listas

# lenguajes = ['Python', 'Java','C++','JavaScript','PHP']
# for index in range (len(lenguajes)):
#     print(f'El lenguaje en la posición {index} es {lenguajes[index]}')

#Iterar sobre diccionarios
#lenguajes = {'nombre': 'Python',
#             'creador': 'Guido Van Rossum'
#             }

#Imprimir las llaves del diccionarios   ES POR DEFECTO
# for elemento in lenguajes:
#     print(elemento)
#for elemento in lenguajes.keys():
#   print(elemento)

#Imprimir los valores de los diccionarios
# for elemento in lenguajes.values():
#     print(elemento)

#Para imprimir todo {llave:valor}
# for elemento in lenguajes.items():
#     print(elemento)

# for llave, valor in lenguajes.items():
#     print(f'llave: {llave}, Valor: {valor}')


#Algunos ejemplos prácticos resueltos con ciclos FOR
#EJEMPLO 1: sumar todos los números de una lista
# numeros = [1,2,3,4,5]
# suma = 0
# for numero in numeros:
#     suma += numero
# print(f'La suma de los números es: {suma}')

#EJEMPLO 2: Encontrar el numero más grande de una lista
# numeros = [10,20,50,40,35]
# maximo = numeros[0]

# for numero in numeros:
#     if numero > maximo:
#         maximo = numero
# print(f'El valor más grande es: {maximo}')

# #EJEMPLO 3: Contar las vocales en una cadena de caracteres
# cadena = 'Hola Mundo!!'
# vocales = 'aeiouAEIOU'
# contador = 0
# for letra in cadena:
#     if letra in vocales:
#         contador += 1
# print(f'El número de vocales en la cadena es: {contador} ')

#EJEMPLO 4: imprimir una tabla de multiplicar

# numero = int(input('Ingrese un número para ver su tabla de multiplicar: '))
# for i in range(1,11):
#      resultado = numero * i
#      print(f'{numero} x {i} = {resultado}')

#EJEMPLO 5: generar una lista de los primeros 10 numeros cuadrados
# cuadrados = []
# for i in range (1,11):
#     cuadrados.append(i ** 2)
# print(f'Los primeros 10 numeros cuadrados son: {cuadrados}')

#EJEMPLO 6: Invertir una cadena
# cadena = 'Python'
# invertida = ''
# for letra in cadena:
#     invertida = letra + invertida
# print(f'La cadena invertida es_ {invertida}')

#EJEMPLO 7: Filtrar números pares de una lista
# numeros = [1,2,3,4,5,6,7,8,9,10]
# pares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
# print(f'Los números pares de la lista son: {pares}')


# monto = float(input("Ingrese el monto de la compra (Gs.): "))

# if monto > 500000:
#     descuento = monto * 0.20
# elif monto > 200000:
#     descuento = monto * 0.10
# else:
#     descuento = 0

# total = monto - descuento

# print(f"Monto original: Gs. {monto}")
# print(f"Descuento aplicado: Gs. {descuento}")
# print(f"Total a pagar: Gs. {total}")
