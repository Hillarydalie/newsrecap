from . import main
from flask import render_template,redirect,request,url_for
from app.requests import getNews,getSearchItem,getArticles

# Insert home page view
@main.route('/')
def home():
  """
  homepage route
  """
  title = "Welcome to Newsrecapp"
  news = getNews()
  return render_template('index.html',sources = news, title = title)

# @main.route('/articles')
# def articles():
#   """
#   articles route
#   """
#   article = getSearchItem('programming')
  
#   return render_template('articles.html',article = article)


@main.route('/source/<id>')
def source(id):
  headlines = getArticles(id)
  source = id
  return render_template('articles.html',headlines = headlines , source = source)

@main.route('/news/highlight')
def highlight():
  technology = getSearchItem('technology')
  title = 'News Highlight'
  search_article = request.args.get('searchword')
  if search_article:
    return redirect(url_for('.searchArticle',new_article = search_article))
  else:
    return render_template('newsHighlight.html',title = title,technology = technology)

@main.route('/search/<new_article>')
def searchArticle(new_article):
  title = f'{new_article}'
  search = getSearchItem(new_article)
  return render_template('search.html',title = title,search = search)