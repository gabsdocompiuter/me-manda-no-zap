import sys
sys.path[0] += '\\..'

from bot.twitter_bot import TwitterBot

twitter = TwitterBot()
id_usuario = twitter.get_id_usuario('sharggg')
twitter.envia_dm(id_usuario, 'oi')
