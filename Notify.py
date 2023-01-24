from winotify import Notification,audio
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def Notify():
     alarm=Notification(app_id='DANGER fissure',title='Fissure has been detected',
     msg='THE SYSTEM HAS DETECTED A FISSURE OUTSIDE OF SAFETY REGULATIONS',
     icon="Fissure_Detection_Project\warning.jpg",duration="long")
     alarm.set_audio(audio.LoopingAlarm,loop=True)
     alarm.show()
     message =MIMEMultipart()
     message['from']="ALARM BOT"
     message['to']="youssefkharbouch2016@gmail.com"
     message['subject']="CONVEYOR FISSURE"
     message.attach(MIMEText("A FISSURE HAS BEEN DETECTED PLEASE ACT QUICKLY"))
     with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
         smtp.ehlo()
         smtp.starttls()
         smtp.login("youssefkharbouch2016@gmail.com","vsxxgalrgtuizvcu")
         smtp.send_message(message)
         print ('sent')