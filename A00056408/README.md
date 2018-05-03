# Segundo Parcial  
**Nombre:** Yesid Leonardo López  
**Código:** A00056408  
**URL repositorio:** https://github.com/leonleo997/so-exam2.git  

## Desarrollo Parcial  
## A. gaa, gcmsg, ggp  

A continuación se muestra las capturas de los comandos gaa, gcmsg, ggp  
  
![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/gitShortcuts.PNG)  

## B. Plugin zsh-autosuggestions  

A continuación, se muestra el auto completado de dos comandos usando el plugin zsh-autosuggestions:  
  
![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/autocomplete1.PNG)  
  
![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/autocomplete2.PNG)  
  
## C. Configuración del tmux  
  
![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/tmuxconf.PNG)   

  A continuación, se observa el archivo .tmux.conf. Este archivo posee la configuración para: Cambiar la combinación de teclas de ´Ctrl + b´ a ´Ctrl + a´, Recargar el archivo de configuración mediante la combinación de teclas ´Ctrl + a + Shift + r´, para navegar a través del flujo usamos la combinación de teclas ´Ctrl + a + [´, Seleccionamos usando ´Espacio´, copiamso la selección usando ´Enter´ y pegamos usando ´Ctrl + a + ]´.  


![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/reload.PNG)  

![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/ctrl+a+[.PNG)  

![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/espacio.PNG)  


## D. Cuadrantes tmux  

En esta sección dividimos la pantalla verticalmente usando ´Ctrl + a + "´, y horizontalmente usando ´Ctrl + a + %´ para tenerla dividida en 4 cuadrantes.  
En cada cuadrante ejecutamos los siguientes comandos:

En el primer cuadrante escribimos:
```console
operativos@Debian:~$ top
```
En el segundo cuadrante ejecutamos:
```console
operativos@Debian:~$ telnet towel.blinkenlights.nl
```
En el tercer cuadrante, ejecutamos el script llamado courses.py creado en Python:
```console
operativos@Debian:~$ python courses.py
```
En el último cuadrante, ejecutamos las siguientes líneas habiendo ejecutado antes courses.py  
```console
operativos@Debian:~$ curl http://0.0.0.0:5000/courses | jq '.'
operativos@Debian:~$ curl http://0.0.0.0:5000/courses/SO2018/curriculum | jq '.'
```
Tendremos finalmente lo siguiente:  
![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/punto6.PNG)  

## E. Envío de mensaje automático a canal de slack  

En esta sección enviaremos un mensaje, cada 10 minutos, a un workspace llamado **so-exam-2**, y creamos un canal con el nombre **#slackmessage**.  
El script que tiene el código se encuentra en [aquí](https://github.com/leonleo997/so-exam2/blob/master/A00056408/codigo_punto6/ejercicio.py).  

Instalamos crontab usando el siguiente comando  
```console
operativos@Debian:~$ sudo apt-get install cron
```
Modificamos el archivo usando el comando ´~ crontab -e´ y adicionamos la línea que se ve al final de la siguiente imagen:  

![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/crontab_config.PNG)  

Guardamos e imprimimos la configuración de crontab usando '~ crontab -l' y revisamos Slack donde imprimirá cada 10 minutos el siguiente mensaje:
![alt text](https://github.com/leonleo997/so-exam2/blob/master/A00056408/images/crontabmessage.PNG)  





