import subprocess
import smtplib
from email.mime.text import MIMEText
from json import dumps
from httplib2 import Http
import sys



threshold = 90
partition = "/"
#server = "aptsreport"
servers = ['aptsreport', 'aptsapp', 'opepa', 'gyankunj', 'punjab', 'wepsolution', 'mcaassales', 'empportal', 'mom', 'linode', 'git', 'apts-repo' , 'edugridelearn', 'edugridict', 'novatium', 'edupal']



def report_via_chat(message):
    """Hangouts Chat incoming webhook quickstart."""
    #SaGo Plays Group url = 'https://chat.googleapis.com/v1/spaces/AAAAn0Y7oJs/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=XxOh9ZNVBQnQehl4V513urU5BpSXf8m1UtkVKoQIYmg%3D'
    url = 'https://chat.googleapis.com/v1/spaces/AAAAj7S4a5c/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=2I50NNQj4AQUC934AN7COBGsAIj2T1tWlVXjVB4tX2I%3D'
    bot_message = {
            'text' : message }

    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    print(response)

def check_once(servername):
   df = subprocess.Popen(["ssh",servername,"df","-h"], stdout=subprocess.PIPE)
   for line in df.stdout:
     splitline = line.decode().split()
     #print(splitline[4][:-1])
     if splitline[5] == partition:
       if int(splitline[4][:-1]) > threshold:
         print(f"Disk Usage {splitline[4]} | Clear unwanted files")
         mes= server+ " server `Disk usage limit exceeded!!!` - "
         mes += splitline[4]
         report_via_chat(mes)
       else:
         print(f"Disk Usage {splitline[4]}")
         mes=server+ " server storage is ok with "
         mes += splitline[4]
         report_via_chat(mes)
report_via_chat("*_GoBot Diskspace Routine Check Module From Red Wolf_*")
for server in servers:
 check_once(server)
