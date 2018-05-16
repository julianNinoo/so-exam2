from slackclient import SlackClient
import psutil
import cli.app
import os
from flask import Flask, request

@cli.app.CommandLineApp
def codigo(app):

	slack_token = 'xoxp-357435948240-357904958452-357436670176-6c43d43f925cd30a30ea128aae850f9d'
	sc = SlackClient(slack_token)
	sc.api_call(
	  "chat.postMessage",
	  channel="#operativos",
	  text="Machine Report: \n Virtual Memory: "+str(psutil.virtual_memory())+" \n Swap Memory: "+str(psutil.swap_memory())+" \n Disk Usage: "+str(psutil.disk_usage('/'))+" \n CPU Percent: "+str(psutil.cpu_percent())+"% \n Cores: "+str(psutil.cpu_count())
	)
if __name__ == "__main__":
    codigo.run()
