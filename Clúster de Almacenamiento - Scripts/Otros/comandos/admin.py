# comandos/admin.py
import os
from datetime import datetime
import pytz

def handle_apagar(message, bot):
    ids_permitidas = ["DanituID"] # "6111310001"

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
        if message.chat.id in ids_permitidas:
            usuario = "Desconocido"
            if message.chat.id == 611131001:
                usuario = "Mario"
            elif message.chat.id == "DanituID":
                usuario = "Daniel"

            logeo = f"El usuario {usuario} ha apagado el servidor. {fecha_formateada}\n"
            archivo1.write(str(logeo))
            # ALADIN

        else:
            bot.send_message(message.chat.id, "No tienes los permisos para apagar el servidor.")
            bot.send_message(message.chat.id, "Este problema será notificado a los administradores.")
            print(f"AVISO: El usuario {message.chat.id} no tiene permisos para apagar el servidor.")
            logeo2 = f"El usuario {message.chat.id} ha intentado apagar el servidor sin permisos. {fecha_formateada}\n"
            archivo1.write(str(logeo2))

def handle_reboot(message, bot):
    ids_permitidas = [6111310001, "DanituID"]

    madrid_tz = pytz.timezone('Europe/Madrid')
    diahora = datetime.now(madrid_tz)
    formato_deseado = '%d-%m-%Y %H:%M:%S'
    fecha_formateada = diahora.strftime(formato_deseado)

    directorio = os.path.dirname(os.path.realpath(__file__))
    dirarchi = os.path.join(directorio, 'botlog.txt')

    with open(dirarchi, 'a') as archivo1:
        if message.chat.id in ids_permitidas:
            bot.send_message(message.chat.id, "Reiniciando servidor...")
            print("AVISO: Reiniciando servidor y guardando el log...")

            usuario = "Desconocido"
            if message.chat.id == 6111310001:
                usuario = "Mario"
            elif message.chat.id == "DanituID":
                usuario = "Daniel"

            logeo = f"El usuario {usuario} ha reiniciado el servidor. {fecha_formateada}\n"
            archivo1.write(str(logeo))
            # ALADIN

        else:
            bot.send_message(message.chat.id, "No tienes los permisos para reiniciar el servidor.")
            bot.send_message(message.chat.id, "Este problema será notificado a los administradores.")
            print(f"AVISO: El usuario {message.chat.id} no tiene permisos para reiniciar el servidor.")
            logeo2 = f"El usuario {message.chat.id} ha intentado reiniciar el servidor sin permisos. {fecha_formateada}\n"
            archivo1.write(str(logeo2))
