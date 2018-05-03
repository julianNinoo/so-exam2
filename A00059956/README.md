**Curso:** Sistemas Operativos  
**Estudiante:** Victor Andres Calambas  
**Codigo:** A00059956  
**Correo:** victor.1818@hotmail.es 

**Instalación y configuracion de Oh-My-Zsh  **
Se hace la instalacion de oh-my-Zsh  y tambien el de Curl con los siguientes comandos  
		"apt-get install zsh"  
		"apt-get install curl"  
    Luego corremos la siguiente linea de codigo  
		"sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" "  
Procedemos a realizar la clonacion del repositorio del examen con nombre SO-exam2 y desde el git ingresamos al prefil, configuracion avanzada, y seleccionamos crear token para poder utilizarlo antes del @ del siguiente codigo:  
git config remote.origin.url "https://"TOKEN"@github.com/JnCV17/so-exam2.git"
Luego se procede a realizar la configuracion para poder utilizar las abreviaciones de git como  
ga, gaa  
Luego se realizo la ejecucion la siguiente linea para poder instalar el plugin que nos permite la funcionalidad del autocompletado, el codigo que se uso fue:  
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
Luego para poder resaltar en amarillo el autocompletado se utuilizo el comando que sigue:  
 vi ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh  
  export ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='yellow'
luego se adiciona a la lista de plugins la configuracion de los plugins para que funcione, se realiza de esta forma :   
plugins=(git vi-mode zsh-autosuggestions)  

---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---  

**Instalación de TMUX**  
Se procede a instalar TMUX de la siguiente forma.Primero se ejecuta la siguiente linea de comando:  
 apt-get install tmux  
Luego se puede procede a realizar la configuracion del archivo tmux para poder utilizar los comandos del repositorio que se encuentran en:  https://github.com/ICESI/so-processes/tree/master/03_tmux  
Con esta configuración realizada las abreviaturas ctrl+b por el coando ctrl+a visto en clase, lo cual me permite que las teclas estén más cercanos, para poder realizar eso debemos modificar en el archivo tmux.conf de las siguiente forma:

*# use C-a, since it's on the home row and easier to hit than C-b*
set-option -g prefix C-a  
unbind-key C-a  
bind-key C-a send-prefix  
set -g base-index 1  

*# Easy config reload*  
bind-key R source-file ~/.tmux.conf \; display-message "tmux.conf reloaded."  

*# vi is good*  
setw -g mode-keys vi  

*# Setup 'v' to begin selection as in Vim*  
bind-key -Tcopy-mode-vi v send -X begin-selection   

---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---

Luego de haber instalado TMux se creo la sesion con nombre so-exam2.  
Se procedío a dividir la pantalla en cuatro cuadrantes, en las cuales se muestra lo siguiente:  
1. Salida del comando top  
2. Salida de la ejecución del script de python courses.py 
3. Peticiones por medio de curl a cada endpoint. Salida formateada con jq
4. Salida de la ejecución de telnet towel.blinkenlights.nl

La captura de la ejecución de las funcionalidades al tiempo es la siguiente  
 ----<<<AQUI VA LA PANTALLA DE LAS 4 FUNCIONALIDADES>>>----


---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---o---0---  

*Punto 6 obtener los datos de procesador, memoria y disco disponibles* 
Se hace la instalacion del python-pip para luego proceder a realizar la instalación del pyCLI, psutil,y del slack client de python, para ello se ejecutan los siguientes comandos:  

pip install pyCLI  
pip install psutil==4.3.0  
pip install slackclient  

Luego se procede a crear un archivo de extencion python ".py" el cual fue llamado estadoPC.py y aqui vamos a importar lo que acabamos de instalar y adicional a ello vamos a llamar los metodos existentes de la libreria psutil que se encuentran en el siguiente link: https://pypi.python.org/pypi/psutil/4.3.0 aquí estan los comandos utilizados para obtener los datos del procesador, memoria y disco los cuales  

Ejecutamos la siguiente linea para entrar a la configuración del crontab  
crontab -e   
Aqui agregamos al final la linea que indica la frecuencia en minutos en que se va a actualizar los datos del procesador, memoria y disco

*/1 * * * * /home/chimbi/so-exam2/A00059956/estadoPC/estadoPC.py

Con  esta configuración terminada procedemos a ejecutar el archivo de python con el comando  
python estadoPC.py   
Con la ejecución de el archivo python se envia al canal de Slack creado cada minuto los datos del procesador, memoria y disco. Las imagenes que muestran el codigo del archivo estadoPC.py y el resultado de cada minuto obteniendo los datos desde el slack se ven acontinuación:


