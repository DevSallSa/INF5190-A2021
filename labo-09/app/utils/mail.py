import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

source = 'mmasson.inf5190@gmail.com'
dest = 'mmasson.inf5190@gmail.com'
body = 'Mon premier courriel'
subject = 'INF5190 - Labo GMAIL'

msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = source
msg['To'] = dest
msg['ReplyTo'] = source

msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login('mmasson.inf5190@gmail.com', 'monpassword')
server.sendmail(source, dest, msg.as_string())
server.quit()
