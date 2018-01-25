import os
from bottle import *

@route('/')
def index():
    return "<h1>Verkefni 2</h1><a href='/about'>Liður A</a>""\n""<a href='/biography'>Liður B</a>"
@route('/about')
def about():
    return "Lorem ipsum litlum fiskum"
@route('/biography')
def biography():
    return "Lorem ipsum kriddum diskum"

  
run(host='0.0.0.0', port=os.environ.get('PORT'))
