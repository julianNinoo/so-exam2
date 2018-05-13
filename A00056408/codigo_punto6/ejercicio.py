from slackclient import SlackClient
import psutil
import cli.app
import os
from flask import Flask, request

@cli.app.CommandLineApp
def slackMessage(app):

	slack_token = 'xoxp-356819662401-356668152000-357297520324-42f3f83505716287fa48e247a7ba41b0'
	sc = SlackClient(slack_token)
	sc.api_call(
	  "chat.postMessage",
	  channel="#slackmessage",
	  text="REPORT OF AVAILABILITY\n Virtual memory available: "+str(100-psutil.virtual_memory()[2])+"% \n Swap memory available: "+str(100-psutil.swap_memory()[3])+"% \n Disk available: "+str(100-psutil.disk_usage('/')[3])+"% \n CPU percent: "+str(psutil.cpu_percent())+"% \n Quantity of cores: "+str(psutil.cpu_count())
	)
if __name__ == "__main__":
    slackMessage.run()
