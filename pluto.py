"""Proyecto Pluto.

Herramienta de organización de finanzas personales.
El programa permite registrar un ingreso y un gasto, y después elegir
qué información quiere ver el usuario.
"""
dinero_total = 0

def registrar_ingreso():
    global dinero_total

    ingreso = float(input("Dinero que se recibió: $"))
    if validar_cantidad(ingreso):
        origen = input("Fuente de la que se obtuvo ese dinero: ")
        dinero_total += ingreso
        return ingreso, origen
    else:
        print("La cantidad debe ser mayor a cero, se tomará como $0.")
        return 0, 0


def registrar_gasto():
    global dinero_total

    gasto = float(input("Dinero que se gastó: $"))
    if validar_cantidad(gasto):
        categoria = input("Categoría (comida, transporte, escuela, salud, entretenimiento): ")
        categoria = validar_categoria(categoria)
        dinero_total -= gasto
        return gasto, categoria
           
    else:
        print("La cantidad debe ser mayor a cero, se tomará como $0.")
        return 0, 0


def calcular_dinero_disponible(total_ingresos, total_gastos):
    dinero_disponible = total_ingresos - total_gastos
    return dinero_disponible


def mostrar_movimiento(cantidad, origen):
    print("Movimiento: $", cantidad)
    print("Origen: ", origen)
    print("Dinero total: ", dinero_total)
    print()


def mostrar_resultados(total_ingresos, total_gastos, dinero_disponible):
    print("Total de ingresos: $", total_ingresos)
    print("Total de gastos: $", total_gastos)
    print("Dinero disponible: $", dinero_disponible)


# Funciones del Avance 4
# Estas funciones usan if, elif y else para tomar decisiones.

def validar_cantidad(cantidad):
    # Regresa la cantidad si es mayor a cero; si no, regresa 0
    if cantidad > 0:
        return True
    else:
        return False


def validar_categoria(categoria):
    # Regresa la categoría si es una de las del programa; si no, "otros"
    if categoria == "comida":
        return categoria
    elif categoria == "transporte":
        return categoria
    elif categoria == "escuela":
        return categoria
    elif categoria == "salud":
        return categoria
    elif categoria == "entretenimiento":
        return categoria
    else:
        print("Esa categoría no está en la lista, se guardará como otros.")
        return "otros"


def mostrar_mensaje_dinero(dinero_disponible):
    # Dice la situación del usuario según su dinero disponible
    if dinero_disponible < 0:
        print("Cuidado: gastaste más dinero del que recibiste.")
    elif dinero_disponible == 0:
        print("Ya no te queda dinero disponible.")
    else:
        print("¡Muy bien!, aún tienes dinero disponible.")


def mostrar_menu():
    print("******* Menú *******")
    print("1. Registrar ingreso")
    print("2. Registrar gasto")
    print("3. Salir")
    print()
    

# *******************************************************************
# Inicio
print("Bienvenido a Pluto, tu herramienta de organización de finanzas "
      "personales")
# *******************************************************************

#Variable para que el programa se repita
inicio = True
# Menú: el usuario elige una opción y el programa decide qué hacer
while (inicio):
    mostrar_menu()
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("******* Ingreso *******")
        ingreso, origen = registrar_ingreso()
        mostrar_movimiento(ingreso, origen)
        
    elif opcion == 2:
        print("******* Gasto *******")
        gasto, categoria = registrar_gasto()
        mostrar_movimiento(gasto, categoria)
        
    elif opcion == 3:
        print("Saliendo del programa...")
        inicio = False
    else:
        print("Opción no válida.")

# *******************************************************************
print("Gracias por cuidar tus finanzas personales :D")
# *******************************************************************