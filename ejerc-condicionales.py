#Solicite al usuario su edad y si posee documento de identidad (S/N).
# Permitir el ingreso únicamente si:
# Tiene 18 años o más.
# Posee documento de identidad.
# En caso contrario, informe el motivo por el cual no puede ingresar.

# edad = int(input("Ingrese su edad: "))
# ci = input("Posee documento de identidad? s/n: ")

# if edad >= 18 and ci == "s":
#     print("Felicidades, puede ingresar...")
# elif edad < 18 and ci != "s":
#     print("No puede ingresar porque es menor de edad y no posee documento de identidad.")
# elif edad < 18:
#     print("No puede ingresar porque es menor de edad...")
# else:
#     print("No puede ingresar porque no posee documento de identidad")

#Solicite el monto de una compra.
#Aplicar los siguientes descuentos:
#20% si supera Gs. 500.000
#10% si supera Gs. 200.000
#Sin descuento en cualquier otro caso
#Mostrar:
#Monto original
#Descuento aplicado
#Total a pagar

# compra = int(input("Cuál es el monto de su compra?: "))

# if compra > 500000:
#     descuento = int(compra * 0.20)
# elif compra > 200000:
#     descuento = int(compra * 0.10)
# else:
#     descuento = 0
# total = compra - descuento

# print("Monto original: ", compra)
# print("Descuento aplicado: ", descuento)
# print("Total a pagar: ", total)


#Solicite el color del semáforo:
#Verde-Amarillo-Rojo
#Mostrar la acción correspondiente:
#Avanzar
#Reducir velocidad
#Detenerse
#Si el color ingresado no es válido, muestre un mensaje de error.

semaforo = input("Ingrese un color del semáforo: ")

if semaforo == "rojo":
    print("detenerse")
elif semaforo == "amarillo":
    print("reducir velocidad")
elif semaforo == "verde":
    print("avanzar")
else:
    print("no ha ingresado un color del semáforo...") 

#Solicite el porcentaje de batería de un teléfono móvil.
#Mostrar:

#Crítica (0% a 10%)
#Baja (11% a 30%)
#Normal (31% a 80%)
#Alta (81% a 100%)
#Validar que el porcentaje ingresado sea correcto.