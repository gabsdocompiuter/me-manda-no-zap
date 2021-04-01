from twilio.rest import Client
from decouple import config

account_sid = config('TWILIO_ACCOUNT_ID')
auth_token = config('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Mensagem enviada pelo python',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+555196540271'
                          )

print(message.sid)
