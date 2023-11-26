from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()
TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("AUTH_TOKEN")


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=os.getenv("FROM_NUMBER"),
            to=os.getenv("TO_NUMBER")
        )
        # print if successfully sent
        print(message.sid)

