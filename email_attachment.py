import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

msg = MIMEMultipart()

msg['From'] = "testethical02@gmail.com"
msg['To'] =  "testethical01@gmail.com"
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
server.login('testethical02@gmail.com','2testethical@2')
server.sendmail('testethical02@gmail.com','testethical01@gmail.com',msg.as_string())
server.close()



"""
#http://email.about.com/cs/standards/a/base64_encoding.htm
why Base64 encoding:
When you have some binary data that you want to ship across a network, you generally don't do it by just 
streaming the bits and bytes over the wire in a raw format. Why? because some media are made for streaming text. 
You never know -- some protocols may interpret your binary data as control characters (like a modem), 
or your binary data could be screwed up because the underlying protocol might think that you've entered a 
special character combination (like how FTP translates line endings).

So to get around this, people encode the binary data into characters. Base64 is one of these types of encodings. 
Why 64? Because you can generally rely on the same 64 characters being present in many character sets, 
and you can be reasonably confident that your data's going to end up on the other side of the wire uncorrupted.

"""

