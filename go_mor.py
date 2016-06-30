#!/usr/bin/env python

from bottle import route, run, template
from random import randint


@route('/hello/<name>')
def index(name):
        return template('<b>Hello {{name}}</b>!', name=name)


@route('/sir/')
def index_sir():
    rand = randint(0, 3)
    return template('<b>Hello {{name}}</b>!', name=rand)


run(host='localhost', port=8080)
