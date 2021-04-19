from twilio.rest import Client
from decouple import config

class WhatsappBot:
    def __init__(self):
        self.sender = config('TWILIO_SENDER_NUMBER')
        self.twilio_sid = config('TWILIO_ACCOUNT_ID')
        self.twilio_token = config('TWILIO_AUTH_TOKEN')

    def send_message(self, receiver, message):
        try:
            client = Client(self.twilio_sid, self.twilio_token)

            message = client.messages.create(
                              body=message,
                              from_='whatsapp:{0}'.format(self.sender),
                              to='whatsapp:{0}'.format(receiver)
                          )

            return message.sid

        except TwilioRestException as e:
            return e
    
    pass
