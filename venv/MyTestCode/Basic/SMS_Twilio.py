# Account Dashboard: https://www.twilio.com/console
# Account SID: AC752bf58f0825c536d323c852364b75e0
# Token: c50f6abe217c05eedf8d3d75b77e33e6
# https://www.twilio.com/console/phone-numbers/getting-started to get your phone number
# Sample: https://www.youtube.com/watch?v=knxlmCVFAZI

# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

account_sid = 'AC752bf58f0825c536d323c852364b75e0'
auth_token = 'c50f6abe217c05eedf8d3d75b77e33e6'
client = Client(account_sid, auth_token)

print('Please input the phone number where you want to send message: ')
phoneNumber = input()

message = client.messages.create(
        body="Welcome to Twilio free world!",
        from_="+14153017406",
        to=phoneNumber)

print(message.sid)
