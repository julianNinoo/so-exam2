from slackclient import SlackClient
import cli.app
import psutil
import os
from flask import Flask, request

@cli.app.CommandLineApp
def app(app):
    slack_token = 'xoxp-357964064544-358115947873-359555646406-da306896a6f1df139e6f97ecd35134e7' 
    sc = SlackClient(slack_token)
    sc.api_call( "chat.postMessage", channel="test-exam",text =str(psutil.cpu_times())+"\n\n"+str(psutil.cpu_percent(interval=1, percpu=True))+"\n\n"+str(psutil.cpu_stats())+"\n\n"+str(psutil.virtual_memory())+"\n\n"+str(psutil.swap_memory())+"\n\n"+str(psutil.disk_partitions())+str(psutil.disk_usage('/')))   

if __name__ == "__main__":
    app.run()
