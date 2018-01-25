import os
from bottle import *

@route('/')
def index():
    return "<h1>Verkefni 2</h1><a href='/about'>About  </a>""<a href='/biography'>Biography</a>"
@route('/about')
def about():
    return "<a href='/sida1'>Síða 1</a>""\n""<a href='/sida2'>Síða 2</a>""\n""<a href='/sida3'>Síða 3</a>"
@route('/biography')
def biography():
    return "Lorem ipsum kriddum diskum"
@route('/sida1')
def sida1():
    return "Þetta er síða 1"
@route('/sida2')
def sida1():
    return "Þetta er síða 2"
@route('/sida3')
def sida1():
    return "Þetta er síða 3"
  
run(host='0.0.0.0', port=os.environ.get('PORT'))
