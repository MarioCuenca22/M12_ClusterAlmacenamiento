import psutil

def handle_sysinfo(message, bot):
    def obtener_informacion_cpu():
        info_cpu = (
            f"Información de la CPU:\n"
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
