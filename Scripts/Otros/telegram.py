import telebot
import time
import ping3
import os
from datetime import datetime
import pytz

bot = telebot.TeleBot("6572086972:AAFFAgetUyFYTIgjlPWQwv89qFjkY6iJBAs")
pinger = ping3.ping

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
Los comandos disponibles son:
- /help: Muestra esta ayuda.
- /ping: Realiza un ping para ver la latencia.
- /temp: Muestra la temperatura actual de la CPU.
- /apaga: Apaga el servidor, shutdown now.
- /reboot: Reinicia el servidor, reboot now.

"""
    bot.send_message(message.chat.id, mensaje)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ APAGA
    
@bot.message_handler(commands=['apagar'])
def apagar_servidor(message):
    usuario = f"{message.from_user.username} ({message.from_user.id})"

    bot.send_message(message.chat.id, "Apagando servidor...")
    


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ REBOOT
    
@bot.message_handler(commands=['reboot'])
def help(message):
    bot.send_message(message.chat.id, "Reiniciando servidor...")
    print("Reiniciando servidor y guardando el log...")
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

        logeo = (f"El usuario {usuario} ha reiniciado el servidor. {fecha_formateada}\n")
        archivo1.write(str(logeo))

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ REBOOT
@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    bot.send_message(message.chat.id, "Comando no reconocido. Escribe /help para ver la lista de comandos disponibles.")

bot.polling()