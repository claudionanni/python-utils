#!/usr/bin/env python3

import smtplib
import ssl
import datetime
from datetime import date

port = 465
pwd = "<your smtp pwd>"

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com",port,context=context) as server:
	server.login("vott2009@gmail.com",pwd)
	sender_email = "Sender<sender@example.com>"
	receiver_email = "recipient@example.com"
	message_subject = "Send Email from Python " + str(date.today())
	message_body = """Hi!
This is the message body.
You can write in multiple lines.
"""

	message = 'Subject: {}\n\n{}'.format(message_subject,message_body)
	
	server.sendmail(sender_email, receiver_email,message)
	server.quit()


