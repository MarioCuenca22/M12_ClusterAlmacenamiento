# Qtile espacios

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys


# Iconos: 
# nf-fa-firefox, 
# nf-fae-python, 
# nf-dev-terminal, 
# nf-fa-code, 
# nf-oct-git_merge, 


groups = [Group(i) for i in [
    "   ", "   ", "   ", "   ", "  ", "   ",
]]

for i, group in enumerate(groups):
    actual_key = str(i + 1)
    keys.extend([
        Key([mod], actual_key, lazy.group[group.name].toscreen()),
        Key([mod, "shift"], actual_key, lazy.window.togroup(group.name))
    ])
