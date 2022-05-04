import os

class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/top-headlines/sources?apiKey={}'
    NEWS_API_KEY = '8b74f92912264851821658c37a3faab6'
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&sortBy=publishedAt&apiKey={}'
class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development' : DevConfig,
    'production'  : ProdConfig
}
