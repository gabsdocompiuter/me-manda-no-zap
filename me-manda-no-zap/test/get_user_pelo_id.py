import sys
sys.path[0] += '\\..'

from bot.twitter_bot import TwitterBot

twitter = TwitterBot()
usuario = twitter.get_usuario("1377029027370835970")
print(usuario)