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


----<<<AQUI VA LA PANTALLA DE LAS 4 FUNCIONALIDADES>>>----
