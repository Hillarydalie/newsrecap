from . import main
from flask import render_template

@main.app_errorhandler(404)
def errorpage(error):
  title = 'Error 404'
  return render_template('error.html',title = title),404    