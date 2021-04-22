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

        self.tweepy = tweepy.API(auth)
        self.username = config('TWITTER_USER')
        self.id_conta = config('TWITTER_USER_ID')


    def read_mentions(self):
        lista_retorno = []
        tweets = self.tweepy.mentions_timeline()

        for tweet in tweets:
            tweet_loop = False
            tweet_respondido = self.tweepy.get_status(tweet.in_reply_to_status_id_str)
            for t in tweet_respondido.entities.get('user_mentions'):
                if t.get('screen_name') == self.username:
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
        self.tweepy.send_direct_message(id_usuario, mensagem)

    def get_id_usuario(self, username):
        usuario = self.tweepy.get_user(username)
        return usuario.id_str

    def get_usuario(self, id):
        usuario = self.tweepy.get_user(id)
        return usuario.screen_name
    
    def get_mensagens(self):
        mensagens_api = self.tweepy.list_direct_messages()
        mensagens = {}

        for mensagem_api in mensagens_api:
            remetente_mensagem = mensagem_api.message_create.get("sender_id")

            if remetente_mensagem != self.id_conta:
                message_data = mensagem_api.message_create.get("message_data")
                conteudo_mensagem = message_data.get("text")

                mensagem_dicionario = {
                    "id_mensagem": mensagem_api.id,
                    "remetente_id": remetente_mensagem,
                    "conteudo": conteudo_mensagem
                }

        #         if remetente_mensagem in mensagens:
        #             msg = mensagens.get(remetente_mensagem)
        #             msg.append(mensagem_dicionario)
        #         else:
        #             mensagens[remetente_mensagem] = []
        #             mensagens[remetente_mensagem].append(mensagem_dicionario)
        
        # for remetente, ms in mensagens.items():
        #     print(remetente)
        #     print(ms)
        #     print()

    def seguir_usuario(self, id_usuario):
        amizade = self.tweepy.create_friendship(id_usuario)
        print(amizade)


    pass