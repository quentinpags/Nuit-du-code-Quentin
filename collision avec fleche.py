# -*- coding: utf-8 -*-
"""
Created on Wed May 28 11:23:02 2025

@author: Hugo
"""
import pyxel
pyxel.init(128,128)

def collision(x_joueur, y_joueur, fleche_x, fleche_y):
    
    if x_joueur + 15 < fleche_x and x_joueur> fleche_x and y_joueur+13 < fleche_y and y_joueur > fleche_y:
        VIE -= 1
def update():
    for projectile in
    collision(Perso.x, Perso.y, Projectile.x, Projectile.y)
    
def draw():
    pass

pyxel.run(update, draw)