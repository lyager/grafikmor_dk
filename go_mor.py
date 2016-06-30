#!/usr/bin/env python

from bottle import route, run, template
from random import randint

hvad_sir_mor = [
    'ja',
    'nej',
    'mere luft!',
    'hmmmmmmm'
]


# @route('/hello/<name>')
# def index(name):
#         return template('<b>Hello {{name}}</b>!', name=name)


@route('/sir/')
def index_sir():
    rand = randint(0, 3)
    try:
        return template(
            '<b>Grafikmor sir: {{svar}}!!!</b>!', svar=hvad_sir_mor[rand])
    except IndexError:
        return template(
            '<b>Grafikfar skal i skammekrogen, vi fik {{rand}}!!!</b>!',
            rand=rand)

run(host='localhost', port=8080)
