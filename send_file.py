import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
mail_content= ''' Hello , this is a test email from ahmed hafdi'''
sender_address='bamirsamir@gmail.com'
sender_pass='bamir100'
reciever_address='Ahmed.Hafdi@ieee.org'
message=MIMEMultipart()
message['From']=sender_address
message['To']=reciever_address
message['To']=reciever_address
message['Subject']='test test alaah'
message.attach(MIMEText(mail_content,'plain'))
attach_file_name='C:/Users/ahafd/Desktop/contest_paper_2020/probas_reste.txt'
attach_file=open(attach_file_name,'rb')
payload=MIMEBase('application','octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload)
payload.add_header('Content-Decomposition','attachement',filename=attach_file_name)
message.attach(payload)
session=smtplib.SMTP('smtp.gmail.com',587)
session.starttls()
session.login(sender_address,sender_pass)
text=message.as_string()
session.sendmail(sender_address,reciever_address,text)
session.quit()
print('Mail SENT')