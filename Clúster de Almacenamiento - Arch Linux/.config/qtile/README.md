# Configuración de Qtile

acordarse de chmod u+x autostart.sh

## Script
Hemos creado un script que nos permite automatizar la selección de temas. Lo que hace el script es recorrer el [directorio de temas](https://github.com/MarioCuenca22/Sintesis-M12/tree/b9f46349dba16b764cce773e10d03897499fa5c4/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/alacritty/themes) y guardarlos en un diccionario, con un número como Identificador y el nombre. Finalmente nos lista las posibilidades, y una vez escogido el número del tema que queremos, cambia la primera línea del [archivo de configuración](https://github.com/MarioCuenca22/Sintesis-M12/blob/b9f46349dba16b764cce773e10d03897499fa5c4/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.config/alacritty/alacritty.toml), que es donde importamos el tema, y lo aplica automáticamente.

Para que funcione, necesitamos instalar python, pip y colorama (Está explicado en la [guía de configuración de Arch](https://github.com/MarioCuenca22/Sintesis-M12/blob/b9f46349dba16b764cce773e10d03897499fa5c4/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/README.md))

```bash
sudo pacman -S python3 python3-pip python-colorama
```

Además, para evitar tener que escribir **python3 /home/admin/.config/alacritty/scripts/change-theme.py**, crearemos un alias en el archivo [.bashrc](https://github.com/MarioCuenca22/Sintesis-M12/blob/b9f46349dba16b764cce773e10d03897499fa5c4/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/.bashrc) (Está explicado en la [guía de configuración de Arch](https://github.com/MarioCuenca22/Sintesis-M12/blob/b9f46349dba16b764cce773e10d03897499fa5c4/Cl%C3%BAster%20de%20Almacenamiento%20-%20Arch%20Linux/README.md))

```bash
alias change-term-theme="/usr/bin/python3 /home/admin/.config/alacritty/scripts/change_theme.py"
```

Ahora, simplemente nos bastará con reinciar, y una vez el sistema vuelva a estar encendido, probaremos lo siguente:

```bash
change-term-theme
```
