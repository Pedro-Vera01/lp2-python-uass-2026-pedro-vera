#Manejo de archivos en Python
#Manejo normal - Apertura y cierre manual
archivo = open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8")
contenido = archivo.read()
print(archivo.read())
archivo.close() #cierra el archivo

#Si no se cierra, se pueden perder cambios o quedar el archivo bloqueado para otros programas

#RECOMENDADO:
with open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8") as archivo:
    contenido = archivo.read()
    print(contenido)  #Devuelve todo el contenido como un único string
    #Se cierra solo, incluso si hay error, no necesita close()

with open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8") as archivo:
    contenido = archivo.readline()
    print(contenido)    #Devuelve una sola linea en cada llamada
    contenido = archivo.readline()
    print(contenido)    #Devuelve la siguiente línea

with open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8") as archivo:
    contenido = archivo.readlines()
    print(contenido)


#Iterar el archivo con FOR lee línea por línea, igual que readline(), pero de forma más simple
with open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8") as archivo:
    for linea in archivo:
        print(linea)

#¿Cómo resolvemos los saltos de líneas adicionales?
#OPCION 1:
with open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8") as archivo:
    for linea in archivo:
        print(linea.strip())    #strip() quita el salto de línea

#OPCION 2: MODIFICAR LA PROPIEDAD END DE LA FUNCION PRINT
with open("C:/Users/isaia/Isaias.py/datos.txt.txt","r", encoding = "utf-8") as archivo:
    for linea in archivo:
        print(linea, end="")

#ESCRITURA EN ARCHIVOS
with open("C:/Users/isaia/Isaias.py/notas.txt.txt","a", encoding = "utf-8") as archivo:
    archivo.write('Reporte de notas\n')
    for alumno in range(5):
        nombre = input("Ingrese el nombre del alumno: ")
        nota = int(input(f'Ingrese la nota para {nombre}: '))
        archivo.write(f'{nombre}: {nota}\n')