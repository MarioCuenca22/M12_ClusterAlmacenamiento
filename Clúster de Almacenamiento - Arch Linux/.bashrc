#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
alias change-qtile-theme="/usr/bin/python3 /home/admin/.config/qtile/scripts/change_theme.py"
alias change-term-theme="/usr/bin/python3 /home/admin/.config/alacritty/scripts/change_theme.py"
export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[00m\]$ '

#export PS1='\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\W\[\033[33m\]$'
#(__git_ps1 "(%s)")\[\033[37m\]\$\[\033[00m\]
