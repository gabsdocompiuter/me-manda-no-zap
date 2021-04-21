import tweepy
from decouple import config

class TwitterBot:
    def __init__(self):
        api_key = config('TWITTER_API_KEY')
        api_secret_key = config('TWITTER_API_SECRET_KEY')
        access_token = config('TWITTER_ACCESS_TOKEN')
        access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')
        
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)

        self.api = tweepy.API(auth)
        self.user = config('TWITTER_USER')

    def read_mentions(self):
        lista_retorno = []
        tweets = self.api.mentions_timeline()

        for tweet in tweets:
            tweet_loop = False
            tweet_respondido = self.api.get_status(tweet.in_reply_to_status_id_str)
            for t in tweet_respondido.entities.get('user_mentions'):
                if t.get('screen_name') == self.user:
                    tweet_loop = True

            if not tweet_loop:
                tweet_dict = {
                    "id": tweet.user.id_str,
                    "user": tweet.user.screen_name,
                    "tweet_replied": tweet_respondido,
                    "link_tweet": f'https://twitter.com/{tweet.user.screen_name}/status/{tweet.id_str}'
                }

                lista_retorno.append(tweet_dict)
        
        return lista_retorno

    def envia_dm(self, id_usuario, mensagem):
        self.api.send_direct_message(id_usuario, mensagem)

    def get_id_usuario(self, username):
        usuario = self.api.get_user(username)
        return usuario.id_str

    pass