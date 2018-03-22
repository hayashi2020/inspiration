import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formatdate

from_address = 'sb@gmail.com'
to_address = 'sb@gmail.com'

charset = 'ISO-2022-JP'
subject = 'email with python'
text = 'Yes, you can send an email with python now.'

msg = MIMEText(text, 'plain', charset)
msg['Subject'] = Header(subject, charset)
msg['From'] = from_address
msg['To'] = to_address
msg['Date'] = formatdate(localtime=True)

smtp = smtplib.SMTP('smtp.gmail.com')
smtp.login(smtp_user, smtp_password)
smtp.sendmail(from_address, to_address, msg.as_string())
smtp.close()
