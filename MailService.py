import os
import Main
import smtplib
import ssl

def mailer():
    port=587
    smtp_server="smtp.gmail.com"
    sender_email="srivardhan729@gmail.com"
    Main.speak("Enter the recipent mail id, sir")
    receiver_email=input("Enter recipent mail id ")
    var=os.environ['var']
    message=Main.TakeCommand()
    context=ssl.create_default_context()
    with smtplib.SMTP(smtp_server,port) as server:
        server.starttls(context=context)
        server.login(sender_email,var)
        server.sendmail(sender_email,receiver_email,message)