#EJERCICIO 1
with open("C:/Users/isaia/Isaias.py/productos.txt","w", encoding = "utf-8") as archivo:
    for producto in range(5): 
        nombre = input("Ingrese el nombre del producto: ")
        precio = input(f'Ingrese el precio de {nombre}: ')
        archivo.write(f'{nombre} - {precio}\n') 

#EJERCICIO 2
with open("C:/Users/isaia/Isaias.py/productos.txt","r", encoding = "utf-8") as archivo:
    for linea in archivo:       
        print(linea.strip())

#EJERCICIO 3:
with open("C:/Users/isaia/Isaias.py/registro.txt","a", encoding = "utf-8") as archivo:
    nombre = input("Ingrese el nombre: ")
    edad = input("Ingrese la edad: ")
    archivo.write(f'{nombre} - {edad}\n')

#EJERCICIO 4;
suma = 0
cantidad = 0
with open("C:/Users/isaia/Isaias.py/numeros.txt","r", encoding = "utf-8") as archivo:
    for linea in archivo:
        suma = suma + int(linea)
        cantidad = cantidad + 1

promedio = suma / cantidad
print(f'El promedio es {promedio}')

with open("C:/Users/isaia/Isaias.py/resultado.txt","w", encoding = "utf-8") as archivo:
    archivo.write(f'Promedio: {promedio}\n')

#EJERCICIO 5:
with open("C:/Users/isaia/Isaias.py/origen.txt","r", encoding = "utf-8") as origen:           
    with open("C:/Users/isaia/Isaias.py/destino.txt","w", encoding = "utf-8") as destino:     
        for linea in origen:
            destino.write(linea) 
