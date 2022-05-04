from flask import render_template
from . import main
from ..request import get_news,get_articles
from ..models import Source,Article

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    source = get_news()
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title, source_list=source)


@main.route('/news/<id>')
def News(id):

    '''
    View news page function that returns the movie details page and its data
    '''
    news = get_articles()
    return render_template('news.html',id = id, news_list = news)

# @main.route('/articles')
# def articles():
#     articles = get_articles()

#     tittle = 'Hop headlines'

#     return render_template('articles.html', articles = articles, tittle = tittle)