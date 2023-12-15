import time
import os
from colorama import Fore

os.system("cls")
print(f"{Fore.RED}AVISO! {Fore.WHITE}Recuerda que al seleccionar un tema el sistema operativo se reiniciará!\n")
time.sleep(3)
print("(1) Dark Grey")
print("(2) Dracula")
print("(3) Material Darker")
print("(4) Material Ocean")
print("(5) Monokai Pro")
print("(6) Nord")
print("(7) Nord Wave")
print("(8) One Dark")
print("(9) Rosepine\n")

temas = {
    "1": {"nombre": "Dark Grey", "id": "1"},
    "2": {"nombre": "Dracula", "id": "2"},
    "3": {"nombre": "Material Darker", "id": "3"},
    "4": {"nombre": "Material Ocean", "id": "4"},
    "5": {"nombre": "Monokai Pro", "id": "5"},
    "6": {"nombre": "Nord", "id": "6"},
    "7": {"nombre": "Nord Wave", "id": "7"},
    "8": {"nombre": "One Dark", "id": "8"},
    "9": {"nombre": "Rosepine", "id": "9"},
}

selección = input("Selecciona el tema deseado (1-10): ")

if selección in temas:
    print(f"El tema seleccionado es: {Fore.YELLOW}{temas[selección]['nombre']}{Fore.WHITE}")
else:
    print("Número de tema no válido")


seguro = input(f"Tu tema escogido ha sido {Fore.YELLOW}{selección}{Fore.WHITE} estás seguro? (y/n) ")

