import requests 
from config import Config
from .models import Article,Sources

api_key = Config.API_KEY
news_url = Config.NEWS_URL
article_url = Config.ARTICLE_URL
sources_url = Config.SOURCE_HEADLINES

# This will generate our sources request from the news api
def getNews():
    response = requests.get(news_url+api_key)
    res = response.json()

    newsSource = None

    if res['sources']:
        sources_list = res['sources']
        newsSource = filter(sources_list)

    return newsSource

def filter(sources_list):
    newsSource = []
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        country = source.get('country')
        if language == 'en':
            source_object = Sources(id,name,description,url,category,language,country)
            newsSource.append(source_object)
    return newsSource

# This will get the articles from the source parent
def getArticles(id):
    new_url = sources_url.format(id)
    response = requests.get(new_url+api_key)
    articleHead = response.json()

    source_article = None

    if articleHead["articles"]:
        headline_list = articleHead["articles"]
        source_article = processArticle(headline_list)
  
    return source_article

# Process articles response from json file
def processArticle(headline_list):
  source_article = []
  for newarticle in headline_list:
    author = newarticle.get('author')
    title = newarticle.get('title')
    description = newarticle.get('description')
    url = newarticle.get('url')
    urlToImage = newarticle.get('urlToImage')
    publishedAt = newarticle.get('publishedAt')
    if urlToImage:
      article_object = Articles(author,title,description,url,urlToImage,publishedAt)
      source_article.append(article_object)
  return source_article

# Search Form
def getSearchItem(search):
  new_url = article_url.format(search)
  response = requests.get(new_url+api_key)
  result = response.json()

  newSearchReturn = None

  if result["articles"]:
    article_list = result["articles"]
    newSearchReturn = ProcessSearch(article_list)
  return newSearchReturn

def ProcessSearch(article_list):
  newSearchReturn = []

  for art in article_list:
    author = art.get('author')
    title = art.get('title')
    description = art.get('description')
    url = art.get('url')
    urlToImage = art.get('urlToImage')
    publishedAt = art.get('publishedAt')
    if urlToImage:
      article_object = Articles(author,title,description,url,urlToImage,publishedAt)
      newSearchReturn.append(article_object)
      
  return newSearchReturn