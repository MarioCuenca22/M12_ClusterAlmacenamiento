
# M12 - Proyecto de Síntesis
## Python
#### Instalar pip y python3

```bash
sudo pacman -S python
sudo pacman -S python-pip
```

Nuestro servidor dispone de varias funcionalidades que hemos programado desde 0 para poder disfrutar más la experiencia de este. La primera y la más destacable de ellas es el [bot de Telegram](https://docs.google.com) al que se puede acceder mediante la propia APP o vía WEB.

> [!NOTE]  
> Tener instalado `pip` y `python3`.

> [!WARNING]  
> Usa `./instalar_requisitos.sh` para instalar los requisitos.

## BOT Telegram
Este bot ha sido diseñado para poder "controlar" la terminal del servidor a distancia desde la propia APP o sitio Weeb de Telegram. De esta manera podemos realizar diversas acciones entre las que podemos encontrar:

| Comando           | Tipo       | Descripción                                            |
| :---------------- | :--------- | :----------------------------------------------------- |
| /help             | Sistema    | Muestra esta ayuda.                                    |
| /ping             | Redes      | Realiza un ping para ver la latencia.                  |
| /sysinfo          | Sistema    | Información del sistema, CPU y RAM.                    |
| /discos           | Sistema    | Información de discos y particiones.                   |
| /apagar           | Sistema    | Apaga el servidor, shutdown now.                       |
| /reboot           | Sistema    | Reinicia el servidor, reboot now.                      |

El bot se ha creado de manera hyper-eficiente de manera que cuando se ejecuta en el servidor se abre un archivo de pocas líneas sin embargo cuando se hace uso de cualquier comando este archivo consulta a otros archivos que están separados en rama para acceder a los comandos, de esta manera cuando el bot esté en "standby" o en espera de comandos se ejecutarán pocas líneas y a consecuencia se consumirán pocos recursos.

##### Estructura de archivos para comandos
```Documentos/
|-- comandos/
|   |-- __init__.py
|   |-- ping.py
|   |-- sysinfo.py
|   |-- discos.py
|   |-- admin.py
|-- main.py
```

## Theme Changer
Hemos creado un sistema para poder cambiar el tema actual de Qtile sin tener que entrar en archivos de configuración externos para usuarios no tan avanzados, ejecutando el archivo [theme.py](https://github.com/MarioCuenca22/M12/blob/main/Scripts/OS/theme.py). Que debería ubicarse en el escritorio puedes modificarlo más fácilmente.

## Temperatura
Con el archivo temperatura.py podrás hacer una especie de "ping" que te permetirá monitorear la temperatura de la CPU 
> [!IMPORTANT]  
> Solo disponible para Raspberry PI 3/4  .

De no estar ejecutandose fuera de una Raspberry 3 o 4 el código no funcionará ni standalone ni con sus afiliados como el Bot de telegram.