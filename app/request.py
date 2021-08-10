import urllib.request
import json
from .models import Sources, Articles


# Getting api key
api_key = None

# Getting the news base url
base_url =None

# Getting the news articles base url
articles_base_url = None


def configure_request(app):
    global api_key,base_url,articles_base_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_SOURCES_BASE_URL']
    articles_base_url = app.config['ARTICLES_BASE_URL']

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_sources(sources_results_list)

    return sources_results


def process_sources(sources_list):
    '''
     Function that processes the news sources results and turns them into a list of objects
     Args:
             sources_list: A list of dictionaries that contain sources details
     Returns:
             sources_results: A list of sources objects
     '''
    sources_results = []

    for source_item in sources_list:
        id = source_item.get('id')
        name = source_item.get('name')
        description = source_item.get('description')
        url = source_item.get('url')
        category = source_item.get('category')
        language = source_item.get('language')
        country = source_item.get('country')

        sources_object = Sources(
            id, name, description, url, category, language, country,)
        sources_results.append(sources_object)

    return sources_results



def get_articles(id):
    '''
    Function that gets the json response to our url request
    '''
    get_articles_url = articles_base_url.format(id, api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)
        

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)

    return articles_results

def process_articles(articles_list):
    '''
     Function that processes the news articles results and turns them into a list of objects
     Args:
             articles_list: A list of dictionaries that contain sources details
     Returns:
             articles_results: A list of sources objects
     '''
    articles_results = []

    for articles_item in articles_list:
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')

        
        articles_object = Articles(
            title, description, url, urlToImage, publishedAt)
        articles_results.append(articles_object)


    return articles_results
