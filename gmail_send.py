#!/usr/bin/env python3

import smtplib
import ssl
import datetime
from datetime import date

port = 465
pwd = "<your smtp pwd>"
user = "<your smtp user>"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
	server.login(user,pwd)
	sender_email = "sender@example.com"
	receiver_email = "recipient@example.com"
	message_subject = "Prova invio Email da Python " + str(date.today())
	message_body = """
Message body,
goes here.
"""

	message = 'Subject: {}\n\n{}'.format(message_subject,message_body)
	
	server.sendmail(sender_email, receiver_email,message)
	server.quit()


