import os
from bottle import *

@route('/')
def index():
    return "<a href='/about'>About</a>""<a href='/biography'>Biography</a>""<a href='/Pictures'>Pictures</a>"
@route('/about')
def about():
    return "Lorem ipsum litlum fiskum"
@route('/biography')
def biography():
    return "Lorem ipsum kriddum diskum"
@route('/Pictures')
def Pictures():
    return "Lorem ipsum stönsum krönsum"

  
run(host='0.0.0.0', port=os.environ.get('PORT'))
