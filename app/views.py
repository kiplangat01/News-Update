from flask import render_template
from requests import request
from app import views
from .request import get_news

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular movie
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_news)


@app.route('/news/<int:news_id>')
def News(news_id):

    '''
    View news page function that returns the movie details page and its data
    '''
    return render_template('news.html',id = news_id)

  
