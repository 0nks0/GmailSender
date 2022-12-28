import smtplib
import ssl
from email.message import EmailMessage

e_sender = input('Enter Email[Gmail] Address: ')
e_password = input('Enter Email Password Key!: ')
e_receiver = input('Enter your Receiver: ')

subject = input('Please Enter Email Subject: ')
body = input('Please Enter Email Body: ')

em = EmailMessage()
em['From'] = e_sender
em['To'] = e_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    try:
        smtp.login(e_sender, e_password)
        print("Preparing Email")
        smtp.sendmail(e_sender, e_receiver, em.as_string())
        print("Email Have Been Sent :)")
    except:
        print('There was an Error sending the Email')
