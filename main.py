# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint
zombie =[[65, 17, -12,14],[80,16,-12,15],[97,17,-11,14],[113,17,-11,14]]#position de tuile
skin = 0

list_entites =[]

width = 128
height = 128
pyxel.init(width, height, title="Chevalliay")
#play(0, 2,loop= True)#import de sons
pyxel.load("2.pyxres")
pyxel.frame_count = 0#nb de frame

def creation_mob():
        global list_entites
        
        if pyxel.frame_count % randint(10, 20) == 0 and len(list_entites) < 5:
            
            list_entites.append([randint(30,128) , 110])
       
            
        
def mouv_mob(entite):
    
    entite[0]-=1
    if entite[0] <= 0:
        list_entites.remove(entite)
    
def mob(pos_x, pos_y, type_mob):
    """affiche un mob a une position pos_x, pos_y, avec le type_mob"""
    
    pyxel.blt(pos_x, pos_y, 0, type_mob[skin][0], type_mob[skin][1], type_mob[skin][2],
              type_mob[skin][3], colkey=2)
    
    
def update():
global skin
if pyxel.frame_count % 4 == 0:
    skin +=1
    if skin >2:
        skin = 0
creation_mob()
# for entite in list_entites:
#     mouv_mob(entite)
pyxel.frame_count +=1


def draw():
    pyxel.cls(0)
    global list_entites
    for entite in list_entites:
        mob(entite[0], entite[1], zombie)




pyxel.run(update, draw)