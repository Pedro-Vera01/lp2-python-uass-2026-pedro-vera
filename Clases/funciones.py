#Definición de una función
""" def SALUDAR(nombre):
    print('Hola Mundo! ' + nombre)

SALUDAR("Pedro")
 """
#Ambito de las variables
#1 Locales: definidas dentro de la función, su ámbito es solo dentro de la misma
""" def MiFuncion():
    print('Mi primera función')
    nombre = 'Pedro' #Variable local
    print(nombre)

MiFuncion()
 """
#2 Global: A diferencia de las locales, pueden usarse en cualquier parte del código
""" apellido = 'Vera'
def MiFuncion():
    print('Mi primera función')
    nombre = 'Pedro' #Variable local
    print(nombre,apellido)
MiFuncion() """
#Si yo quiero imprimir la variable nombre, no se va a poder porque se declara dentro del def

#Parámetros o argumentos de una función
#Creamos una función para calcular el parámetro de un cuadrado (lado * 4)

""" def perimetro_cuadrado(lado, unidades):
    perimetro = lado * 4
    print(f'El perimetro es {perimetro} {unidades}') """
#A. Forma de indicar los parámetros de una función, {POR ORDEN}
#perimetro_cuadrado(25,'metros')

#B. Forma de indicar los parámetros de una función, {VALOR NOMINAL}
#perimetro_cuadrado(lado = 25, unidades = 'metros')

#C. Mezclando ambas formas
#perimetro_cuadrado(25, unidades = 'metros')


#Cuando necesitamos usar el resultado de nuestras funciones en el proceso principal, debemos
#usar la instrucción {RETURN} 

""" def perimetro_cuadrado(lado):
    perimetro = lado * 4
    return perimetro

def area_cuadrado(lado):
    area = lado * lado
    return area """

#Podemos almacenar en una variable el valor retornado
""" perimetro = perimetro_cuadrado(5)
area = area_cuadrado(5)
print(f'Area: {area}, Perimetro: {perimetro} ') """

#Tambien podemos retornar más de un valor en la función
""" def calcular_cuadrado(lado):
    perimetro = lado * 4
    area = lado * lado
    return perimetro, area """
#perimetro, area = calcular_cuadrado(5)
#print(f'Area: {area}, Perimetro: {perimetro} ')


#Podemos almacenar un valor en una sola variable, el resultado será una tupla
#resultado = calcular_cuadrado(5)
#print(resultado)

#Podemos almacenar un valor en una sola variable, el resultado será una tupla
""" resultado = calcular_cuadrado(5)
print(resultado) """

#Cuando una funcion no retorna ningun valor y tratamos de asignar el resultado de la funcion
#a una variable, esta variable va a recibir como resultado el valor 'None', para probarlo
#quitamos el retorno de la funcion perimetro_cuadrado

""" def perimetro_cuadrado(lado):
    perimetro = lado * 4
def area_cuadrado(lado):
    area = lado * lado
    return area 
perimetro = perimetro_cuadrado(5)
area = area_cuadrado(5)
print(f'Area: {area}, Perimetro: {perimetro} ')
 """

#Funciones lambda
""" suma = lambda numero1, numero2, : numero1 + numero2 #funciones lambda
print(suma(2,5)) """

#Documentacion de las funciones
#1. Documentación corta: con tres comillas simples
def perimetro_cuadrado(lado):
    '''Se encarga de calcular el perímetro de un cuadrado...'''
    perimetro = lado * 4
    return perimetro

#2. Documentación larga
def perimetro_cuadrado(lado):
    '''Se encarga de calcular el perímetro de un cuadrado
    Esta función recibe el valor de un lado del cuadrado a partir de éste calcula y 
    retorna su perímetro...
    Args:
        lado (int): medida del lado del cuadrado
    
    Returns: 
        perimetro (int): retorna el perímetro del cuadrado
        
    '''
    perimetro = lado * 4
    return perimetro
