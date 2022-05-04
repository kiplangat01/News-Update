# from unicodedata import category, name
# from app.main.views import articles
from . import create_app
import urllib.request,json
from .models import Source,Article

# News = models.News

# Getting api key
# app = create_app('development')
api_key=None
articles_url=None
base_url=None

def configure_request(app):
    global api_key,articles_url,base_url
    api_key = app.config['NEWS_API_KEY']
    articles_url = app.config['ARTICLES_URL']
    base_url = app.config['NEWS_API_BASE_URL']

def get_news():
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)

        news_results = None

        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)


    return news_results

def process_results(news_list):
    '''
    Function  that processes the news result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of news objects
    '''

    news_results = []
    for news_item in news_list:
        id = news_item.get('id')
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        category = news_item.get('category')
        language = news_item.get('language')
        country = news_item.get('country')

        if id:
            news_object = Source(id,name,description,language,country,category,url)
            news_results.append(news_object)

    return news_results

def get_articles(id):
    ariclesurl=articles_url.format(id,api_key)
    with urllib.request.urlopen(ariclesurl) as url:
        jdata=url.read()
        data= json.loads(jdata)
        articles_result= None
        if data['articles']:
            art_list=data['articles']
            articles_result=proc(art_list)


    return articles_result


def proc(lista):
    aricles_result=[]
    for l in lista:
        source=l.get('source')
        title=l.get('title')
        author=l.get('author')
        descrpition=l.get('description')
        content=l.get('content')
        url= l.get('url')
        urlToImage=l.get('urlToImage')
        publishedAt=l.get('publishedAt')
        if source:
            article_object=Article(source, title, author,descrpition, urlToImage,publishedAt,content,url)
            aricles_result.append(article_object)
    return aricles_result
    
    







