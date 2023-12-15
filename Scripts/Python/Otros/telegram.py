import telebot
import subprocess
import time
import threading

TOKEN = "6572086972:AAFFAgetUyFYTIgjlPWQwv89qFjkY6iJBAs"
CHAT_ID = " 6111310001"

bot = telebot.TeleBot(TOKEN)

def obtener_datos(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        datos = archivo.readline().strip()
        return datos

def obtener_temperatura():
    comando = "vcgencmd measure_temp"
    proceso = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE)
    salida = proceso.communicate()[0].decode()

    temperatura = float(salida.split('=')[1].split('\'')[0])
    temperatura_truncada = '{:.1f}'.format(temperatura)
    return float(temperatura_truncada)
 
def apagado(password):
    comando = "sudo -S shutdown now"
    proceso = subprocess.Popen(comando, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida, error = proceso.communicate(input=(password + '\n').encode())
    if error:
        print("Ocurrió un error:", error.decode())

ruta_archivo = '/etc/fonts/fonts.txt'
password = obtener_datos(ruta_archivo)

def benchmark_potente(message):
    bot.send_message(message.chat.id, "Realizando benchmark potente...")

    comando_benchmark = "sudo stress-ng --cpu 4 --timeout 60s"
    proceso_benchmark = subprocess.Popen(comando_benchmark, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    salida_benchmark, error_benchmark = proceso_benchmark.communicate(input=(password + '\n').encode())

    if error_benchmark:
        bot.send_message(message.chat.id, f"Ocurrió un error al ejecutar el benchmark: {error_benchmark.decode()}")
    else:
        for _ in range(12):
            temperatura = obtener_temperatura()
            bot.send_message(message.chat.id, f"La temperatura del procesador es: {temperatura}°C")
            time.sleep(5) 

        bot.send_message(message.chat.id, "Benchmark potente completado.")


@bot.message_handler(commands=["temp"])
def benchmark_potente(message):
    temperatura = obtener_temperatura()
    bot.send_message(message.chat.id, f"La temperatura del procesador es: {temperatura}°C") 

@bot.message_handler(commands=["help"])
def ayuda(message):
    commandos = [
        "/help - Imprime este mensaje.\n",
        "/temp - Consulta la temperatura una vez.\n",
        "/ping_t - Consulta la temperatura 10 veces.\n",
        "/apaga - Apaga remotamente el servidor.\n",
        "/benchp - Realiza un benchmark potente.\n",
    ]

    lista_comandos = "".join(commandos)
    texto_ayuda = (
        "¡Hola! Aquí están los comandos disponibles:\n\n" + lista_comandos +
        "\n\nPara obtener más detalles sobre un comando, simplemente escribe el comando (por ejemplo, /benchp)."
    )
    bot.reply_to(message, texto_ayuda)


bot.polling()
