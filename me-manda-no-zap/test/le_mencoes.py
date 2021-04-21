import sys
sys.path[0] += '\\..'

from bot.twitter_bot import TwitterBot

twitter = TwitterBot()
for a in twitter.read_mentions():
    print(a.get('user'))
    print(a.get('id'))
    print()