import sys
sys.path[0] += '\\..'

from bot.twitter_bot import TwitterBot

twitter = TwitterBot()
twitter.get_mensagens()