# Configuración de Arch Linux

Esta guía es una recopilación de todos los pasos necesarios para construir un entorno de escritorio a partir de una instalación limpia basada en Arch Linux. Podéis elegir el gestor de ventanas que queráis, pero aquí usaremos Qtile como primer "tiling window manager". Esta guía es básicamente una descripción de cómo hemos construido nuestro entorno de escritorio desde 0.

Como hemos comentado, nos basaremos de una instalación limpia de Arch Linux. Dejamos la guía [aquí](https://docs.google.com/document/d/1T74VJPgouKC-BnTltKkQZuOcEpC_ARj_kXZPgsYHiCs/edit?usp=sharing) (Mirar solo el encabezado "**Instalación**") para que podáis instalar de 0 este SO

## Pasos Previos
Antes de pasar a la personalización del SO, necesitamos unos útiles básicos, e instalar **sudo** para obtener privilegios de superusuario:

```bash
pacman -S sudo
```

### Redes y Internet
La [Wiki de Arch](https://wiki.archlinux.org/index.php/Installation_guide) no dice qué hacer después de establecer la contraseña del superusuario, por lo que nos aseguraríamos de tener internet con [NetworkManager](https://wiki.archlinux.org/title/NetworkManager), y lo habilitaremos para que se ejecuta el iniciar el sistema:

```bash
pacman -S networkmanager
systemctl enable NetworkManager
```

### Gestor de Arranque
Ahora podéis instalar un gestor de arranque, en nuestro caso, [grub](https://wiki.archlinux.org/title/GRUB). Así es como se haría en hardware moderno, suponiendo que has montado la partición efi en [/boot](https://wiki.archlinux.org/index.php/Installation_guide#Example_layouts):

```bash
pacman -S grub efibootmgr os-prober
grub-install --target=x86_64-efi --efi-directory=/boot
os-prober
grub-mkconfig -o /boot/grub/grub.cfg
```

### Usuario Personal
Una vez tengáis lo anterior, podéis proceder con la creación del usuario personal. Lo crearemos, estableceremos la contraseña y lo añadiremos a los grupos necesarios:

```bash
useradd -m username
passwd username
usermod -aG wheel,video,audio,storage username
```

Edita **/etc/sudoers** con un editor de texto y descomenta la línea con "wheel":

```bash
## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```
Ahora ya puedes reiniciar. Primero saldremos de la ISO, la desmontamos y finalmente, reiniciamos:

```bash
# Sal de la imagen ISO, desmóntala y extráela
exit
umount -R /mnt

reboot
```

### Redes y Internet II
Después de haber iniciado sesión, el internet debería funcionar sin problema, pero eso solo aplica si el ordenador está conectado por cable. Si no tiene puertos Ethernet, tenemos [NetworkManager](https://wiki.archlinux.org/index.php/NetworkManager), así que no hay problema.
Para conectaros a una red inalámbrica con este software solo debéis hacer esto:

```bash
# Lista las redes disponibles
nmcli device wifi list

# Conéctate a tu red
nmcli device wifi connect TU_SSID password TU_CONTRASEÑA
```

### Sistema de Ventanas
Lo último que tenemos que hacer antes de pensar en entornos de escritorio es instalar [Xorg](https://wiki.archlinux.org/index.php/Xorg), un sistema de ventanas:

```bash
sudo pacman -S xorg
```


## Inicio de Sesión y Gestor de Ventanas
Primero, necesitamos una forma de iniciar sesión y abrir programas como navegadores y terminales, así que empezaremos instalando [lightdm](https://wiki.archlinux.org/index.php/LightDM) y [qtile](https://wiki.archlinux.org/index.php/Qtile). *lightdm* no funcionará si no instalamos también un [greeter](https://wiki.archlinux.org/index.php/LightDM#Greeter). También necesitamos [xterm](https://wiki.archlinux.org/index.php/Xterm) porque esa es la terminal que qtile abre por defecto, hasta que lo cambiemos en el archivo de configuración. Para editar archivos de configuración necesitaremos también un editor de texto, [vscode](https://wiki.archlinux.org/index.php/Visual_Studio_Code). Por último necesitamos un navegador.

```bash
sudo pacman -S lightdm lightdm-gtk-greeter qtile xterm code firefox
```

Activad el servicio de *lightdm* y reiniciad el ordenador, deberíais poder iniciar sesión en *qtile* a través de *lightdm* una vez se vuelva a iniciar el sistema.

```bash
sudo systemctl enable lightdm
reboot
```

Antes de hacer nada, si no tenéis la distribución del teclado en español, deberíais cambiarla usando *setxkbmap*. Abre *xterm* con **Mod + Return**, y cambia la distribución a español:

```bash
setxkbmap es
```


## Configuración por Defecto de Qtile
Ahora que estáis dentro de *qtile*, deberíais conocer algunos de los atajos de teclado que vienen por defecto.

| **Atajo**            | **Acción**                          |
| -------------------- | ----------------------------------- |
| **Mod + Return**     | Abrir xterm                         |
| **Mod + K**          | Siguiente Ventana                   |
| **Mod + J**          | Anterior Ventana                    |
| **Mod + W**          | Cerrar Ventana                      |
| **Mod + [12345678]** | Espacio de Trabajo [12345678]       |
| **Mod + Ctrl + R**   | Reiniciar Qtile                     |
| **Mod + Ctrl + Q**   | Cerrar Sesión                       |

- **A partir de ahora, la configuración la aplicaremos sobre la estructura por defecto de archivos de qtile (~/.config/qtile). En nuestro caso hemos modificado la estructura por defecto, y hemos separado la configuración en varios archivos, haciendola más escalable. Podéis seguir la guía de este documento, y una vez acabada importar la carpeta [~/.config/qtile](https://github.com/MarioCuenca22/Sintesis-M12/tree/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/qtile) de este repositorio con nuestra estructura, y funcionará igual. La explicación más a fondo de la estructura la encontramos en el anterior enlace.**


## Utilidades del Sistema

### Fuentes
Las fuentes en Arch son básicamente un meme, antes de que os den problemas podéis simplemente instalar estos paquetes:

```bash
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

Para listar todas las fuentes disponibles, usaremos el siguiente comando:

```bash
fc-list
```

### AUR helper - *yay*
Instalad un **[AUR helper](https://wiki.archlinux.org/index.php/AUR_helpers)**, nosotros usamos [yay](https://github.com/Jguer/yay):

```bash
sudo pacman -S base-devel git
cd /opt/
sudo git clone https://aur.archlinux.org/yay-git.git
sudo chown -R username:username yay-git/
cd yay-git
makepkg -si
```

Con acceso al *Arch User Repository*, podéis instalar prácticamente
todo el software de este planeta que haya sido pensado para correr en Linux.

### Emulador de terminal - *alacritty*
En este punto podéis instalar otro emulador de terminal. [Alacritty](https://wiki.archlinux.org/title/Alacritty) es muy comodo y personalizable:

```bash
sudo pacman -S alacritty
```

Abre el archivo de configuración de Qtile:

```bash
code ~/.config/qtile/config.py
```

Al principio, después de los imports, encontrarás una variable **terminal**. Cambiaremos el valor al emulador de terminal que hemos instalado: 

```python
terminal = "alacritty"
```

- **Configuración y Explicación de Alacritty [aquí](https://github.com/MarioCuenca22/Sintesis-M12/tree/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/alacritty)** 

### Menú - *rofi*
Instalad un menú como [rofi](https://wiki.archlinux.org/index.php/Rofi) para poder abrir aplicaciones más comodamente sin depender de una terminal:

```bash
sudo pacman -S rofi
```

Después añadid atajos de teclado en la configuración de qtile para poder ejecutar el menú:

```python
Key([mod], "m", lazy.spawn("rofi -show run")),
Key([mod, 'shift'], "m", lazy.spawn("rofi -show")),
```

Reiniciad Qtile con **Mod + Ctrl + R**. Deberíais poder abrir el menú y el emulador de terminal usando los atajos de teclado que acabais de definir. 

Ahora, podéis cambiar su tema instalando unas dependencias y con el siguiente comando:

```bash
sudo pacman -S which def
rofi-theme-selector
```

- **Configuración y Explicación de Rofi [aquí](https://github.com/MarioCuenca22/Sintesis-M12/tree/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/rofi)**

### Fondo de Pantalla - *feh*
Lo primero es lo primero, vuestra pantalla se ve negra y vacía, así que probablemente queráis un fondo más bonito para no sentiros tan deprimidos. Podéis abrir *firefox* usando *rofi* y descargar un fondo de pantalla. Después instalad
**[feh](https://wiki.archlinux.org/index.php/Feh)**
y poned vuestro fondo:

```bash
sudo pacman -S feh
feh --bg-scale ruta/al/fondo/de/pantalla
```

En nuestro caso hemos creado el directorio [~/.config/Wallpapers](https://github.com/MarioCuenca22/Sintesis-M12/tree/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/Wallpapers) donde guardaremos los fondos de pantalla.

### Audio - *pavucontrol*
En este punto, no hay audio, necesitamos
**[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**.
Recomandamos instalar un programa gráfico para manejar el audio como
**[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**, porque todavía no tenemos atajos de teclado para ello.

```bash
sudo pacman -S pulseaudio pavucontrol
```

En Arch,
[pulseaudio está activado por defecto](https://wiki.archlinux.org/index.php/PulseAudio#Running), pero puede que tengáis que reiniciar para que *pulseaudio* arranque. Después de reiniciar, abrid *pavucontrol* usando *rofi*, activad el audio, ya que por defecto está silenciado, y debería estar todo correcto.

Ahora podéis establecer atajos de teclado para *pulseaudio*. Abrid el archivo de configuración de Qtile y añadid lo siguiente:


```python
# Volumen
Key([], "XF86AudioLowerVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ -5%"
)),
Key([], "XF86AudioRaiseVolume", lazy.spawn(
    "pactl set-sink-volume @DEFAULT_SINK@ +5%"
)),
Key([], "XF86AudioMute", lazy.spawn(
    "pactl set-sink-mute @DEFAULT_SINK@ toggle"
)),
```

Aunque para una mejor experiencia en la línea de comandos, recomendamos usar
**[pamixer](https://www.archlinux.org/packages/community/x86_64/pamixer/)** (En nuestro caso no lo hemos instalado):

```bash
sudo pacman -S pamixer
```

Con ello puedes convertir los atajos de teclado en:

```python
# Volumen
Key([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
Key([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
Key([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
```

Reiniciad Qtile con **Mod + Ctrl + R** y probad los atajos.

### Brillo - *brightnessctl*
Si estáis en un portátil, probablemente también necesitéis controlar el brillo de vuestra pantalla, para ello recomendamos
**[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**:

```bash
sudo pacman -S brightnessctl
```

Podéis añadir estos atajos y volver a reiniciar Qtile:

```python
# Brillo
Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
```

### Monitores - *xrandr* y *arandr*
Si tenéis múltiples monitores, seguramente queráis usarlos todos. Así es como funciona **[xrandr](https://wiki.archlinux.org/index.php/Xrandr)**:

```bash
# Lista todas las salidas y resoluciones disponibles
xrandr

# Formato común para un portátil con monitor extra
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0
```

Es necesario especificar la posición de cada salida, si no se utilizará 0x0, y todas las salidas estarán solapadas. Ahora bien, si no queréis calcular píxeles necesitáis una interfaz gráfica como
**[arandr](https://www.archlinux.org/packages/community/any/arandr/)**:

```bash
sudo pacman -S arandr
```

Abridla con *rofi*, ordenad las pantallas como queráis, y después podéis guardar la disposición de las mismas, lo cual simplemente os dará un script con el comando exacto de *xrandr* que necesitáis. Guardad ese script, pero todavía no le deis al botón de aplicar.

Para un sistema con múltiples monitores deberíais crear una instancia de *Screen* por cada uno de ellos en la configuración de Qtile.

Encontraréis una lista llamada *screens* en la configuración de Qtile que contiene solo un objeto inicializado con una barra en la parte de abajo.

Dentro de esa barra podéis ver los widgets con los que viene por defecto:

Añadid tantas pantallas como necesiteis y copia-pegad los widgets, más adelante podréis personalizarlos. Ahora podéis volver a *arandr*, darle click en "apply". Finalmente, reiniciad el gestor de ventanas.

### Almacenamiento - *udiskie*
Otra utilidad básica que podríais necesitar es montar de forma automática unidades de almacenamiento externas. Para ello usamos
**[udisks](https://wiki.archlinux.org/index.php/Udisks)**
y **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**. *udisks* es una dependencia de *udiskie*, así que solo instalaremos este último. Instalad también el paquete
**[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**
para leer y escribir en discos NTFS:

```bash
sudo pacman -S udiskie ntfs-3g
```

### Redes - *nm-applet*
Hemos configurado la red a través de *NetworkManager*, pero un programa gráfico es más cómodo. Nosotros usamos
**[nm-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**:

```bash
sudo pacman -S network-manager-applet
```

### Systrays - *udiskie*, *nm-applet*, *volumeicon* y *cbatticon*
Por defecto, tenemos una "bandeja del sistema" en Qtile, pero no hay nada ejecutándose en ella. Podéis lanzar los programas que acabamos de instalar así:

```bash
udiskie -t &
nm-applet &
```

Ahora deberíais ver unos iconos en la barra. Podéis interactuar con ellos para configurar la red, los discos... Podéis instalar también iconos para la batería y el volumen:

```bash
sudo pacman -S volumeicon cbatticon
volumeicon &
cbatticon &
```

Haciendolo de esta manera deberías de ejecutar esos comandos cada vez que inicies el sistema. En [.xprofile](#.xprofile) explicaremos la automatización de esto.

### Notificaciones - *libnotify*
Nos gusta tener notificaciones en el escritorio también, para ello tenéis que instalar [**libnotify**](https://wiki.archlinux.org/index.php/Desktop_notifications#Libnotify) y [**notification-daemon**](https://www.archlinux.org/packages/community/x86_64/notification-daemon/):

```bash
sudo pacman -S libnotify notification-daemon
```

En nuestro caso, [esto es lo que tenemos que hacer para tener notificaciones](https://wiki.archlinux.org/index.php/Desktop_notifications#Standalone):

```bash
# Crea este fichero con nano o vim
sudo nano /usr/share/dbus-1/services/org.freedesktop.Notifications.service

# Pega estas líneas
[D-BUS Service]
Name=org.freedesktop.Notifications
Exec=/usr/lib/notification-daemon-1.0/notification-daemon
```

Probadlo:

```bash
notification-send "Hola Mundo"
```

### Explorador de Archivos - *thunar* y *ranger*
Hasta ahora siempre hemos manejado los ficheros a través de la terminal, pero podéis instalar un explorador de archivos. Para uno gráfico, recomendamos **[thunar](https://wiki.archlinux.org/index.php/Thunar)**, y para uno basado en terminal, **[ranger](https://wiki.archlinux.org/index.php/Ranger)**.

```bash
sudo pacman -S thunar ranger
```

### Basura - *glib2* y *gvfs*
Si no queréis usar *rm* constantemente y arriesgaros a perder ficheros,
necesitáis un sistema de basura. Por suerte, es bastante sencillo de hacer [usando alguna de estas herramientas](https://wiki.archlinux.org/index.php/Trash_management#Trash_creation)
como **[glib2](https://www.archlinux.org/packages/core/x86_64/glib2/)**, y para interfaces gráficas como *thunar* necesitais **[gvfs](https://www.archlinux.org/packages/extra/x86_64/gvfs/)**:

```bash
sudo pacman -S glib2 gvfs

# Uso
gio trash path/to/file

# Vaciar papelera
gio trash --empty
```

Con *thunar* podéis abrir la basura desde el panel izquierdo, pero desde la línea de comandos podéis hacer:

```bash
ls ~/.local/share/Trash/files
```

### Compositor de Imágen - *picom*
Finalmente, si queréis transparencia y demás (Tanto en GTK como en terminal) instala un compositor:

```bash
sudo pacman -S picom
# Pon esto en ~/.xprofile
picom &
```

### Multimedia
Consultad [esta página](https://wiki.archlinux.org/index.php/List_of_applications/Multimedia) para ver la variedad de programas multimedia disponibles.

#### Imágenes
Para ver imágenes, tenemos [imv](https://archlinux.org/packages/extra/x86_64/imv/):

```bash
sudo pacman -S imv
```

#### Vídeo y audio
Aquí sin duda el clásico [vlc](https://wiki.archlinux.org/index.php/VLC_media_player_(Espa%C3%B1ol)) es lo que necesitamos:

```bash
sudo pacman -S vlc
```

### Actualizaciones
Instalaremos un maquete que incluye mejoras para pacman, [pacman-contrib](https://archlinux.org/packages/extra/x86_64/pacman-contrib/)

```bash
sudo pacman -S pacman-contrib
```

### Otras Dependencias
En caso de que useis nuestra configuración, tenemos varios scripts personalizados para cambiar los temas de Qtile y Alacritty.

Necesitaremos instalar las siguientes dependencias:

```bash
sudo pacman -S python3 python3-pip xdotool python-colorama
```

Estas dependencias son necesarias para los scripts que hemos creado para cambiar los temas de Qtile y Alacritty:

- [Explicación del Script para los Temas de Qtile](https://github.com/MarioCuenca22/Sintesis-M12/blob/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/qtile/README.md)
- [Explicación del Script para los Temas de Alacritty](https://github.com/MarioCuenca22/Sintesis-M12/blob/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/alacritty/README.md)


## Temas

### GTK
Ahora, vamos a instalar un tema oscuro para GTK. Nosotros usamos *Material Black Colors*, podéis descargar una versión [aquí](https://www.gnome-look.org/p/1316887/), con sus respectivos iconos
[aquí](https://www.pling.com/p/1333360/).

Sugerimos empezar con *Material-Black-Blueberry* y *Material-Black-Blueberry-Suru*. Podéis encontrar otros temas para GTK
[en esta página](https://www.gnome-look.org/browse/cat/135/).

Una vez tengais descargados los temas, podéis hacer esto:

```bash
# Asumiendo que habéis descargado Material-Black-Blueberry
cd Downloads/
sudo pacman -S unzip
unzip Material-Black-Blueberry.zip
unzip Material-Black-Blueberry-Suru.zip
rm Material-Black*.zip

# Haced vuestro tema visible a GTK
sudo mv Material-Black-Blueberry /usr/share/themes
sudo mv Material-Black-Blueberry-Suru /usr/share/icons
```

Ahora editad **~/.gtkrc-2.0** y **~/.config/gtk-3.0/settings.ini** añdiendo estas líneas:

```ini
# ~/.gtkrc-2.0
gtk-theme-name = "Material-Black-Blueberry"
gtk-icon-theme-name = "Material-Black-Blueberry-Suru"

# ~/.config/gtk-3.0/settings.ini
gtk-theme-name = Material-Black-Blueberry
gtk-icon-theme-name = Material-Black-Blueberry-Suru
```

La próxima vez que inicieis sesión veréis los cambios aplicados. Podéis instalar también un tema de cursor distinto, para ello necesitais **[xcb-util-cursor](https://www.archlinux.org/packages/extra/x86_64/xcb-util-cursor/)**. El tema que usamos es
[Breeze](https://www.gnome-look.org/p/999927/):

```bash
sudo pacman -S xcb-util-cursor
cd Downloads/
tar -xf Breeze.tar.gz
sudo mv Breeze /usr/share/icons
```

Editad **/usr/share/icons/default/index.theme** añadiendo esto:

```ini
[Icon Theme]
Inherits = Breeze
```

Ahora volved a editar **~/.gtkrc-2.0** y **~/.config/gtk-3.0/settings.ini**:

```ini
# ~/.gtkrc-2.0
gtk-cursor-theme-name = "Breeze"

# ~/.config/gtk-3.0/settings.ini
gtk-cursor-theme-name = Breeze
```

Aseguraos de escribir bien los nombres de los temas e iconos, deben ser
exactamente los nombres de los directorios donde se encuentran, los que
ofrece esta salida:

```bash
ls /usr/share/themes
ls /usr/share/icons
```

Recordad que solo veréis los cambios si iniciais sesión de nuevo.

### lightdm
También podemos cambiar el tema de *lightdm* para que mole más, ¿por qué no? Necesitamos otro *greeter* y algún tema, en concreto
**[lightdm-webkit2-greeter](https://www.archlinux.org/packages/community/x86_64/lightdm-webkit2-greeter/)** y **[lightdm-webkit-theme-aether](https://aur.archlinux.org/packages/lightdm-webkit-theme-aether/)**:

```bash
sudo pacman -S lightdm-webkit2-greeter
yay -S lightdm-webkit-theme-aether
```

Estas son las configuraciones que tenéis que hacer:

```ini
# /etc/lightdm/lightdm.conf
[Seat:*]
# ...
# Descomenta esta línea y pon este valor
greeter-session = lightdm-webkit2-greeter
# ...

# /etc/lightdm/lightdm-webkit2-greeter.conf
[greeter]
# ...
webkit_theme = lightdm-webkit-theme-aether
```


## .bashrc
Hemos modificado el archivo .bashrc para incluir dos comandos para ejecutar el Script python para cambiar los temas de Qtile y Alacritty. Esto lo conseguimos añadiendo un alias con el nombre del comando, y que será lo que ejecutará. 

En nuestro caso, el comando para cambiar el tema de Qtile se llama **change-qtile-theme**, que ejecuta la ubicación de *python3* para abrir con python la ruta script. La línea quedaría así:

```bash
alias change-qtile-theme="/usr/bin/python3 /home/admin/.config/qtile/scripts/change_theme.py"
```

La línea del comando para cambiar el tema de Alacritty es la siguiente (El nombre del comando es **change-term-theme**):

```bash
alias change-term-theme="/usr/bin/python3 /home/admin/.config/alacritty/scripts/change_theme.py"
```

FInalmente, hemos modificado la información y colores del promp. Cambiaremos la línea **export PS1** de la siguiente manera

```bash
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]$ '
```

Podéis importaros nuestro archivo [.bashrc](https://github.com/MarioCuenca22/Sintesis-M12/blob/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.bashrc)

## .xprofile
El archivo [.xprofile](https://wiki.archlinux.org/title/xprofile) nos permite ejecutar comandos al iniciar el sistema, por lo que nos puede venir bien para dejar programas en ejecución, como los Systrays, una vez arranque el sistema.

Para ello necesitaremos descargar xorg:

```bash
sudo pacman -S xorg-xinit
```

Una vez instalado, modificaremos el archivo **.xprofile** y añadiremos el siguiente contenido:

```bash
setxkbmap es &
feh --bg-scale ~/.config/Wallpapers/wallpaper2.jpg &
picom &
volumeicon &
export PATH=$HOME/.local/bin:$PATH
```

Podéis remplazar vuestro archivo por nuestro [.xprofile](https://github.com/MarioCuenca22/Sintesis-M12/blob/2564693f26f3bdd190c58e985953673b5ab5debd/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.xprofile)


## Atajos de Teclado

### Ventanas
| **Atajo**                   | **Acción**                                       |
| ----------------------- | -------------------------------------------- |
| **Mod + J**             | Siguiente Ventana                            |
| **Mod + K**             | Anterior Ventana                               |
| **Mod + Shift + H**     | Aumentar Master                              |
| **Mod + Shift + L**     | Decrementar Master                           |
| **Mod + Shift + J**     | Mover Ventana abajo                          |
| **Mod + Shift + K**     | Mover Ventana arriba                         |
| **Mod + Shift + F**     | Pasar Ventana a Flotante                     |
| **Mod + Shift + F**     | Pasar Ventana a Flotante                     |
| **Mod + Tab**           | Cambiar la Disposición de Ventanas       |
| **mod + [1-9]**         | Cambiar al Espacio de Trabajo N (1-9)        |
| **Mod + Shift + [1-9]** | Mover Ventana al Espacio de Trabajo N (1-9) |
| **Mod + .**         | Enfocar Siguiente Monitor                    |
| **Mod + ,**          | Enfocar Previo Monitor                       |
| **Mod + W**             | Cerrar Ventana                               |
| **Mod + Ctrl + R**      | Reiniciar Gestor de Ventanas                  |
| **Mod + Ctrl + Q**      | Cerrar Sesión                                |

### Aplicaciones y Utilidades
Los siguientes atajos de teclado funcionarán solo si instalas los programas que lanzan:

```bash
sudo pacman -S rofi thunar firefox alacritty redshift scrot
```

| **Atajo**               | **Acción**                                 |
| ------------------- | -------------------------------------- |
| **Mod + M**         | Lanzar Menú de Aplicaciones (Rofi)                            |
| **Mod + Shift + M** | Lanzar Menú de Navegación de Ventanas (Rofi)                      |
| **Mod + B**         | Lanzar Navegador (Firefox)            |
| **Mod + E**         | Lanzar Explorador de Archivos (Thunar) |
| **Mod + Return**    | Lanzar Terminal (Alacritty)            |
| **Mod + R**         | Lanzar Redshift                               |
| **Mod + Shift + R** | Parar Redshift                         |
| **Mod + S**         | Lanzar Capturas de Pantalla (Scrot)            |

## Software Instalado

### Utilidades Básicas y de Sistema
| **Software**                                                                                            | **Utilidad**                                      |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------- |
| **[networkmanager](https://wiki.archlinux.org/index.php/NetworkManager)**                           | Servicio de Redes                               |
| **[network-manager-applet](https://wiki.archlinux.org/index.php/NetworkManager#nm-applet)**         | Bandeja del Sistema (Systray) para *NetworkManager*                      |
| **[pulseaudio](https://wiki.archlinux.org/index.php/PulseAudio)**                                   | Servicio de Audio                               |
| **[pavucontrol](https://www.archlinux.org/packages/extra/x86_64/pavucontrol/)**                     | GUI de *pulseaudio*                              |
| **[pamixer](https://www.archlinux.org/packages/community/x86_64/pamixer/)**                         | CLI de *pulseaudio*                             |
| **[brightnessctl](https://www.archlinux.org/packages/community/x86_64/brightnessctl/)**             | Gestor de Brillo (Portátil)                        |
| **[xorg-xinit](https://wiki.archlinux.org/index.php/Xinit)**                                             | Script de Inicio para *Xorg* |
| **[libnotify](https://wiki.archlinux.org/index.php/Desktop_notifications)**                         | Notificaciones de Escritorio                  |
| **[notification-daemon](https://www.archlinux.org/packages/community/x86_64/notification-daemon/)** | Dependencia de *libnotify*                               |
| **[udiskie](https://www.archlinux.org/packages/community/any/udiskie/)**                            | Montar Unidades Automáticamente                 |
| **[ntfs-3g](https://wiki.archlinux.org/index.php/NTFS-3G)**                                         | Leer y Escribir Unidades NTFS                          |
| **[arandr](https://www.archlinux.org/packages/community/any/arandr/)**                              | GUI de *xrandr*                             |
| **[cbatticon](https://www.archlinux.org/packages/community/x86_64/cbatticon/)**                     | Bandeja del Sistema (Systray) para la Batería                       |
| **[volumeicon](https://www.archlinux.org/packages/community/x86_64/volumeicon/)**                   | Bandeja del Sistema (Systray) para el Volumen                       |
| **[glib2](https://www.archlinux.org/packages/core/x86_64/glib2/)**                                  | Basura                                        |
| **[gvfs](https://www.archlinux.org/packages/extra/x86_64/gvfs/)**                                   | Basura para GUIs                              |
| **[pcmanfm](https://wiki.archlinux.org/title/PCManFM)** |                             |
| **[xdotool](https://man.archlinux.org/man/xdotool.1.en)** | Simulador de Entradas de Teclado                            |
| **[python-colorama](https://archlinux.org/packages/extra/any/python-colorama/)** |                             |

### Fuentes y Temas
| **Software**                                                                               | **Utilidad**                               |
| -------------------------------------------------------------------------------------- | -------------------------------------- |
| **[Picom](https://wiki.archlinux.org/index.php/Picom)**                                | Compositor para Xorg                   |
| **[UbuntuMono Nerd Font](https://aur.archlinux.org/packages/nerd-fonts-ubuntu-mono/)** | Fuente Nerd Font                 |
| **[Material Black](https://www.gnome-look.org/p/1316887/)**                            | Tema e Iconos para GTK (Thunar)                |
| **[feh](https://wiki.archlinux.org/index.php/Feh)**                                    | CLI para establecer fondos de pantalla |

### Aplicaciones y Utilidades
| **Software**                                                              | **Utilidad**                           |
| --------------------------------------------------------------------- | ---------------------------------- |
| **[alacritty](https://wiki.archlinux.org/index.php/Alacritty)**       | Emulador de Terminal               |
| **[thunar](https://wiki.archlinux.org/index.php/Thunar)**             | Gestor de Archivos Gráfico         |
| **[ranger](https://wiki.archlinux.org/index.php/Ranger)**             | Gestor de Archivos de Terminal     |
| **[neovim](https://wiki.archlinux.org/index.php/Neovim)**             | Editor de Texto Basado en Terminal |
| **[rofi](https://wiki.archlinux.org/index.php/Rofi)**                 | Menú y Navegación                  |
| **[scrot](https://wiki.archlinux.org/index.php/Screen_capture)**      | Captura de Pantalla                |
| **[redshift](https://wiki.archlinux.org/index.php/Redshift)**         | Cuida tus Ojos                     |
| **[trayer](https://www.archlinux.org/packages/extra/x86_64/trayer/)** | Systray                            |