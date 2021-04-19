from decouple import config

class TwitterBot:
    def __init__(self):
        self.api_key = config('TWITTER_API_KEY')
        self.api_secret_key = config('TWITTER_API_SECRET_KEY')
        self.access_token = config('TWITTER_ACCESS_TOKEN')
        self.access_token_secret = config('TWITTER_ACCESS_TOKEN_SECRET')

    pass