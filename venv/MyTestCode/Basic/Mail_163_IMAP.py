# How to get the mail from mailbox
# Need special settings for security: http://config.mail.163.com/settings/imap/index.jsp?uid=fred82li@163.com 

import imaplib, string, email 

M = imaplib.IMAP4_SSL("imap.163.com")  
print('Please type in your password: ')
pwd = input()
M.login('fred82li@163.com',pwd)
M.select()
typ, data = M.search(None, 'ALL') 

for num in data[0].split():  
   try:
        typ, data = M.fetch(num, '(RFC822)')  
        msg = email.message_from_string(data[0][1].decode('utf-8'))  
        # print(msg["From"])
        print('The ' + str(num) + ' mail: ' + msg["Subject"])
        # print(msg["Date"])  
    except Exception as e:
        print('Unexcepted Error catched by code : ' + str(e))
        continue

print('Done!')
M.logout()  
