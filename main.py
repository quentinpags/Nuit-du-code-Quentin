# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint
zombie =[[65, 17, -12,14],[80,16,-12,15],[97,17,-11,14],[113,17,-11,14]]#position de tuile
SKIN = 0


LISTE_ENTITES =[]

width = 128
height = 128
pyxel.init(width, height, title="Chevalliay")
#play(0, 2,loop= True)#import de sons
pyxel.load("2.pyxres")
pyxel.frame_count = 0#nb de frame


x = width//2
y = height//2
print("self.y", y)
JEU = "EN_COURS"
PLAYER_X = 0
PLAYER_Y = 50
VITESSE = 3

def creation_mob():
        global LISTE_ENTITES
        
        if pyxel.frame_count % randint(10, 20) == 0 and len(LISTE_ENTITES) < 5:
            
            LISTE_ENTITES.append([randint(30,128) , 110])
       
            
        
def mouv_mob(entite):
    
    entite[0]-=1
    if entite[0] <= 0:
        LISTE_ENTITES.remove(entite)
    
def mob(pos_x, pos_y, type_mob):
    """affiche un mob a une position pos_x, pos_y, avec le type_mob"""
    
    pyxel.blt(pos_x, pos_y, 0, type_mob[SKIN][0], type_mob[SKIN][1], type_mob[SKIN][2],
              type_mob[SKIN][3], colkey=2)
    
    
def update():
    global SKIN
    if pyxel.frame_count % 4 == 0:
        SKIN +=1
        if SKIN >2:
            SKIN = 0
    creation_mob()
    # for entite in list_entites:
    #     mouv_mob(entite)
    pyxel.frame_count +=1

    if pyxel.btn(pyxel.KEY_UP):
        global PLAYER_Y, VITESSE
        PLAYER_Y += -VITESSE
    elif pyxel.btn(pyxel.KEY_DOWN):
        PLAYER_Y += +VITESSE


def draw():
    global LISTE_ENTITES
    pyxel.cls(0)

    pyxel.cls(0)
    pyxel.blt(PLAYER_X, PLAYER_Y, 0, 0, 16, 16, 16, colkey=2, )
    pyxel.blt(PLAYER_X-1, PLAYER_Y+5, 0, 32, 112, 16, 16, colkey=2)
    
    for entite in LISTE_ENTITES:
        mob(entite[0], entite[1], zombie)




pyxel.run(update, draw)