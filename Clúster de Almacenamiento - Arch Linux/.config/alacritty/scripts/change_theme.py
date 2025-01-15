import time
import os
import subprocess
from colorama import Fore

USER = os.getenv("USER) or os.getenv("USERNAME)

def cargar_temas():
    temas = {}
    carpeta_temas = f"/home/{USER}/.config/alacritty/themes"
    id_tema = 1

    for nombre_archivo in os.listdir(carpeta_temas):
        if nombre_archivo.endswith(".toml"):
            ruta_archivo = os.path.join(carpeta_temas, nombre_archivo)
            nombre_tema = os.path.splitext(nombre_archivo)[0]
            temas[str(id_tema)] = {"nombre": nombre_tema, "ruta": ruta_archivo}
            id_tema += 1

    return temas

os.system("clear")

temas = cargar_temas()

print("TEMAS DISPONIBLES\n")

for id_tema, info_tema in temas.items():
    print(f"({id_tema}) {info_tema['nombre']}")

seleccion = input("\nSelecciona el tema deseado: ")

if seleccion in temas:
    print(f"\nEl tema seleccionado es: {Fore.YELLOW}{temas[seleccion]['nombre']}{Fore.WHITE}")
    ruta_config_alacritty = os.path.expanduser(f"/home/{USER}/.config/alacritty/alacritty.toml")
    with open(ruta_config_alacritty, 'r+') as archivo:
        lineas = archivo.readlines()
        lineas[0] = f"import = ['{temas[seleccion]['ruta']}']\n"
        archivo.seek(0)
        archivo.writelines(lineas)
        archivo.truncate()
    time.sleep(3)
    os.system("clear")
else:
    print("Número de tema no válido")
    os.system("clear")
