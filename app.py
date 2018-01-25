#Þröstur Haraldsson
import os
from bottle import *

@route('/')
def index():
    run(host='0.0.0.0', port=os.environ.get('PORT')
