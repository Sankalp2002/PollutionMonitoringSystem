import time
from timeloop import Timeloop
from datetime import timedelta
from .models import Node
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from myapp import views

import smtplib, ssl

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "iiitapollutionmonitoring@gmail.com"  # Enter your address
receiver_email = "rajendran02sankalp@gmail.com"  # Enter receiver address
password = "Z5rCyYFT"


def polCheck():
    nodes=Node.objects.all()
    for node in nodes:
        if node.mq135>250:
            node.alert=True
            node.save()
def alertCheck():
    print ("ALERT CHECK : {}".format(time.ctime()))
    polCheck()
    alertnodes=[]
    nodes=Node.objects.all()
    for node in nodes:
        if node.alert==True:
            alertnodes.append(node)
    nodes = Node.objects.all()
    if len(alertnodes)!=0:
        text = "Pollution alert at nodes with IDs "
        for n in alertnodes:
            text.append(n.node_Id)
            text.append(',')
        message='Subject: {}\n\n{}'.format("Pollution Alert", text)
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
        HttpResponseRedirect(reverse('showNodes'))
    return (alertnodes,nodes)

tl = Timeloop()

@tl.job(interval=timedelta(seconds=20))
def check():
    alertCheck()
    
    
# if __name__ == "__main__":
#     tl.start(block=True)
# import plotly
# plotly.tools.set_credentials_file(username='sankyplot', 
# api_key='zsjuRWCY3GCpwpRb2vbT')