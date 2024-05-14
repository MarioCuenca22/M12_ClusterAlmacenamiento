# main.py
import telebot
from commands import ping, sysinfo, discos, admin

bot = telebot.TeleBot("X")

@bot.message_handler(commands=['help'])
def help(message):
    mensaje = """
    Bienvenido al bot de control de nuestro servidor!
    A continuación verás los comandos disponibles.

    Consultas:
    - /help: Muestra esta ayuda.
    - /ping: Realiza un ping para ver la latencia.
    - /sysinfo: Información del sistema, CPU y RAM.
    - /discos: Información de discos y particiones.

    Administración ⚠:
    - /apagar: Apaga el servidor, shutdown now.
    - /reboot: Reinicia el servidor, reboot now.
    """
    bot.send_message(message.chat.id, mensaje)

# Importa los comandos desde el paquete comandos
@bot.message_handler(commands=['ping'])
def handle_ping(message):
    ping.handle_ping(message, bot)

@bot.message_handler(commands=['sysinfo'])
def handle_sysinfo(message):
    sysinfo.handle_sysinfo(message, bot)

@bot.message_handler(commands=['discos'])
def handle_discos(message):
    discos.handle_discos(message, bot)

@bot.message_handler(commands=['apagar'])
def handle_apagar(message):
    admin.handle_apagar(message, bot)

@bot.message_handler(commands=['reboot'])
def handle_reboot(message):
    admin.handle_reboot(message, bot)

@bot.message_handler(func=lambda message: True)
def handle_messages(message):
    bot.send_message(message.chat.id, "Comando no reconocido 📍 Escribe /help para ver la lista de comandos disponibles.")

if __name__ == "__main__":
    bot.polling()
