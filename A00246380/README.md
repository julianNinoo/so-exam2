**1.**
# Examen Parcial 2
**Nombre:** Marisol Giraldo Cobo

**Código:** A00246380

**Correo:** marisol.giraldo@correo.icesi.edu.co

**Curso:** Sistemas Operativos

**Tema:**  Comandos de Linux, Scripts, Herramientas.

**Profesor:** Daniel Barragán

**2.**
# DESCRIPCIÓN:
Con la realización de este Readme, se pretende mostrar los pasos realizados para conocer y emplear comandos de Linux para la 
realización de tareas administrativas. Como instalar, configurar y emplear herramientas de Linux de apoyo al uso del sistema operativo.
Y la Automatización de tareas por medio de scripts.

**3.**
# INSTALACIÓN Y CONFIGURACIÓN DE ZSH Y GIT 
Para la instalación de git se usa el siguiente comando: #apt-get install git
![instalaciongit](https://user-images.githubusercontent.com/35766585/39630713-c9c83160-4f75-11e8-80f7-a3e236ad0a4e.png)

Para la instalación de zsh se usa el siguiente comando: # apt-get install zsh
![instalacionzsh](https://user-images.githubusercontent.com/35766585/39630803-132ea9f6-4f76-11e8-9db1-cdeaa6c70373.png)

Para instalar los plugins de oh-my-zsh se debe ejecutar el comando:
sh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

En caso de no tener instalado curl, debe instalarse, mediante el comando: #apt-get install curl
![curl](https://user-images.githubusercontent.com/35766585/39632470-cba54de2-4f7a-11e8-9dea-fd062d99dd92.png)

Los plugins  de oh-my-zsh tambien se pueden instalar mediante el comando:
sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
![instalacionoh_my_zsh](https://user-images.githubusercontent.com/35766585/39632634-4436ff08-4f7b-11e8-8960-560193af8ff0.png)

# USO DE UN TOKEN EN LUGAR DE USUARIO Y CONTRASEÑA PARA LA CONEXIÓN CON GIT
Existen distintas maneras de conectarse a GitHub. La conexión por medio de tokens no solo permite la interacción de un usuario con repositorios de GitHub, sino también permite la conexión de aplicaciones directamente con repositorios.

Primero desde mi cuenta de GitHub voy a perfil, opción configuraciones y selecciono la opción de token personal.
Luego se le agrega una descripción, se le asignan los permisos necesarios y se genera token.
![guardartoken](https://user-images.githubusercontent.com/35766585/39631046-c8d64f16-4f76-11e8-9c43-140f5b7fc2a9.png)

Una vez el token se genera es necesario tener en cuenta,  nunca compartir el token de forma pública.
![tokengenerado](https://user-images.githubusercontent.com/35766585/39631469-dcf8c662-4f77-11e8-8ca6-52d4661295c7.png)

Para configurar el token se debe clonar el repositorio, mediante el comando: ~ git clone https://github.com/marisolcitag/so-exam2.git
![gitclone](https://user-images.githubusercontent.com/35766585/39632217-18ff46a2-4f7a-11e8-8fa2-bfa31810bad2.png)

Para configurar el token como medio de autenticación a GitHub , se ejecuta el comando ~ git config remote.origin.url "https://topSecretToken@github.com/marisolcitag/so-exam2.git"
![gitremote](https://user-images.githubusercontent.com/35766585/39646663-c90d0f44-4fa1-11e8-97fb-8eb061985070.png)

# USO DE LOS ALIAS gaa, gcmsg y ggp PARA EL ENVIO DE UN COMMIT AL FORK DEL REPOSITORIO so-exam2.
Los comandos gaa, gcmsg y ggp son comandos utilizados como atajos para usar con git.

Atajo | Comando
--- | --- 
gaa | git add --all
gcmsg | git commit -m
ggp | git push origin $(current_branch)

A continuación se muestra la ejecución de estos comandos.
![ggagcmgpp](https://user-images.githubusercontent.com/35766585/39633046-79810aae-4f7c-11e8-838d-71d0320cb84b.png)

**4.**
# INSTALACIÓN Y CONFIGURACIÓN DEL PLUGIN  ZSH-AUTOSUGGESTIONS
Se debe clonar el repositorio en el directorio de plugins de oh-my-zsh con el comando:
~ git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
![1](https://user-images.githubusercontent.com/35766585/39633287-260ef3e4-4f7d-11e8-8b32-4752abee9d58.png)

Adicionar el plugin a la lista de plugins activos con los comandos:
~ nano ~/.zshrc
![2](https://user-images.githubusercontent.com/35766585/39633386-6b95de96-4f7d-11e8-8f11-2f5f93061747.png)

Adicionar el plugin a la lista de plugins activos con los comandos:
~ plugins=(git vi-mode zsh-autosuggestions)
![3](https://user-images.githubusercontent.com/35766585/39633757-82d0f6da-4f7e-11e8-9b71-1ec6cdb0d7ea.png)

Luego se ejecuta el comando:
~ source ~/.zshrc
![4](https://user-images.githubusercontent.com/35766585/39633800-a08ac264-4f7e-11e8-8096-4e4f7e01a252.png)

Mediante el comando ~ nano $ZSH_CUSTOM/marisolcitag.zsh se ingresa al archivo para modificar el valor de resaltado por yellow
![5](https://user-images.githubusercontent.com/35766585/39633915-f11b1436-4f7e-11e8-8215-325ace5167ca.png)

Luego se ejecuta el comando:
~ source ~/.zshrc

Una vez que se ejecute al ingresar algun comando se podra observar la modificación.
![6](https://user-images.githubusercontent.com/35766585/39634249-e2f2a300-4f7f-11e8-9318-8abab0aa37fc.png)
![7](https://user-images.githubusercontent.com/35766585/39634396-544dc660-4f80-11e8-9935-332c7a984462.png)

**5.**
# INSTALACIÓN Y CONFIGURACIÓN DE TMUX
Para instalar tmux se ejecuta el comando ~ apt-get install tmux -y
![8](https://user-images.githubusercontent.com/35766585/39634603-d938d8ec-4f80-11e8-9cb0-07120910f6cc.png)

Para realizar una configuración personalizada se debe modificar el archivo de configuración llamado .tmux.conf. 
Se digita el comando: ~ nano ~/.tmux.conf ; y se agrega la siguiente configuración:
![9](https://user-images.githubusercontent.com/35766585/39634687-0f956ffe-4f81-11e8-8308-d64ea83aa3ff.png)
La nueva configuración permitirá hacer lo siguiente:
- Cambiar la combinación de teclas Ctrl+b por Ctrl+a
- Recargar el archivo de configuración mediante la combinación de teclas Ctrl + a + Shift + r
- Navegar a través del buffer utilizando la combinación de teclas Ctrl + a + [
- Seleccionar texto usando Espacio, Copiar la selección usando Enter y Pegar usando Ctrl + a + ]

Para que la configuración tenga efecto se debe salir de tmux e ingresar nuevamente. 
![10 1](https://user-images.githubusercontent.com/35766585/39635512-5423ee32-4f83-11e8-990f-35f909dcba49.png)

A continuación se muestra la ejecución del proceso de Copiar y Pegar
- Seleccionar y Copiar texto
![11](https://user-images.githubusercontent.com/35766585/39635633-ad6f3f82-4f83-11e8-96ce-85becef57799.png)
-Pegar texto
![pegolo que copie](https://user-images.githubusercontent.com/35766585/39652203-6d971d60-4fb2-11e8-939b-b685f889ebd2.png)

**6.**
# SESIÓN DE TMUX
Para crear la sesión tmux, se debe ejecutar el siguiente comando: ~ tmux new-session -s so-exam2.
Una vez creada la sesión, para dividir la pantalla en cuatro cuadrantes, se deben combinar las siguientes teclas:
- Ctrl + a + %   -> Divide la pantalla verticalmente
- Ctrl + a + "   -> Divide la pantalla horizontalmente
![12](https://user-images.githubusercontent.com/35766585/39635939-7ac28552-4f84-11e8-9002-91fdb1da0d4a.png)

En el primer cuadrante se ejecuta el comando: ~ top

![top](https://user-images.githubusercontent.com/35766585/39636120-ea4675f0-4f84-11e8-8e9f-efa450acf94e.png)

En el segundo cuadrante ejecutamos el script llamado courses.py creado en python.
Para ejecutar el script de python courses.py es necesario importar el modulo Flask. Para ello se siguieron las siguientes instrucciones:
* Se Instala python
![13](https://user-images.githubusercontent.com/35766585/39636430-c312a048-4f85-11e8-937f-360cba175602.png)

* Se Instala la libreria Flask
![14](https://user-images.githubusercontent.com/35766585/39636464-e100e2f4-4f85-11e8-9a9b-aeb4a9df605f.png)

* Para realizar las peticiones por medio de curl con la salida formateada con jq, se debe instalar jq.
![16](https://user-images.githubusercontent.com/35766585/39636619-687d730a-4f86-11e8-83dd-c0b8748d552d.png)

* Se selecciona el script que se encuentra en el punto 6 del enunciado del examen en el enlace: https://github.com/ICESI/all-exams/tree/master/2018_a/so/exam2 y se pega en el archivo courses.py ejecutando el comando ~ nano courses.py en el cuadrante.  
![17](https://user-images.githubusercontent.com/35766585/39636719-b48a14c4-4f86-11e8-9e3e-a568481000b9.png)

Después de guardar, se ejecuta el comando: ~ pyhon courses.py
![18](https://user-images.githubusercontent.com/35766585/39637221-f953a196-4f87-11e8-80c7-3b1608038d71.png)

![19 1](https://user-images.githubusercontent.com/35766585/39637382-6d81e29e-4f88-11e8-9e5c-81cbf21511ae.png)

En el tercer cuadrante se mostrara la salida de la ejecución del comando ~ telnet towel.blinkenlights.nl
![starwars8](https://user-images.githubusercontent.com/35766585/39637762-990b935a-4f89-11e8-9a02-d5dfaa280a8b.png)
![starwars2](https://user-images.githubusercontent.com/35766585/39637584-19b7637c-4f89-11e8-93eb-9ed2588bfcac.png)

En el cuarto cuadrante se realizarán peticiones por medio de curl a cada endpoint. Salida formateada con jq.
* Se ejecuta el comando ~ curl http://0.0.0.0:5000/courses | jq '.'
![curl1](https://user-images.githubusercontent.com/35766585/39638018-783d6b7a-4f8a-11e8-8ce7-b5763884dfe1.png)

* Se ejecuta el comando ~ curl http://0.0.0.0:5000/courses/SO2018/curriculum | jq '.'
![curl2](https://user-images.githubusercontent.com/35766585/39638186-03d7138e-4f8b-11e8-9276-e79453105cad.png)

**7**
# APLICACIÓN QUE ENVIA UN MENSAJE AUTOMÁTICO AL CANAL DE SLACK
Se debe realizar una aplicación que envie un mensaje cada 10 minutos; para esto primero se crea un workspace en slack llamado marisolcitagoperativos, y un canal con el nombre #parcialoperativos.
![22](https://user-images.githubusercontent.com/35766585/39638557-37f1f9c6-4f8c-11e8-93bb-619bdd50b921.png)

Se debe instalar pyCLI mediante el comando ~ pip install pyCLI. Este comando nos permitirá ejecutar nuestra aplicación como una de linea de comandos se utilizó la guía https://pythonhosted.org/pyCLI/.
![23](https://user-images.githubusercontent.com/35766585/39638801-fa741eca-4f8c-11e8-9341-9c942a4a705f.png)

* Luego se instala psutil mediante el comando ~ pip install psutil. Esto permite obtener los valores de procesador, memoria y disco disponible. Se utilizo la guia https://pypi.org/project/psutil

* Y se instala el Slack Client con el comando ~ pip install slackClient. Se utilizo la guía https://github.com/slackapi/python-slackclient

![25](https://user-images.githubusercontent.com/35766585/39640622-315831ca-4f91-11e8-959c-7b3fdafc41f0.png)
![24](https://user-images.githubusercontent.com/35766585/39639018-a89a6a90-4f8d-11e8-8360-9cdf7d1c6c1d.png)

 * Ahora, se crea el script de python con nombre ~ codigo_punto6.py. Este script se encuentra en la guia https://github.com/slackapi/python-slackclient donde:
1. Se importan librerias de slackCliente, de psutil, de flask, entre otras.
2. Antes de definir el método se coloca la linea @cli.app.CommandLineApp para que identifique que es una aplicación de lineas de comando.
3. Se le asigna el token a una variable.
4. El uso primario del slack es enviar mensajes a un usuario o a un canal. En este caso para enviar el mensaje al canal se
utiliza el id del canal(parcialoperativos)
5. A través de psutil se obtiene el consumo de CPU, RAM y Disco.
A continuación se muestra el script.
![26](https://user-images.githubusercontent.com/35766585/39647201-a338fcfe-4fa3-11e8-900f-01a4ef1c80d1.png)

* Después de guardar, se ejecuta el comando: ~ pyhon codigo_punto6.py

* Para ejecutar la aplicación en background, se configura crontab para que el algoritmo se ejecute cada 10 minutos, mediante el comando
~ crontab -e.
![instalar crontab](https://user-images.githubusercontent.com/35766585/39648671-9e122e80-4fa8-11e8-9d9b-a78f131c882a.png)

* Dentro del archivo se añade la siguiente linea:
  */10 * * * * python /home/marisolcitag/so-exam2/A00246380/codigo_punto6/codigoslack.py
![sin titulo2](https://user-images.githubusercontent.com/35766585/39648723-d41a3aa4-4fa8-11e8-9595-37248d3301de.png)

* Se guarda el archivo y se verifica que la configuración se haya guardado con ~ crontab -l.
![instalar crontab -l](https://user-images.githubusercontent.com/35766585/39650674-b31168fe-4fae-11e8-9e29-087d4d7321df.png)

Y una vez transcurridos 10 minutos se puede observar el envio de la información que se programo en el script.
![sin titulo4](https://user-images.githubusercontent.com/35766585/39648991-cee64e14-4fa9-11e8-98ee-dd208c5ce41e.png)
![slack2](https://user-images.githubusercontent.com/35766585/39649030-f70b42fa-4fa9-11e8-8e84-66792c6a02d3.png)

* Después se realizo el respectivo commit.
![final](https://user-images.githubusercontent.com/35766585/39650585-561fb4fc-4fae-11e8-959f-74f3a74b45e6.png)

**7**
URL GITHUB => https://github.com/marisolcitag/so-exam2.git

#BIBLIOGRAFIA

- DEBIAN
 URL:https://www.debian.org/

- REPOSITORIO GITHUB
  URL: https://github.com/ICESI 
  URL: https://github.com/ICESI-Training

- Oh My Zsh
  URL:https://github.com/robbyrussell/oh-my-zsh

- zsh-autosuggestions 
  URL: https://github.com/zsh-users/zsh-autosuggestions
  
- cli — command line tools
  URL: https://pythonhosted.org/pyCLI/

- psutil 5.4.5
  URL: https://pypi.org/project/psutil

- python-slackclient
  URL: https://github.com/slackapi/python-slackclient
  










