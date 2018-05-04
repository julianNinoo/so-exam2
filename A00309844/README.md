# Segundo Parcial
 
**Nombre:** David Felipe Cobo Plazas

**Código:** A00309844

**URL repositorio:** https://github.com/davidcobogithub/so-exam2.git 

**Tabla de Contenido**

  - [1. Instalación de zsh](#1.-Instalación-de-zsh)
  - [2. Instalación del plugin zsh-autosuggestions](#2.-Instalación-del-plugin-zsh-autosuggestions)
  - [3. Instalación y configuración de tmux](#3.-Instalación-y-configuración-de-tmux)
  - [4. Creación de una sesión con tmux](#4.-Creación-de-una-sesión-con-tmux)
  - [5. Aplicación.py](#5.-Aplicación.py)
 
# Solución Parcial 2

##  1. Instalación de zsh

**1.** Se escribe el siguiente comando ```apt-get install zsh -y```

**2.** Para instalar los plugins de oh-my-zsh se debe ejecutar el comando 

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

**3.** Nota: Si no tiene instalado curl, debe instalarse. También funciona con el comando 

```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | zsh
```

**4.** Para habilitar el plugin vi-mode se deben realizar los comandos: 

```
nano ~/.zshrc
```

```
plugins=(git vi-mode)
```

```
$ source ~/.zshrc
```

**5.** Para configurar el token se debe clonar el repositorio. en mi caso el comando es 

```
git clone https://github.com/davidcobogithub/so-exam2.git
```

**6.** Configure el token como medio de autenticación a GitHub con el comando 

```
git config remote.origin.url "https://topSecretToken@github.com/davidcobogithub/so-exam2.git"
```

**7.** Ahora, algunas capturas de pantalla mostrando el uso de los alias gaa, gcmsg y ggp para el envío de un commit:

![](imagenes/d3.jpg)

##  2. Instalación del plugin zsh-autosuggestions

**1.** Se debe clonar el repositorio en el directorio de plugins de oh-my-zsh con el comando

```
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

**2.** Adicionar el plugin a la lista de plugins activos con los comandos

```
nano ~/.zshrc
```

```
plugins=(git vi-mode)
```

```
$ source ~/.zshrc
```

**3.** Para cambiar el color de resaltado de las coincidencias a amarillo, se deben ejecutar los comandos, que en mi caso son

```
nano $ZSH_CUSTOM/davidcobo.zsh
```

```
export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE="fg=yellow"
```

```
$ source ~/.zshrc
```

**4.** Algunas capturas de pantalla con el autocompletado de dos comandos

![](imagenes/1.jpg)

![](imagenes/2.jpg)

##  3. Instalación y configuración de tmux

**1.** Se debe ejecutar el comando ```sudo apt-get install tmux -y```

**2.** Para realizar una configuración personalizada se debe ejecutar una acción a través de un archivo de configuración llamado .tmux.conf. Se digita el comando ``` nano ~/.tmux.conf ```

**3.** Una vez dentro del archivo se agrega la siguiente configuración:

```
set-option -g prefix C-a
unbind-key C-a
bind-key C-a send-prefix
set -g base-index 1

# Easy config reload
bind-key R source-file ~/.tmux.conf \; display-message "tmux.conf reloaded."

# vi is good
setw -g mode-keys vi

# Setup 'v' to begin selection as in Vim
bind-key -Tcopy-mode-vi v send -X begin-selection
```

**4.** Modo vi para la navegación y modo de copia visual a portapapeles

![](imagenes/d4.jpg)

![](imagenes/d5.jpg)

![](imagenes/d6.jpg)

##  4. Creación de una sesión con tmux 

**1.** Se debe ejecutar el siguiente comando ``` tmux new-session -s so-exam2 ```

**2.** Una vez creada la sesión, para dividir la pantalla en cuatro cuadrantes, se deben combinar las siguientes teclas

```
Ctrl + a + %   -> Divide la pantalla verticalmente
```

```
Ctrl + a + "   -> Divide la pantalla horizontalmente
```

**3.** En el primer cuadrante ejecutar el comando ``` top ```

**4.** Para ejecutar el script de python courses.py es necesario tener importado el modulo Flask. En caso de no tenerlo instalado los siguientes enlaces lo orientará en la instalación

https://github.com/ICESI/so-microservices-python/tree/master/01_virtualenvs

https://github.com/ICESI/so-microservices-python/tree/master/02_intro_flask

Salida en el navegador al ejecutar el programa courses.py

![](imagenes/d7.jpg)

**5.** Para realizar las peticiones por medio de curl con la salida formateada con jq, debe asegurarse de tener instalado jq. En caso de no tenerlo puede instalarlo con el siguiente comando

```
sudo apt-get install jq
```

**6.** Finalmente, ejecutar el comando ``` telnet towel.blinkenlights.nl ```

**7.** Aqui una imagen de los cuatro cuadrantes

![](imagenes/d8.jpg)

##  5. Aplicación.py

**1.** 
