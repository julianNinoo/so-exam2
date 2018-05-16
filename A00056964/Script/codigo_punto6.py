
from slackclient import SlackClient
import cli.app
import psutil
import os
from flask import Flask, request

@cli.app.CommandLineApp
def cod_punto6(app):

  slack_token = "xoxp-357232918080-357232918320-357466306033-41e17da00ded377164faf0bd7a6b03cc"
  sc = SlackClient(slack_token)

  tiempo_cpu=str(psutil.cpu_times())
  porcentaje_uso=str(psutil.cpu_percent(interval=1, percpu=True))
  estatus=str(psutil.cpu_stats())
  memoria=str(psutil.virtual_memory())
  swap=str(psutil.swap_memory())
  particiones=str(psutil.disk_partitions())
  uso_disco=str(psutil.disk_usage('/'))


  sc.api_call( "chat.postMessage", channel="CAHTCMM5Y",text ="Datos parcial: "+"\n\n"+particiones+"\n\n"+uso_disco+"\n\n"+estatus+"\n \n"+swap+"\n\n"+memoria+"\n\n"+tiempo_cpu+"\n\n"+porcentaje_uso)


if __name__ == "__main__":
  cod_punto6.run()
