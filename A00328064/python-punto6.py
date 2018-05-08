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
