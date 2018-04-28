# Parcial 2  
  
**Universidad Icesi**  
**Curso:** Sistemas Operativos  
**Estudiante:** Juan Felipe Reyes Garcia  
**Codigo:** A00309924  
**Correo:** juanfe_518@hotmail.co  
  
 **Instalación zsh y oh-my-zsh**  
 Se instala zsh, el cual tiene abreviaciones para diferentes comandos de git:  
   
 ![](images/git%20commands.PNG)    
 
Se instala el plugin zsh-autosuggestions, el cual sugiere el autocompletado de comando previamente invocados por el usuario. Para cambiar el color del resaltado de la sugeriencia del plugin se modifica:  
```
$ vi ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh
  ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='yellow'
```  
  
*Comandos resaltados en amarillo:*  
![](images/echo%20Somethin%20zsh%20auto%20yellow.PNG)     
![](images/source%20zsh%20auto%20yellow.PNG)   

**Instalacion tmux**
Se instala tmux y se configura los comandos de tmux para cambiar el **ctrl+a = ctrl+b** y activar el vi-mode y la selección:  

![](images/tmux%20vi-mode%20and%20Selection.PNG)  

Usando tmux se realiza se crea una nueva sesion operativos y se divide en 4 cuadrantes para cada nos de los procesos requeridos:   
*4 cuadrantes tmux*    
![](images/tmux%204%20vistas.PNG)  

Se implementa un codigo en python que usa pyCli para crea una aplicación de comandos que por medio de psUtil obtienen el consumo de 
CPU, RAM y Disco, el cual es enviado a un canal de slack: [canal de Slack](https://pruebanina.slack.com/messages/CAAHMBBFT/), 
por medio de crontab se llama a la aplicación cada 10 minutos, como se ve en el canal de Slack.  

```
#!/usr/bin/env python
import cli.app
import psutil
from slackclient import SlackClient
import os
from flask import Flask, request

@cli.app.CommandLineApp
def codigo_punto6(app):
	slack_token = 'xoxp-350599383857-350915301092-351282028229-fd4877eac07506c1564830343d70d77f' 
	sc = SlackClient(slack_token)

	sc.api_call(
	  "chat.postMessage",
	  channel="CAAHMBBFT",
	  text =str(psutil.cpu_times())+"\n\n"+str(psutil.cpu_percent(interval=1, percpu=True))+"\n\n"+str(psutil.cpu_stats())+"\n\n"+str(psutil.virtual_memory())+"\n\n"+str(psutil.swap_memory())+"\n\n"+str(psutil.disk_usage('/'))              
	)
	print(psutil.cpu_times())	


if __name__ == "__main__":
    codigo_punto6.run()
```

**Crontab:**
Agregar al archivo de crontab para agendar el proceso cada 10 minutos:  
```
 0,10,20,30,40,50 * * * * /home/operativos/so-exam2/A00309924/codigo_punto6.py
```


*imagen canal Slack*
![](images/slack%20message.PNG)  


