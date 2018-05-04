# Examen Parcial 2 

**Nombre:** Cristian Osorio Trejos  
**Código:** A00056436  
**URL:** [https://github.com/crisosotre/so-exam2/blob/crisosotre/so-exam2/A00056436/README.md](https://github.com/crisosotre/so-exam2/blob/crisosotre/so-exam2/A00056436/README.md)

## Descripción:

El segundo parcial del curso sistemas operativos trata sobre el empleo de comandos de Linux, la instalación y configuración de herramientas y la automatización de tareas.

Este documento será subido al siguiente repositorio: [https://github.com/ICESI-Training/so-exam2](https://github.com/ICESI-Training/so-exam2)

## **Instalación de zsh y git**

Para realizar la instalación de zsh y de git es necesario ingresar como usuario **root** en nuestra maquina virtual. Seguido de eso
ejecutamos el comando ```apt-get install zsh``` para instalar zsh y luego ejecutamos el comando ```apt-get install git``` para instalar git. Este procedimiento se muestra en la siguiente imagen.

![Instalar zsh y git](img/installzshygit.png)
En mi caso zsh y git ya estaban instalados anteriormente.

### **Instalación de oh-my-zsh**

Para realizar la instalacion de oh-my-zsh es necesario instalar **curl** para poder instalarlo.

1) Ejecutamos el comando ```apt-get install curl``` como se muestra en la imagen. En mi caso, ya lo tengo instalado

![](img/installcurl.png)

2) Luego ejecutamos el comando ```sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"``` para instalar oh-my-zsh como usuario root.

![](img/oh-my-zsh.png)

3) Para que oh-my-zsh lo puedan utilizar todos los usuarios, ejecutamos el comando ```export ZSH="$HOME/.dotfiles/oh-my-zsh"; sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"```.  Ya con esto, todos los usuarios pueden utilizar esta herramienta.

![](img/oh-my-zsh-todos-usuarios.png)

4) Creamos un token para nuestro repositorio de git siguiendo el tutorial:  [https://github.com/ICESI/so-git/tree/master/00_github_intro](https://github.com/ICESI/so-git/tree/master/00_github_intro). Siguiendo el tutorial, primero clonamos el repositorio con  el comando ```git clone```, después configuramos el repositorio con el token generado con el comando ```git config remote.origin.url https://xxxxxxxxxxxxxxxxxxxx@github.com/DonMiguelin/so-exam2.git``` en  XXXXXXXXXXXX ponemos el toquen que generamos.

5) Para realizar el literal 4, fue necesario crear un directorio en el repositorio clonado con el comando ```mkdir``` y ponerle como nombre **codigo_punto6**, en este directorio cree un archivo **README.md** y lo subi a mi repositorio ejecutando los comandos ```gaa``` que es git add all, ```gcmsg``` git commit -m y ```ggp``` git push origin.

![](img/tokenmascomandos.png)


## instalar los plugins necesarios de oh-my-zsh


