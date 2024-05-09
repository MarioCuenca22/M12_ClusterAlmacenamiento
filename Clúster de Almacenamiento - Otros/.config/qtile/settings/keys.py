# Configuración de atajos con telcado (Keybinds)

from libqtile.config import Key
from libqtile.command import lazy


mod = "mod4"

keys = [Key(key[0], key[1], *key[2:]) for key in [
    # ------------ Ventanas y otros --------------

    # Cambiar entre ventanas en el espacio actual
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),

    # Cambiar entre ventanas (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Activar o desactivar flotabilidad
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Mover entre ventanas actuales
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Cambiar entre los diferentes layouts
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Cerrar ventana
    ([mod], "w", lazy.window.kill()),

    # Cambiar el foco entre monitores
    ([mod], "period", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Reiniciar Qtile
    ([mod, "control"], "r", lazy.restart()),

    ([mod, "control"], "q", lazy.shutdown()),
    ([mod], "r", lazy.spawncmd()),

    # ------------ Aplicaciones ------------

    # Menu Apps
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Navegar entre ventanas
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Firefox
    ([mod], "b", lazy.spawn("firefox")),

    # Explorador de archivos
    ([mod], "e", lazy.spawn("pcmanfm")),

    # Terminal
    ([mod], "Return", lazy.spawn("alacritty")),

    # Visual Studio
    ([mod], "v", lazy.spawn("code")),

    # Redshift
    ([mod], "r", lazy.spawn("redshift -O 2400")),
    ([mod, "shift"], "r", lazy.spawn("redshift -x")),

    # Captura de pantalla
    ([mod], "s", lazy.spawn("scrot -s")),
    ([mod, "shift"], "s", lazy.spawn("scrot")),

    # ------------ Hardware y sonido --------------

    # Volumen
    ([], "XF86AudioLowerVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ -5%"
    )),
    ([], "XF86AudioRaiseVolume", lazy.spawn(
        "pactl set-sink-volume @DEFAULT_SINK@ +5%"
    )),
    ([], "XF86AudioMute", lazy.spawn(
        "pactl set-sink-mute @DEFAULT_SINK@ toggle"
    )),

    # Brillo
    ([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl set +10%")),
    ([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl set 10%-")),
]]
