from re import sub
import smtplib
import ssl
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"

sender_email = "kareltestcode@gmail.com"
reciever_email = "vanoordtkarel@gmail.com"

password = "aaghntxwbpgjlpnk"

message = EmailMessage()

message["From"] = sender_email
message["To"] = reciever_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:

    server.login(sender_email, password)
    server.sendmail(sender_email, reciever_email, message.as_string())

print("Success!")
