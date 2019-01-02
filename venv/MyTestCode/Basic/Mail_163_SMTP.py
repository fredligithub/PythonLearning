# How to send mail via 163 mailbox
# smtp.163.com

import smtplib
from email.mime.text import MIMEText

mailto_list=['fred82li@163.com']           #收件人(列表)
mail_host="smtp.163.com"                   #使用的邮箱的smtp服务器地址，这里是163的smtp地址
mail_user="fred82li@163.com"               #用户名

def send_mail(to_list,sub,content,password):
    msg = MIMEText(content,_subtype='plain')
    msg['Subject'] = sub
    msg['From'] = mail_user
    msg['To'] = to_list  

    server = smtplib.SMTP()        
    server.connect(mail_host)                      #连接服务器        
    server.login(mail_user,password)               #登录操作        
    server.sendmail(mail_user,mailto_list, msg.as_string())      
    server.close()

print('Ready to send mail, please input your password for mail account: ')
pwd = input()
send_mail('fred82li@163.com','Test','My Test Mail From Python!', pwd)
print('Done!')