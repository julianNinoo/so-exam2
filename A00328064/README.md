# Segundo Examen parcial de Sistemas Operativos 

**Nombre:** Cristian Alejandro Morales Lopez

**Codigo** A00328064

 Todo esta almacenada en la Rama cam/so-exam1 ([URL del fork desde camtelematica](https://github.com/camtelematica/so-exam2.git))
 
Para la realizacion de este parcial se instalaron los siguientes programas y librerias de python

Programas

* tmux
* zsh
* python
* asciinema
* pip

Librerias

* flask
* pyCLI psutil
* Slackclient

A continuacion se muestran capturas de pantalla con todos los programas anteriores instalados.

![](/A00328064/imagenes/instalaciones1.png)

![](/A00328064/imagenes/instalaciones2.png)

***1 PUNTO UTILIZACION DE COMANDOS DE GIT***

una vez instalada la shell zsh se ejecutaron los comandos gaa, gcmsg, ggp a continuacion se muestra captura de pantalla con los comando anteriormente mencionados

![](/A00328064/imagenes/gaa.png)


***2 CONFIGURACION DEL PLUGIN AUTOSUGESTION DE LA SHELL ZSH***

se configuro el plugin de Autosugestion de la shell zsh para la autocompletacion de comandos resaltandolos en amarillo los comandos autocompletados son 

* nano config.zsh
* source config.zsh

![](/A00328064/imagenes/captura-autocompletado1.png)

![](/A00328064/imagenes/captura-autocompletado2.png)


***3 INSTALACION Y CONFIGURACION DE TMUX***

Como se menciono anteriormente tmux ya se encuentra instalado ahora se procedera a la configuracion 

#### Configuración personalizada

Puede ajustar configuraciones como la edición de la salida de comandos con vi ó la combinación de teclas para ejecutar una acción a través de un archivo de configuración llamado .tmux.conf. 

```
$ vi ~/.tmux.conf
# use C-a, since it's on the home row and easier to hit than C-b
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
A continuacion se anexa imagen donde se genero el link del video de asciinema  grabado para la demostracion de la configuracion anteriormente mencionada

https://asciinema.org/a/jyyHMWIUIEypxBojMaUCijfbY

[![asciicast](A00328064/imagenes/link-video-asciinema.png)](https://asciinema.org/a/jyyHMWIUIEypxBojMaUCijfbY)

***4 DIVISION DE PANTALLA CON TMUX***

A continuacion se divide la pantalla en 4 cuadrantes y en cada uno se realiza las siguientes acciones:

* Salida del comando top
 * Salida de la ejecución del script de python courses.py
 * Peticiones por medio de curl a cada endpoint. Salida formateada con **jq**
 * Salida de la ejecución de **telnet towel.blinkenlights.nl**

Se anexa el Script courses.py

  ```
  # courses.py
  from flask import Flask
  import json
  app = Flask(__name__)

  @app.route("/courses")
  def courses():
      courses = {"courses": ["SO2018", "DS2018"]}
      return json.dumps(courses), 200

  @app.route("/courses/SO2018/curriculum")
  def curriculum():
      curriculum = {"curriculum": ["virtualization", "processes", "memory"]}
      return json.dumps(curriculum), 200

  if __name__ == "__main__":
      app.run('0.0.0.0')
  ```
  ```
  python courses.py
  ```
  ![](/A00328064/imagenes/captura1.png)
  
  ![](/A00328064/imagenes/captura2.png)
  
  
  ***5 APLICACION DE SLACK CON PYTHON***
  
 * ejecuta en background a las 8:00am todos los días con crontab
 
 ```
 * 8 * * * /home/operativos/so-exam2/A00328064/python-punto6.py
 ```
 
 * Se ejecuta como una aplicación de linea de comandos usando.
 * tiene los valores de procesador, memoria y disco disponibles usando https://pypi.python.org/pypi/psutil/4.3.0
 * publica en este canal de slack https://so-exam2-espacio.slack.com/messages/CAK92Q04A/ 

  
 ![](/A00328064/imagenes/slack.png)
 
```
 
 #!/usr/bin/env python
import cli.app
import psutil
from slackclient import SlackClient
import os
from flask import Flask, request

@cli.app.CommandLineApp
def codigo_punto6(app):
	slack_token = 'xoxp-359442552021-358760308865-359213525683-48613a5acfec2e654c48d7c553203080' 
	sc = SlackClient(slack_token)

	sc.api_call(
	  "chat.postMessage",
	  channel="CAK92Q04A",
	  text =str(psutil.cpu_times())+"\n\n"+str(psutil.cpu_percent(interval=1, percpu=True))+"\n\n"+str(psutil.cpu_stats())+"\n\n"+str(psutil.virtual_memory())+"\n\n"+str(psutil.swap_memory())+"\n\n"+str(psutil.disk_usage('/'))              
	)
	print(psutil.cpu_times())	


if __name__ == "__main__":
    codigo_punto6.run()
```
