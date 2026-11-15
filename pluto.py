import pandas as pd
import os

"""Proyecto Pluto.

Herramienta de organización de finanzas personales.
El programa permite registrar un ingreso y un gasto, y después elegir
qué información quiere ver el usuario.
"""
dinero_total = 0
lista_ingresos = []
lista_gastos = []
lista_categoria_gastos = []
matriz = [ 
    lista_gastos, lista_categoria_gastos
]

def registrar_ingreso():
    global dinero_total

    ingreso = float(input("Dinero que se recibió: $"))
    if validar_cantidad(ingreso):
        origen = validar_texto(input("Fuente de la que se obtuvo ese dinero: "))

        # Registrar ingreso
        lista_ingresos.append(ingreso)
        dinero_total += ingreso
        return ingreso, origen
    else:
        print("La cantidad debe ser mayor a cero, se tomará como $0.")
        return 0, 0


def registrar_gasto():
    global dinero_total

    gasto = float(input("Dinero que se gastó: $"))
    if validar_cantidad(gasto):
        categoria = input("Categoría (comida, transporte, escuela, salud, entretenimiento, vivienda, gustos): ")
        categoria = validar_categoria(categoria)

        # Registrar gasto
        matriz[0].append(gasto)
        matriz[1].append(categoria)

        dinero_total -= gasto
        return gasto, categoria
           
    else:
        print("La cantidad debe ser mayor a cero, se tomará como $0.")
        return 0, 0


def calcular_dinero_disponible(total_ingresos, total_gastos):
    dinero_disponible = total_ingresos - total_gastos
    return dinero_disponible


def mostrar_movimiento(cantidad, origen):
    print("Movimiento: ", formatear_dinero(cantidad))
    print("Origen: ", str(origen).capitalize())
    print("Dinero total: ", formatear_dinero(dinero_total))
    print()


def mostrar_historial():
    print("Total de ingresos: ", lista_ingresos)
    print("Total de gastos: ", matriz[0])
    print("Categorías de los gastos: ", matriz[1])
    print("Dinero disponible: ", formatear_dinero(dinero_total))
    print()


# Funciones del Avance 4
# Estas funciones usan if, elif y else para tomar decisiones.

def validar_cantidad(cantidad):
    # Regresa la cantidad si es mayor a cero; si no, regresa 0
    if cantidad > 0:
        return True
    else:
        return False


def validar_categoria(categoria):
    # Quita los espacios y pasa la categoría a minúsculas
    categoria = categoria.strip().lower()

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
    elif categoria == "vivienda":
            return categoria
    elif categoria == "gustos":
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
    print("3. Ver historial de movimientos")
    print("4. Buscar gastos por categoría")
    print("5. Salir")
    print()


# Funciones del Avance 9

def validar_texto(texto):
    # Quita los espacios y pasa el texto a minúsculas;
    # si el texto queda vacío regresa "sin especificar"
    texto = texto.strip()
    if texto == "":
        return "sin especificar"
    else:
        return texto.lower()


def formatear_dinero(cantidad):
    # Regresa la cantidad como texto con signo de pesos y dos decimales
    return "$" + str(round(cantidad, 2))


def buscar_gastos():
    # Busca los gastos cuya categoría contenga el texto que escribe el usuario
    busqueda = input("Categoría que quieres buscar: ").strip().lower()

    if busqueda == "":
        print("No escribiste nada para buscar.")
        print()
    else:
        encontrados = 0
        total = 0
        for i in range(len(matriz[1])):
            if busqueda in matriz[1][i]:
                print(matriz[1][i].capitalize(), ": ", formatear_dinero(matriz[0][i]))
                encontrados += 1
                total += matriz[0][i]

        if encontrados == 0:
            print("No se encontraron gastos con esa categoría.")
        else:
            print("Gastos encontrados: ", encontrados)
            print("Total gastado: ", formatear_dinero(total))
        print()


def guardar_datos():
    diccionario_gastos = {
        "Gastos": matriz[0],
        "Categoría Gastos": matriz[1]
    }
    dfGastos = pd.DataFrame(diccionario_gastos)

    diccionario_ingresos = {
            "Ingresos": lista_ingresos,
        }
    dfIngresos = pd.DataFrame(diccionario_ingresos)

    print(dfGastos)
    print(dfIngresos)

    dfGastos.to_csv("historialGastos.csv", index=False)
    dfIngresos.to_csv("historialIngresos.csv", index=False)


def cargar_datos():
    global lista_ingresos
    global matriz

    if os.path.exists("historialGastos.csv") and os.path.exists("historialIngresos.csv"):
        dfGastos = pd.read_csv("historialGastos.csv", sep=",")
        dfIngresos = pd.read_csv("historialIngresos.csv", sep=",")
        print(dfGastos)
        print(dfIngresos)

        lista_ingresos = dfIngresos["Ingresos"].to_list()
        matriz[1] = dfGastos["Categoría Gastos"].to_list()
        matriz[0] = dfGastos["Gastos"].to_list()
    else:
        print("No se encontraron registros anteriores")
        print()

# *******************************************************************
# Inicio
print("Bienvenido a Pluto, tu herramienta de organización de finanzas "
      "personales")
# *******************************************************************

#Variable para que el programa se repita
inicio = True
# Menú: el usuario elige una opción y el programa decide qué hacer

cargar_datos()

while (inicio):
    #Función para guardar los datos ingresados con anterioridad
    mostrar_menu()
    opcion = int(input("Elige una opción: "))

    # Salto de linea
    print()

    if opcion == 1:
        print("******* Ingreso *******")
        ingreso, origen = registrar_ingreso()
        mostrar_movimiento(ingreso, origen)
        
    elif opcion == 2:
        print("******* Gasto *******")
        gasto, categoria = registrar_gasto()
        mostrar_movimiento(gasto, categoria)

    elif opcion == 3:
        print("******* Historial de movimientos *******")
        mostrar_historial()

    elif opcion == 4:
        print("******* Buscar gastos *******")
        buscar_gastos()
        
    elif opcion == 5:
        print("Saliendo del programa...")
        guardar_datos()
        inicio = False
    else:
        print("Opción no válida.")

# *******************************************************************
print("Gracias por cuidar tus finanzas personales :D")
# *******************************************************************