import telebot
import time
import ping3
import os
from datetime import datetime
import pytz
import psutil
from colorama import Fore

bot = telebot.TeleBot("6572086972:AAFFAgetUyFYTIgjlPWQwv89qFjkY6iJBAs")
pinger = ping3.ping
amarillo = Fore.YELLOW
verde = Fore.GREEN
rojo = Fore.RED
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ PINGS

@bot.message_handler(commands=['ping'])
def start(message):
    respuesta = pinger('google.es')

    if respuesta is not None:
        latencia = round(respuesta * 1000, 2)
    else:
        latencia = "N/A"

    bot.send_message(message.chat.id, f"Pong 🏓 {latencia} ms!")

    print(f"Latencia: {latencia} ms")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ HELP
    
@bot.message_handler(commands=['help'])
def help(message):
    mensaje = """

Consultas:
- /help: Muestra esta ayuda.
- /ping: Realiza un ping para ver la latencia.
- /sysinfo: Información del sistema, CPU y RAM.
- /discos: Información de discos y particiones.

Administración:
- /apaga: Apaga el servidor, shutdown now.
- /reboot: Reinicia el servidor, reboot now.

"""
    bot.send_message(message.chat.id, mensaje)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ APAGA
    
@bot.message_handler(commands=['apagar'])
def apagar_servidor(message):
    usuario = f"{message.from_user.username} ({message.from_user.id})"

    bot.send_message(message.chat.id, "Apagando servidor...")
    print("Apagando servidor y guardando log...")
    madrid_tz = pytz.timezone('Europe/Madrid')
    diahora = datetime.now(madrid_tz)

    formato_deseado = '%d-%m-%Y %H:%M:%S'
    fecha_formateada = diahora.strftime(formato_deseado)

    directorio = os.path.dirname(os.path.realpath(__file__))
    dirarchi = os.path.join(directorio, 'botlog.txt')
    with open(dirarchi, 'a') as archivo1:  

        if message.chat.id == 6111310001:
            usuario = "Mario"
        elif message.chat.id == "DanituID":
            usuario = "Daniel"
        else:
            usuario = message.chat.id

        logeo = (f"El usuario {usuario} ha apagado el servidor. {fecha_formateada}\n")
        archivo1.write(str(logeo))
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SysInfo
    
@bot.message_handler(commands=['sysinfo'])
def mostrar_informacion_sistema(message):
    usuario = f"{message.from_user.username} ({message.from_user.id})"
    
    def obtener_informacion_cpu():
        info_cpu = (
            f"Información de la CPU:\n"
            f"Número de núcleos físicos: {psutil.cpu_count(logical=False)}\n"
            f"Número de núcleos lógicos: {psutil.cpu_count(logical=True)}\n"
            f"Porcentaje de uso de la CPU: {psutil.cpu_percent(interval=1)}%"
        )
        return info_cpu

    def obtener_informacion_memoria():
        mem = psutil.virtual_memory()
        info_memoria = (
            f"\nInformación de la memoria:\n"
            f"Memoria total: {mem.total} bytes\n"
            f"Memoria disponible: {mem.available} bytes\n"
            f"Porcentaje de uso de la memoria: {mem.percent}%"
        )
        return info_memoria

    def obtener_informacion_red():
        info_red = psutil.net_io_counters()
        info_red_texto = (
            f"\nInformación de la red:\n"
            f"Bytes enviados: {info_red.bytes_sent}\n"
            f"Bytes recibidos: {info_red.bytes_recv}"
        )
        return info_red_texto

    informacion_cpu = obtener_informacion_cpu()
    informacion_memoria = obtener_informacion_memoria()
    informacion_red = obtener_informacion_red()

    mensaje_final = f"{informacion_cpu}\n{informacion_memoria}\n{informacion_red}"
    bot.send_message(message.chat.id, mensaje_final)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ SysInfo
    
@bot.message_handler(commands=['discos'])
def mostrar_informacion_sistema(message):
    usuario = f"{message.from_user.username} ({message.from_user.id})"
    
    def obtener_informacion_disco():
        infodisco = "\nInformación del disco:\n"
        particiones = psutil.disk_partitions()
        for particion in particiones:
            infoparti = psutil.disk_usage(particion.mountpoint)
            infodisco += (
                f"Partición:{particion.device}\n"
                f"Espacio total en la partición: {infoparti.total} bytes\n"
                f"Espacio utilizado en la partición: {infoparti.used} bytes\n"
                f"Espacio libre en la partición: {infoparti.free} bytes\n"
                f"Porcentaje de uso en la partición: {infoparti.percent}%\n"
                "--------------------------------------------------------------------------------\n"
            )
        return infodisco

    informacion_disco = obtener_informacion_disco()

    mensaje_final = f"{informacion_disco}"
    bot.send_message(message.chat.id, mensaje_final)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ REBOOT
ids_permitidas = [6111310001, "DanituID"]

@bot.message_handler(commands=['reboot'])
def help(message):
    madrid_tz = pytz.timezone('Europe/Madrid')
    diahora = datetime.now(madrid_tz)
    formato_deseado = '%d-%m-%Y %H:%M:%S'
    fecha_formateada = diahora.strftime(formato_deseado)

    directorio = os.path.dirname(os.path.realpath(__file__))
    dirarchi = os.path.join(directorio, 'botlog.txt')

    if message.chat.id in ids_permitidas:
        bot.send_message(message.chat.id, "Reiniciando servidor...")
        print(f"{amarillo}AVISO:{Fore.RESET} Reiniciando servidor y guardando el log...")

        with open(dirarchi, 'a') as archivo1:
            usuario = "Desconocido"
            if message.chat.id == 6111310001:
                usuario = "Mario"
            elif message.chat.id == "DanituID":
                usuario = "Daniel"

            logeo = f"El usuario {usuario} ha reiniciado el servidor. {fecha_formateada}\n"
            archivo1.write(str(logeo))
            print("sudo reboot now") #Cambiar por un reboot now funcional.
    else:
        bot.send_message(message.chat.id, "No tienes los permisos para reiniciar el servidor.")
        bot.send_message(message.chat.id, "Este problema será notificado a los administradores.")
        print(f"{amarillo}AVISO:{Fore.RESET} El usuario {message.chat.id} no tiene permisos para reiniciar el servidor.")
        with open(dirarchi, 'a') as archivo1:
            logeo2 = f"El usuario {message.chat.id} ha intentado reiniciar el servidor sin permisos. {fecha_formateada}\n"
            archivo1.write(str(logeo2))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ EXCLUSIONES
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    bot.send_message(message.chat.id, "Comando no reconocido 📍 Escribe /help para ver la lista de comandos disponibles.")

bot.polling()