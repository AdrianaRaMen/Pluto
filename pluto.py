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

#*******************************************************************
#Inicio
print("Bienvenido a Pluto, tu herramienta de organización de finanzas personales")
#*******************************************************************

#Registrar ingreso
ingreso, origen = registrar_ingreso()

#Registrar gasto
gasto, categoria = registrar_gasto()

#Mostrar movimientos
print("*******Movimientos*******")
print("Ingreso: $", ingreso)
print("Origen del ingreso: ", origen)
print("Gasto: $", gasto)
print("Categoría del gasto: ", categoria)

#En este avance solo hay un ingreso y un egreso registrado debido a que aún no sé cómo registrar varios ingresos y gastos. 
#Investigué y se podría hacer con un acumulador, pero aún no sé cómo se usan, en este se implementaria el operador de suma.
#Por lo anterior el "total" es igual a ese único valor, sería el único valor que ya tengo.

total_ingresos = ingreso
total_gastos = gasto

#Calcular el dinero disponible
dinero_disponible = calcular_dinero_disponible (total_ingresos, total_gastos)

#Mostrar resultados
print("Resultados")
print("Total de ingresos: $", total_ingresos)
print("Total de gastos: $", total_gastos)
print("Dinero disponible: $", dinero_disponible)

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

#Si el tiempo es suficiente se planea agregar al programa lo siguiente:
# ~ Crear una meta de ahorro.
# ~ Ver el avance de una meta de ahorro.
# ~ Buscar un gasto o ingreso ya registrado.