import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

msg = MIMEMultipart()

msg['From'] = "fromemailID"
msg['To'] =  "toemailID"
msg['Subject'] = "Test Email"

content = "This is the mail"

msg.attach(MIMEText(content))

filename = "test.txt"
fileopen = open(r'C:\Python 35\test1.txt', "rb")


attachment = MIMEBase('application','octect-stream')
attachment.set_payload(fileopen.read())
encoders.encode_base64(attachment)
attachment.add_header('Content-Disposition', 'attachment', filename=filename)

msg.attach(attachment)


server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('emailID','password')
server.sendmail('from','to',msg.as_string())
server.close()


