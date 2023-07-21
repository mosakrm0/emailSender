from email.message import EmailMessage
import ssl
import smtplib


emailSender = 'YourGmail'
appEmailPassword = 'YourAppPassword'

emailReceiver = 'The Email You Want To Sent TO'

subject = "Your Message Subject"

body = '''
Your Message body 


'''

em =EmailMessage()
em['From'] = emailSender
em['To'] = emailReceiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(emailSender, appEmailPassword)
    smtp.sendmail(emailSender, emailReceiver, em.as_string())
