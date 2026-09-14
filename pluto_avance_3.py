""" Proyecto Pluto """
"""Herramienta de organización de finanzas personales"""
"""El programa permitirá a los usuarios registrar sus gastos y administrar sus ingresos para distribuir su dinero de una manera más organizada y consciente"""
""" Al final el usuario podrá reconocer sus principales patrones de gasto y tomar decisiones más informadas sobre la administración de sus recursos"""

#Avance 2: Incorporar al proyecto libre operaciones con operadores

def registrar_ingreso():
    cantidad = float(input("Dinero que se recibió: $"))
    origen = input("Fuente de la que se obtuvo ese dinero: ")
    return cantidad, origen

def registrar_gasto():
    cantidad = float(input("Dinero que se gastó: $"))
    categoria = input("Uso que se le dio al dinero ")
    return cantidad, categoria

def calcular_dinero_disponible(total_ingresos, total_gastos):
    dinero_disponible = total_ingresos - total_gastos
    return dinero_disponible

#Funciones del Avance 3
#No tienen return, solo imprimen en pantalla.
#Las hice para no repetir tantas veces en el código los "print" como en el ejemplo
#del material que se encuentra en canvas.

def mostrar_ingreso(cantidad, origen):
    print("Ingreso: $", cantidad)
    print("Origen del ingreso: ", origen)

def mostrar_gasto(cantidad, categoria):
    print("Gasto: $", cantidad)
    print("Categoría del gasto: ", categoria)

def mostrar_resultados(total_ingresos, total_gastos, dinero_disponible):
    print("Total de ingresos: $", total_ingresos)
    print("Total de gastos: $", total_gastos)
    print("Dinero disponible: $", dinero_disponible)

#*******************************************************************
#Inicio
print("Bienvenido a Pluto, tu herramienta de organización de finanzas personales")
#*******************************************************************

#Registrar ingreso
ingreso, origen = registrar_ingreso()

#Registrar gasto
gasto, categoria = registrar_gasto()

#Mostrar movimientos
#Aquí ya no escribo los "print", sino que uso las funciones
#mostrar_ingreso y mostrar_gasto, mandando las variables como parámetros
print("*******Movimientos*******")
mostrar_ingreso(ingreso, origen)
mostrar_gasto(gasto, categoria)

#En este avance (avance 2) solo hay un ingreso y un egreso registrado debido a que aún no sé cómo registrar varios ingresos y gastos. 
#Investigué y se podría hacer con un acumulador, pero aún no sé cómo se usan, en este se implementaria el operador de suma.
#Por lo anterior el "total" es igual a ese único valor, sería el único valor que ya tengo.

total_ingresos = ingreso
total_gastos = gasto

#Calcular el dinero disponible
dinero_disponible = calcular_dinero_disponible (total_ingresos, total_gastos)

#Mostrar resultados
#Aquí uso la nueva función de mostrar_resultados en vez de los prints que tenía.
print("Resultados")
mostrar_resultados(total_ingresos, total_gastos, dinero_disponible)

#******************************************************************
print("Gracias por cuidar tus finanzas personales :D")

#******************************************************************
#Faltantes para completar el proyecto
#Todavía no desarrollo estas partes del código porque aún no sé cómo hacerlas:
# ~ Que se pueda repetir el programa para registrar varios ingresos y gastos, no solo uno de cada uno.
# ~ Un acumulador que sume todos los ingresos y todos los gastos conforme se van registrando
#   (por el momento el total es el único valor que se registró).
# ~ Un menu que permita elegir qué operación hacer cada vez.
# ~ Ver en qué categoría se gasta más dinero.