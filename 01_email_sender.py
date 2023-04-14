import smtplib
import ssl
from email.message import EmailMessage
from app2 import password

email_sender ='m.nozad@gmail.com'
email_password=password

email_receiver=input('Enter Address of Receiver:') 
subject='plse dont forget me'
body="""
when you watch this code, please follow me
"""
em=EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

# context= ssl.create_default_context()
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender,email_password)
#     smtp.sendmail(email_sender,email_receiver,em.as_string())
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_sender, email_password)
    smtp.send_message(em)
    print('OK')