import cli.app
import psutil
from slackclient import SlackClient
import os
from flask import Flask, request

@cli.app.CommandLineApp
def codigo(app):
        slack_token = 'xoxp-354235018625-355829357959-355038697093-52b57c6fdd13ed203c6b8d4ed56da79a'
        sc = SlackClient(slack_token)
        sc.api_call(
          "chat.postMessage",
          channel="CAEG813EG",
          text =str(psutil.cpu_times())+"\n\n"+str(psutil.cpu_percent(interval=1, percpu=True))+"\n\n"+str(psutil.cpu_stats())+"\n\n"+str(psutil.virtual_memory())+"\n\n"+str(psutil.swap_memory())+"\n\n"+str(psutil.disk_usage('/'))
        )
        print(psutil.cpu_times())


if __name__ == "__main__":
    codigo.run()




