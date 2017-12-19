from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP

smtpPort = 587
host_server = 'smtp-mail.outlook.com'
senderAddr = 'hpycal@outlook.com'
pwd = 'pycalPass1'
receiver = 'h.lx@outlook.com'

mail_title = '邮件标题'
mail_content = '邮件内容'

smtp = SMTP(host_server,smtpPort)
smtp.ehlo()
smtp.starttls()
smtp.login(senderAddr, pwd)

msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = senderAddr
msg["To"] = receiver

smtp.sendmail(senderAddr, receiver, msg.as_string())
smtp.quit()