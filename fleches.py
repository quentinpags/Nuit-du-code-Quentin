# -*- coding: utf-8 -*-
"""
Created on Wed May 28 12:51:29 2025

@author: Hugo
"""
import pyxel

skin_fleche=[132,72,8,0]
list_fleches =[]
pyxel.init(128,128)
pyxel.load("2.pyxres")

player_x = 60
player_y = 60

vitesse_balle = 4


def tir_fleche_joueur(pos_x, pos_y):#du joueur
    """ajout fleche ds list_fleche"""
    global list_fleches
    if pyxel.btnp(pyxel.KEY_SPACE):
        
        list_fleches.append([pos_x+8, pos_y+8])
        
def creation_fleche(pos_x, pos_y):        
    """creation de fleches de list_fleche"""
    pyxel.blt(pos_x+3, pos_y+7, 0, 132, 72, 8, 1)
    
def mouv_fleche(fleche):
    global vitesse_balle
    fleche[0] += vitesse_balle
def verif_mort():
    global list_fleches
    for fleches in list_fleches:
        for hostiles in list_entites:
            if hostiles[0] + 15 < fleches[0] and hostiles[0]> fleches[0] and hostiles[1]+13 < fleches[1] and hostiles[1] > fleches[1]:
                list_fleches.remove(fleches)
                list_entites.remove(hostiles)
                

def update():
    tir_fleche_joueur(player_x, player_y)
    for fleches in list_fleches:
        mouv_fleche(fleches)
        #destruction
        verif_mort()
                
def draw():
    pyxel.cls(3)
    
    for fleche in list_fleches:
        creation_fleche(fleche[0], fleche[1])

pyxel.run(update, draw)