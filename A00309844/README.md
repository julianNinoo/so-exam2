# Segundo Parcial
 
**Nombre:** David Felipe Cobo Plazas

**Código:** A00309844

**URL repositorio:** https://github.com/davidcobogithub/so-exam2.git 

**Tabla de Contenido**

  - [1. Instalación de zsh]
  - [2. Instalación del plugin zsh-autosuggestions]
  - [3. Instalación y configuración de tmux]
  - [4. Instalación de git y tig]
  - [5. Exportación de la máquina virtual]
  - [6. Importación de la máquina virtual]
  - [7. Cuadro comparativo entre Debian 9 y CentOS7]
 
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
vi ~/.zshrc
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
vi ~/.zshrc
```

```
plugins=(git vi-mode)
```

```
$ source ~/.zshrc
```

**3.** Para cambiar el color de resaltado de las coincidencias a amarillo, se deben ejecutar los comandos, que en mi caso son

```
vi $ZSH_CUSTOM/davidcobo.zsh
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

**1.** 
