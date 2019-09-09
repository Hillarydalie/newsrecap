import os
from dotenv import load_dotenv
load_dotenv()

class Config:
  """
  Main parent config class
  """
  NEWS_URL = 'https://newsapi.org/v2/sources?apiKey='
  API_KEY = os.environ.get('API_KEY')
  ARTICLE_URL = 'https://newsapi.org/v2/everything?q={}&sortBy=publishedAt&apiKey='
  SOURCE_HEADLINES = 'https://newsapi.org/v2/everything?sources={}&apiKey='


class Devconfig(Config):
  """
  Development configuration child class
  """
  
  DEBUG = True

class Prodconfig(Config):
  """
  Production configuration child class
  """
  pass

configurations = {
  'development' : Devconfig, 'production' : Prodconfig
}