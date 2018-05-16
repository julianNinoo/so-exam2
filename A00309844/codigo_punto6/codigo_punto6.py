from slackclient import SlackClient
import psutil
import cli.app

@cli.app.CommandLineApp
def slackMessage(app):

	slack_token = 'xoxb-359517053831-KciUfv3LezJMxAdwb8tBb7WW'
	sc = SlackClient(slack_token)
	sc.api_call(
	  "chat.postMessage",
	  channel="CAJHR8E6R",
	  text="Reporte de los valores de disponibilidad de memoria RAM, Disco Duro y CPU: \n Memoria Disponible: "+str(100-psutil.virtual_memory()[2])+"% \n Porcentaje de uso del Disco Duro: "+str(100-psutil.disk_usage('/')[3])+"% \n Porcentaje de uso de la CPU: "+str(psutil.cpu_percent())+"% "
	)
if __name__ == "__main__":
    slackMessage.run()
