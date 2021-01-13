import schedule
import time

from twilio.rest import Client

#from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

msg = "Good Morning Love! Hope You Have An Amazing Day <3"
cellphone = "+917840038110"
twilio_number = "+16106001093"
twilio_account = "AC16df31d7cf349814862ec1a2ea8f5287"
twilio_token = "d0bb8168932c47a20ee732bcf090aae1"

def send_message():
    client = Client(twilio_account, twilio_token)
    client.messages.create(to=cellphone, from_=twilio_number, body=msg)


schedule.every().day.at("15:55").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(2)