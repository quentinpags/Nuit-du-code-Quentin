# -*- coding: utf-8 -*-
"""
Created on Wed May 28 12:17:51 2025

@author: Hugo
"""

import pyxel
from random import randint
zombie =[[65, 17, -12,15],[81,16,-12,15],[97,17,-12,15],[113,17,-11,15]]#position de tuile
SKIN = 0



LISTE_ENTITES =[]

width = 128
height = 128
pyxel.init(width, height, title="Chevalliay")

pyxel.load("2.pyxres")
pyxel.play(0, 2,loop= True)#import de sons
pyxel.frame_count = 0#nb de frame


x = width//2
y = height//2
print("self.y", y)

PLAYER_X = 0
PLAYER_Y = 50
VITESSE = 3
MODE = "DEV"
VIE = 3
STATUT_GAME = "PLAYING"

skin_fleche=[132,72,8,0]
list_fleches= []




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
def verif_mort(fleches):
    global list_fleches, LIST_ENTITES
    
    for hostiles in LIST_ENTITES:
        if hostiles[0] + 15 < fleches[0] and hostiles[0]> fleches[0] and hostiles[1]+13 < fleches[1] and hostiles[1] > fleches[1]:
            list_fleches.remove(fleches)
            LIST_ENTITES.remove(hostiles)
                

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

def degats_player():
    global MODE, VIE
    if MODE == "DEV":
        return
    else:
        VIE -=1
        if VIE == 0:
            mort()




def mort():
    global STATUT_GAME
    STATUT_GAME = "END"

    
    
def update():
    global SKIN
    if pyxel.frame_count % 4 == 0:
        SKIN +=1
        if SKIN >2:
            SKIN = 0
    creation_mob()
    # for entite in LIST_ENTITES:
    #     mouv_mob(entite)
    pyxel.frame_count +=1

    if pyxel.btn(pyxel.KEY_UP):
        global PLAYER_Y, VITESSE
        PLAYER_Y += -VITESSE

    if pyxel.btn(pyxel.KEY_LEFT):
        global VIE
        mort()

     
    elif pyxel.btn(pyxel.KEY_DOWN):
        PLAYER_Y += +VITESSE
    tir_fleche_joueur(PLAYER_X, PLAYER_Y)
    for fleches in list_fleches:
        
        mouv_fleche(fleches)
        
        #destruction
        # verif_mort(fleches)
        

def draw():
    global LISTE_ENTITES,STATUT_GAME,STAT
    pyxel.cls(6)
    
    for i in range(VIE):
        pyxel.blt(4*(i+1), 5, 0, 115, 52, 10, 9, colkey=2)
    

    if STATUT_GAME == "PLAYING":

        

        
        pyxel.blt(PLAYER_X, PLAYER_Y, 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(PLAYER_X-1, PLAYER_Y+5, 0, 32, 112, 16, 16, colkey=2)
        
        for entite in LISTE_ENTITES:
            mob(entite[0], entite[1], zombie)
    
    if STATUT_GAME == "END":
        if pyxel.frame_count % 30 < 25:  # visible pendant 15 frames sur 30
            pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "You Lose", 7)
            chaine_de_caractere = "PUSH ENTER TO START"
            # pyxel.text((pyxel.height-114)//2, (pyxel.width-114)//2, 7)
            pyxel.text((pyxel.width - len(chaine_de_caractere) * 4) // 2, (pyxel.height - 8) // 2, chaine_de_caractere, 7)
    for fleche in list_fleches:
        creation_fleche(fleche[0], fleche[1])




pyxel.run(update, draw)