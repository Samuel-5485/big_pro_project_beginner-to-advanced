from email.message import EmailMessage
from config import password
import ssl #what is the use of this 
import smtplib #and also this

email_sender = "samediriba54@gmail.com"
email_password = password

email_receiver = "samidiriba54@gmail.com"

subject = "Friendly Python Project!"
body = """
To be a perfect programmer this is the way for you!"""

em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())