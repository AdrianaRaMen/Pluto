import pandas as pd
import os
from funciones_archivos import abrir_archivo

"""Proyecto Pluto.

Herramienta de organización de finanzas personales.
El programa permite registrar un ingreso y un gasto, y después elegir
qué información quiere ver el usuario.
"""
dinero_total = 0
lista_ingresos = []
lista_gastos = []
lista_categoria_gastos = []

# Avance 9 (rutas de los archivos de texto)
RUTA_MOVIMIENTOS = "./datos/movimientos.txt"
RUTA_RESUMEN = "./datos/resumen.txt"
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

        # Avance 9 (guardar el ingreso en el archivo de movimientos)
        guardar_movimiento("ingreso", ingreso, origen)
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

        # Avance 9 (guardar el gasto en el archivo de movimientos)
        guardar_movimiento("gasto", gasto, categoria)
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

    # Avance 9 (mostrar también lo que está guardado en el archivo)
    mostrar_movimientos_guardados()


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


# Funciones del Avance 8

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
    # Avance 9 (para actualizar el dinero total al cargar)
    global dinero_total

    if os.path.exists("historialGastos.csv") and os.path.exists("historialIngresos.csv"):
        dfGastos = pd.read_csv("historialGastos.csv", sep=",")
        dfIngresos = pd.read_csv("historialIngresos.csv", sep=",")
        print(dfGastos)
        print(dfIngresos)

        lista_ingresos = dfIngresos["Ingresos"].to_list()
        matriz[1] = dfGastos["Categoría Gastos"].to_list()
        matriz[0] = dfGastos["Gastos"].to_list()

        # Avance 9 (calcular el dinero total con lo que se cargó)
        dinero_total = calcular_dinero_disponible(sum(lista_ingresos), sum(matriz[0]))
    else:
        print("No se encontraron registros anteriores")
        print()


# Funciones del Avance 9

def guardar_movimiento(tipo, cantidad, descripcion):
    # Agrega el movimiento al final del archivo (modo append)
    # Cada línea queda así: tipo,cantidad,descripcion
    archivo = open(RUTA_MOVIMIENTOS, "at")
    archivo.write(f"{tipo},{cantidad},{descripcion}\n")
    archivo.close()


def mostrar_movimientos_guardados():
    # Lee el archivo de movimientos línea por línea
    archivo = abrir_archivo(RUTA_MOVIMIENTOS)
    contador = 0

    print("Movimientos guardados en el archivo:")
    for linea in archivo:
        # Borrar salto de línea del final y espacios en blanco
        linea = linea.strip("\n").strip()
        if linea != "":
            datos = linea.split(",")
            tipo = datos[0]
            cantidad = float(datos[1])
            descripcion = datos[2]
            print(tipo.capitalize(), ": ", formatear_dinero(cantidad), "(", descripcion, ")")
            contador += 1

    if contador == 0:
        print("Todavía no hay movimientos guardados.")
    print()

    archivo.close()


def categoria_mayor_gasto():
    # Suma los gastos de cada categoría y regresa en la que se gastó más
    categorias = ["comida", "transporte", "escuela", "salud",
                  "entretenimiento", "vivienda", "gustos", "otros"]
    mayor_categoria = "ninguna"
    mayor_total = 0

    for categoria in categorias:
        total = 0
        for i in range(len(matriz[1])):
            if matriz[1][i] == categoria:
                total += matriz[0][i]

        if total > mayor_total:
            mayor_total = total
            mayor_categoria = categoria

    return mayor_categoria


def guardar_resumen():
    # Escribe un resumen de las finanzas (modo escritura, reemplaza lo anterior)
    total_ingresos = sum(lista_ingresos)
    total_gastos = sum(matriz[0])
    dinero_disponible = calcular_dinero_disponible(total_ingresos, total_gastos)

    archivo = open(RUTA_RESUMEN, "wt")
    archivo.write(f"Total de ingresos: {formatear_dinero(total_ingresos)}\n")
    archivo.write(f"Total de gastos: {formatear_dinero(total_gastos)}\n")
    archivo.write(f"Dinero disponible: {formatear_dinero(dinero_disponible)}\n")
    archivo.write(f"Categoría con más gasto: {categoria_mayor_gasto()}\n")
    archivo.close()

    print("Se guardó el resumen en", RUTA_RESUMEN)


def mostrar_resumen_anterior():
    # Lee el resumen que se guardó la última vez que se usó el programa
    archivo = abrir_archivo(RUTA_RESUMEN)
    contenido = archivo.read()
    archivo.close()

    if contenido == "":
        print("Todavía no hay un resumen guardado.")
    else:
        print("******* Resumen de la última vez *******")
        print(contenido)

# *******************************************************************
# Inicio
print("Bienvenido a Pluto, tu herramienta de organización de finanzas "
      "personales")
# *******************************************************************

#Variable para que el programa se repita
inicio = True
# Menú: el usuario elige una opción y el programa decide qué hacer

cargar_datos()

# Avance 9 (mostrar el resumen guardado la última vez)
mostrar_resumen_anterior()

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
        # Avance 9 (guardar el resumen en un archivo de texto)
        guardar_resumen()
        inicio = False
    else:
        print("Opción no válida.")

# *******************************************************************
print("Gracias por cuidar tus finanzas personales :D")
# *******************************************************************