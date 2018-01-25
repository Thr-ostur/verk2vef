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
def lidur2():
    return "<a href='/sida_1'>Síða 1</a>""\n"
    "<a href='/sida_2'>Síða 2</a>""\n"
    "<a href='/sida_3'>Síða 3</a>"
@route('/sida1')
def sida1():
    return "Þetta er síða 1"
@route('/sida2')
def sida2():
    return "Þetta er síða 2"
@route('/sida3')
def sida3():
    return "Þetta er síða 3"
@route('/sida_1')
def sida_1():
    return "static/1.png"
@route('/sida_2')
def sida_2():
    return "static/2.png"
@route('/sida_2')
def sida_2():
    return "static/3.png"
@route('/static/myndir')
def server_static(myndir):
    return static_file(myndir,root="./myndir")
run(host='0.0.0.0', port=os.environ.get('PORT'))
