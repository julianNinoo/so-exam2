from slackclient import SlackClient
import psutil

slack_token = 'xoxp-357583684772-357711730259-357118694816-1288f10af0d0a0d6abfab7eeb69e582e'
sc = SlackClient(slack_token)

cpu_percent = psutil.cpu_times_percent(interval=1, percpu=False)
swap_memory =  psutil.swap_memory()
disk_partitions = psutil.disk_partitions()
disk_usage = psutil.disk_usage('/')


sc.api_call(
          "chat.postMessage",
            channel="icesi_prueba",
              text= "CPU TIMES PERCENT \n" + str(cpu_percent) + "\n SWAP MEMORY \n" + str(swap_memory) + "\n DISK PARTITIONS \n" + str(disk_partitions) + "\n DISK USAGE \n" + str(disk_usage)
              )
