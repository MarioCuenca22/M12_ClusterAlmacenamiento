import ping3

pinger = ping3.ping

def handle_ping(message, bot):
    respuesta = pinger('google.es')
    if respuesta is not None:
        latencia = round(respuesta * 1000, 2)
    else:
        latencia = "N/A"
    bot.send_message(message.chat.id, f"Pong 🏓 {latencia} ms!")
    print(f"Latencia: {latencia} ms")
