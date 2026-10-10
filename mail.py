# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 17:23:18 2023

@author: svmah
"""

import smtplib
from email.message import EmailMessage

def Mail():
    SENDER_EMAIL = "supriya.protech@gmail.com"
    APP_PASSWORD = "clel schk jvvm fxfp"


    print("Mail Start")
    msg = EmailMessage()
    msg['Subject'] = "Suspicious Activity"
    msg['From'] = SENDER_EMAIL
    msg['To'] = "sohansprotech@gmail.com"
    msg.set_content('Suspicious Activity has been detected')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(SENDER_EMAIL, APP_PASSWORD)
            smtp.send_message(msg)
            print("Mail send successfully")
