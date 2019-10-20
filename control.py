# control interfaces with model and view

from model import Model
from view import View
import numpy as np

def filled(p, q):
    if p == '1':
        if m.update(0,0,q):
            return True
    elif p == '2':
        if m.update(0,1,q):
            return True
    elif p == '3':
        if m.update(0,2,q):
            return True
    elif p == '4':
        if m.update(1,0,q):
            return True
    elif p == '5':
        if m.update(1,1,q):
            return True
    elif p == '6':
        if m.update(1,2,q):
            return True
    elif p == '7':
        if m.update(2,0,q):
            return True
    elif p == '8':
        if m.update(2,1,q):
            return True
    elif p == '9':
        if m.update(2,2,q):
            return True
    return False

# init model
m = Model()

print(View.update(m.getBoard()))

while True:
    pos1 = input("Player 1: choose your position\n")
    while not filled(pos1, 'x'):
        pos1 = input("Player 1: Invalid move. Choose your position\n")
    
    print(View.update(m.getBoard()))
    if m.end():
        break

    pos2 = input("Player 2: choose your position\n")
    while not filled(pos2, 'o'):
        pos2 = input("Player 2: Invalid move. Choose your position\n")
    
    print(View.update(m.getBoard()))
    if m.end():
        break
