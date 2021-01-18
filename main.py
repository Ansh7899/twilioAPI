import schedule
import time

from twilio.rest import Client

#from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

msg = "Good Morning Love! Hope You Have An Amazing Day <3"
cellphone = "+91XXXXXXXXXXXXXXX"
twilio_number = "+16XXXXXXXXXXXXXXXXX"
twilio_account = "AXXXXXXXXXXXXXXXXXXXXXXXXX"
twilio_token = "dXXXXXXXXXXXXXXXXXXXXXXXX"

def send_message():
    client = Client(twilio_account, twilio_token)
    client.messages.create(to=cellphone, from_=twilio_number, body=msg)


schedule.every().day.at("15:55").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(2)
