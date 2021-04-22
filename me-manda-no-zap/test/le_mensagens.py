import sys
sys.path[0] += '\\..'

from bot.twitter_bot import TwitterBot

twitter = TwitterBot()
mensagens = twitter.get_mensagens()
for key, value in mensagens.items():
    print(key)
    for mensagem in value:
        print(mensagem)
        print()