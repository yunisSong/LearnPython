#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header



sender = 'xxx@163.com'
receiver = 'xxx@qq.com'
subject = '大家好'
smtpserver = 'smtp.163.com'
username = 'xxx'
password = 'xxxx'

msg = MIMEText('你这是什么情况','plain','utf-8')#中文需参数‘utf-8'，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = 'Yunis<yunis_song@163.com>'
msg['To'] = "Yunis<332963965@qq.com>"


try:
    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com',25)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msg.as_string())

    print ("邮件发送成功")
    smtp.quit()
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
    print (smtplib.SMTPException.message)
