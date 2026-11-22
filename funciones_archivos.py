from pathlib import Path

# Verificar si un archivo existe
def verificar_existencia(ruta) :
    path = Path(ruta)
    return path.is_file()

def abrir_archivo(ruta, modo = "r", tipo = "t") :
    if modo == "r" :
        if not verificar_existencia(ruta) :
            open(ruta, "x")

        return open(ruta, "r" + tipo)

    return open(ruta, modo + tipo)