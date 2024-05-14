# Configurar BOT de Telegram

Una de las características más interesantes de nuestro servidor, es el [bot de Telegram](https://docs.google.com) al que se puede acceder mediante la propia APP o vía [WEB](espetoneta.es).

## Python - *pip* y *python3*

> [!NOTE]  
> Puedes usar `./instalar_requisitos.sh` para instalar los requisitos al completo. Explicaremos requisito a requisito.

Para poder instalar y configurar el BOT de Telegram, completamente programado en **python**, debemos tener unos requisitos a nivel de software instalado.

Primeramente, instalaremos [Python](https://wiki.archlinux.org/title/python), y su gestor de paquetes, [pip](https://archlinux.org/packages/extra/any/python-pip/)

```bash
sudo pacman -S python python-pip
```

#PENDIENTE DE EXPLICAR LOS PREGRAMAS REQUERIDOS. ACORDARSE DE LA CARPETA "REQUIRMENTS" Y EL SCRIPT DE INSTALACIÓN AUTOMÁTICA, COMO SE MENCIONA EN !NOTE.

## Funcionamiento
Este bot ha sido diseñado para poder controlar y monitorizar servidor a distancia desde el propio Telegram. De esta manera podemos realizar diversas acciones entre las que podemos encontrar:

| Comando           | Tipo       | Descripción                                            |
| :---------------- | :--------- | :----------------------------------------------------- |
| /help             | Sistema    | Muestra esta ayuda.                                    |
| /ping             | Redes      | Realiza un ping para ver la latencia.                  |
| /sysinfo          | Sistema    | Información del sistema, CPU y RAM.                    |
| /discos           | Sistema    | Información de discos y particiones.                   |
| /apagar           | Sistema    | Apaga el servidor, shutdown now.                       |
| /reboot           | Sistema    | Reinicia el servidor, reboot now.                      |

## Estructura de Archivos y Eficiencia

El bot se ha creado de manera muy eficiente, de manera que cuando se ejecuta en el servidor, se abre un archivo de pocas líneas. Sin embargo, cuando se hace uso de cualquier comando, este archivo consulta al resto de archivos que están separados por comandos. De esta manera cuando el bot esté en "standby" o en espera de comandos, haciendo que se ejecutan programas de pocas líneas, y a consecuencia, un menor consumo de recursos.

```Documentos/
|-- comandos/                   # Directorio de comandos y logs
|   |-- old/                    # Aquí encontramos el antiguo código del BOT, en un único archivo.
|   |-- __init__.py             # Instancia init.
|   |-- admin.py                # Comandos de apagado y reinicio, con guardado en log.
|   |-- botlog.txt              # Log de ejecución.
|   |-- discos.py               # Comando de obtención de información de los discos.
|   |-- ping.py                 # Comando de ping con el servidor.
|   |-- sysinfo.py              # Comando de obtención de información deel sistema.
|
|-- requirments/                # Directorio del script de instalación de los requisitos.
|   |-- install_requirments.py  # Script instalador de requisitos.
|   |-- requirments.txt         # Archivo de texto con los requisitos.
|
|-- main.py                     # Iniciador del BOT. Aplicación a ejecutar en el servidor.
```