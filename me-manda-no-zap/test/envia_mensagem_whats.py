import sys
sys.path[0] += '\\..'

from bot.whatsapp_bot import WhatsappBot

whatsapp = WhatsappBot()
whatsapp.send_message('+555196540271', 'outra mensagem mais legal')
