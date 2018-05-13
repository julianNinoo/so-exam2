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






