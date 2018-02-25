import importlib
from p5 import *
 
x = importlib.import_module('elements')
a = x.Elements()

def setup():
    size(500,257)
    a = x.Elements()

def draw():
    #clear()
    background(92,170,130)
    a.backdrop(controls())
    a.biker(width, height, controls())  

def controls():
    if key == 'LEFT': return -1
    if key == 'RIGHT': return 1  

run()
