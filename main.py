import smtplib
from email.mime.text import MIMEText
from email.header import Header
from smtplib import SMTP_SSL

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header



smtpPort = 587
host_server = 'smtp-mail.outlook.com'
senderAddr = 'hpycal@outlook.com'
pwd = 'pycalPass1'
receiver = 'h.lx@outlook.com'

# 邮件的正文内容
mail_content = "你好，<p>这是使用python登录qq邮箱发送HTML格式邮件的测试：</p><p><a href='http://www.yiibai.com'>易百教程</a></p>"
# 邮件标题
mail_title = 'Maxsu的邮件'

# 邮件正文内容
msg = MIMEMultipart()
# msg = MIMEText(mail_content, "plain", 'utf-8')
msg["Subject"] = Header(mail_title, 'utf-8')
msg["From"] = senderAddr
msg["To"] = Header("接收者测试", 'utf-8')  ## 接收者的别名

# 邮件正文内容
msg.attach(MIMEText(mail_content, 'html', 'utf-8'))

# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('d:\\test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="attach.txt"'
msg.attach(att1)

# 构造附件2，传送当前目录下的 runoob.txt 文件
# att2 = MIMEText(open('yiibai.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="yiibai.txt"'
# msg.attach(att2)

smtp = smtplib.SMTP(host_server,smtpPort)
smtp.ehlo()
smtp.starttls()
smtp.login(senderAddr, pwd)

smtp.sendmail(senderAddr, receiver, msg.as_string())
smtp.quit()
