import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'zxq1617233141@126.com'
msg['to'] = '2428374088@qq.com'
msg['subject'] = 'test'
content = '''''
    你好，
            这是一封自动发送的邮件。


'''
txt = email.mime.text.MIMEText(content)
msg.attach(txt)

smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.126.com', '25')
smtp.login('zxq1617233141@126.com', 'zxq1617233141zxq')
smtp.sendmail('zxq1617233141@126.com', '2428374088@qq.com', str(msg))
smtp.quit()