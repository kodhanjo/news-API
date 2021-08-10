from flask import render_template
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_sources, get_articles
from ..models import Sources, Articles


# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    business_sources = get_sources('business')
    entertainment_sources = get_sources('entertainment')
    sports_sources = get_sources('sports')
   
    title = "Get News"

    return render_template('index.html', title=title, sports_sources=sports_sources,business_sources=business_sources,entertainment_sources=entertainment_sources)



@main.route('/sources/<id>')
def articles(id):

    '''
    View root page function that returns the articles page and its data
    '''
    
    articles =get_articles(id)
    title = f'{id}'

    return render_template('articles.html', articles=articles, title=title)