import time
import os
import json
import subprocess
from colorama import Fore

def cargar_temas():
    temas = {}
    carpeta_temas = "/home/admin/.config/qtile/themes"
    id_tema = 1

    for nombre_archivo in os.listdir(carpeta_temas):
        if nombre_archivo.endswith(".json"):
            ruta_archivo = os.path.join(carpeta_temas, nombre_archivo)
            with open(ruta_archivo) as archivo_json:
                datos_tema = json.load(archivo_json)
                nombre_tema = os.path.splitext(nombre_archivo)[0]
                temas[str(id_tema)] = {"nombre": nombre_tema}
                id_tema += 1

    return temas

os.system("clear")
print(f"{Fore.RED}AVISO! {Fore.WHITE}Recuerda que al seleccionar un tema, el gestor de ventanas se reiniciará!\n")
time.sleep(3)

temas = cargar_temas()

print("TEMAS DISPONIBLES\n")

for id_tema, info_tema in temas.items():
    print(f"({id_tema}) {info_tema['nombre']}")

seleccion = input("\nSelecciona el tema deseado: ")

if seleccion in temas:
    print(f"\nEl tema seleccionado es: {Fore.YELLOW}{temas[seleccion]['nombre']}{Fore.WHITE}")
    ruta_config_qtile = os.path.expanduser("/home/admin/.config/qtile/config.json")
    with open(ruta_config_qtile, 'w') as archivo:
        archivo.write('{"theme": "' + temas[seleccion]['nombre'] + '"}')
    time.sleep(3)
    subprocess.run(["xdotool", "key", "Super_L+Control_R+r"])
    os.system("clear")
else:
    print("Número de tema no válido")
    os.system("clear")
