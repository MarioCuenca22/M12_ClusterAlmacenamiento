import time

# Recuerda que este código está hecho para ser usado en Raspberry Pi 4 y en Arch / Linux

def obtener_temperatura_cpu_rpi():
    try:
        with open("/sys/class/thermal/thermal_zone0/temp", "r") as file:
            temperatura = int(file.read()) / 1000.0  # La temperatura se proporciona en miligrados
        return temperatura
    except Exception as e:
        print(f"Error al obtener la temperatura de la CPU: {e}")
        return None

def main():
    try:
        while True:
            temperatura_actual = obtener_temperatura_cpu_rpi()

            if temperatura_actual is not None:
                print(f"Temperatura actual: {temperatura_actual}ºC")
            else:
                print("No se pudo obtener la temperatura.")

            # Esperar un segundo antes de volver a obtener la temperatura
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nPrograma terminado por el usuario.")

if __name__ == "__main__":
    main()
