# EJERCICIO 1: Control de acceso

edad = int(input("Ingrese su edad: "))
documento = input("¿Posee documento de identidad? (S/N): ").strip().upper()

mayor_edad = edad >= 18
tiene_documento = documento == "S"

if mayor_edad and tiene_documento:
    print("Adelanteeee")
elif not mayor_edad and not tiene_documento:
    print("Acceso denegado: es menor de edad y no posee documento de identidad.")
elif not mayor_edad:
    print("Acceso denegado: es menor de edad.")
else:
    print("Acceso denegado: no posee documento de identidad.")

# EJERCICIO 2: Descuento en una tienda
monto = float(input("Ingrese el monto de la compra (Gs.): "))

if monto > 500000:
    descuento = monto * 0.20
elif monto > 200000:
    descuento = monto * 0.10
else:
    descuento = 0

total = monto - descuento

print(f"Monto original: Gs. {monto}")
print(f"Descuento aplicado: Gs. {descuento}")
print(f"Total a pagar: Gs. {total}")


# EJERCICIO 3: Semáforo inteligente
color = input("Ingrese el color del semáforo (Verde/Amarillo/Rojo): ").strip().lower()

if color == "verde":
    print("Acción: Avanzar")
elif color == "amarillo":
    print("Acción: Reducir velocidad")
elif color == "rojo":
    print("Acción: Detenerse")
else:
    print("Color no válido.")


# EJERCICIO 4: Nivel de batería
bateria = int(input("Ingrese el porcentaje de batería (0-100): "))

if bateria < 0 or bateria > 100:
    print("Error: porcentaje no válido.")
elif bateria <= 10:
    print("Nivel de batería: Crítica")
elif bateria <= 30:
    print("Nivel de batería: Baja")
elif bateria <= 80:
    print("Nivel de batería: Normal")
else:
    print("Nivel de batería: Alta")


#EJERCICIO 5: Evaluación climática
temperatura = float(input("Ingrese la temperatura actual: "))

if temperatura < 10:
    print("Evaluación: Mucho frío")
elif temperatura <= 24:
    print("Evaluación: Templado")
elif temperatura <= 34:
    print("Evaluación: Caluroso")
else:
    print("Evaluación: Muy caluroso")
