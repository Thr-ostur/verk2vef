import os
from bottle import *

@route('/')
def index():
    return "<h1>Verkefni 2</h1><a href='/about'>Liður 1</a>""<a href='/lidur2'>Liður 2</a>"
@route('/about')
def about():
    return "<a href='/sida1'>Síða 1</a>""\n"
    "<a href='/sida2'>Síða 2</a>""\n"
    "<a href='/sida3'>Síða 3</a>"
@route('/lidur2')
def lidurb():
    return '<h2>Liður 2</h2>' \
           '<h3>Veldu tölu:</h3>' \
           '<a href="/favorite?image=1"><img src="/static/1.png" width="150"></a>' \
           '<a href="/favorite?image=2"><img src="/static/2.png" width="150"></a>' \
           '<a href="/favorite?image=3"><img src="/static/3.png" width="150"></a>'
@route('/sida1')
def sida1():
    return "Þetta er síða 1"
@route('/sida2')
def sida2():
    return "Þetta er síða 2"
@route('/sida3')
def sida3():
    return "Þetta er síða 3"
@route('/favorite')
def favorite():
    image = request.query.image

    return '<h2>Númerið sem þú valdir er: </h2>' \
           '<img src="/static/' + image +'.png" width="200">' \
           '<h4><a href="/lidur2">Til baka</a></h4>'
@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./myfiles")
run(host='0.0.0.0', port=os.environ.get('PORT'))
