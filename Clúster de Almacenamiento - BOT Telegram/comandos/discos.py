import psutil

def handle_discos(message, bot):
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
