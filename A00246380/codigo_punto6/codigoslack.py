from slackclient import SlackClient
import psutil
import cli.app
import os
from flask import Flask, request

@cli.app.CommandLineApp
def codigoslack(app):

	slack_token = 'xoxp-357553063088-358150103939-358387871861-ab7ac84ab6a3746664dd161ed5869cd2'
	sc = SlackClient(slack_token)
	sc.api_call(
	  "chat.postMessage",
	  channel="#parcialoperativos",
	  text="MY REPORT\n Virtual memory: "+str(psutil.virtual_memory())+"\n Swap memory: "+str(psutil.swap_memory())+"\n Disk: "+str(psutil.disk_usage('/'))+"\n CPU percent: "+str(psutil.cpu_percent())+"% \n Cores: "+str(psutil.cpu_count())
	)
if __name__ == "__main__":
    codigoslack.run()
