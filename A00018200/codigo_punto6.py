import psutil
import os 
from slackclient import SlackClient
import cli.app

@cli.app.Application
def stats(app):
	slack_token =os.environ["SLACK_BOT_TOKEN"]
 

	cpu= psutil.cpu_times() 
	print(cpu)

	memoria = psutil.virtual_memory()
	print(memoria)

	disco=psutil.disk_usage('/')
	print(disco)

	sc = SlackClient(slack_token)

	sc.api_call(
  	"chat.postMessage",
  	channel="aleatorio",

  	text="Hello from Python! :tada:"+'\n'+"los recursos en este momentos son:"+'\n'+"cpu:"+str(cpu)+'\n'+" memoria :"+str(memoria)+'\n'+" disco:"+str(disco)
)
if __name__=="__main__":
	stats.run()
