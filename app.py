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
           '<a href="/val?image=1"><img src="/static/1.png" width="150"></a>' \
           '<a href="/val?image=tveir"><img src="/static/tveir.png" width="150"></a>' \
           '<a href="/val?image=3"><img src="/static/3.png" width="150"></a>'
@route('/sida1')
def sida1():
    return "Þetta er síða 1"
@route('/sida2')
def sida2():
    return "Þetta er síða 2"
@route('/sida3')
def sida3():
    return "Þetta er síða 3"
@route('/val')
def val():
    image = request.query.image

    return '<h1>Númerið sem þú valdir er: </h1>' \
           '<img src="/static/' + image +'.png" width="200">' \
           '<h3><a href="/lidur2">Til baka</a></h3>'
        
@error(404)
def error404(error):
    return '<h1>Hvað gerðiru vitlaust? þetta er allavegana ekki rétt</h1>'

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root="./myndir")

run(host='0.0.0.0', port=os.environ.get('PORT'))
