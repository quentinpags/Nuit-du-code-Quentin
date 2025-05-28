# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint
coeur = 4#a changer avec le nombre de coeur du perso


pyxel.init(128,128)


pyxel.load("2.pyxres")
def update():
    pass


def draw():
    pyxel.cls(1)
    for i in range(coeur):
        pyxel.blt(4*(i+1), 5, 0, 115, 52, 10, 9, colkey=2)
    if coeur <= 0:
        #fin de jeu
        pass
    
pyxel.run(update, draw)