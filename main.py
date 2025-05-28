# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint
zombie =[[128,16, 12,14]]#position de tuile
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

PLAYER_X = 0
PLAYER_Y = 50
VITESSE = 3
MODE = "DEV"
VIE = 3
STATUT_GAME = "PLAYING"


def creation_mob():
        global LISTE_ENTITES
        
        if pyxel.frame_count % randint(10, 20) == 0 and len(LISTE_ENTITES) < 5:
            
            LISTE_ENTITES.append([pyxel.width-10, randint(0, pyxel.height-20)])
       
            
        

    
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
    global SKIN,STATUT_GAME
     
    
    
    if STATUT_GAME == "PLAYING":
        creation_mob()
        # for entite in list_entites:
        #     mouv_mob(entite)
        pyxel.frame_count +=1

        if pyxel.btn(pyxel.KEY_UP):
            global PLAYER_Y, VITESSE
            PLAYER_Y += -VITESSE

        elif pyxel.btn(pyxel.KEY_DOWN):
            PLAYER_Y += VITESSE

        

    if pyxel.btnp(pyxel.KEY_RIGHT):
        
        if STATUT_GAME == "PAUSE":
            STATUT_GAME = "PLAYING"

        else:
            STATUT_GAME = "PAUSE"

    if pyxel.btn(pyxel.KEY_LEFT):
            global VIE
            mort()
            

        
     
    


def draw():
    global LISTE_ENTITES,STATUT_GAME,STAT
    
    

    if STATUT_GAME == "PLAYING":
        pyxel.cls(6)
    
        for i in range(VIE):
            pyxel.blt(4*(i+1), 5, 0, 115, 52, 10, 9, colkey=2)

        

        
        pyxel.blt(PLAYER_X, PLAYER_Y, 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(PLAYER_X-1, PLAYER_Y+5, 0, 32, 112, 16, 16, colkey=2)
        
        for entite in LISTE_ENTITES:
            mob(entite[0], entite[1], zombie)
    
    if STATUT_GAME == "END":
        pyxel.cls(6)
    
    
        if pyxel.frame_count % 30 < 25:  # visible pendant 15 frames sur 30
            pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "You Lose", 7)
            chaine_de_caractere = "PUSH ENTER TO START"
            # pyxel.text((pyxel.height-114)//2, (pyxel.width-114)//2, 7)
            pyxel.text((pyxel.width - len(chaine_de_caractere) * 4) // 2, (pyxel.height - 8) // 2, chaine_de_caractere, 7)
    
    if STATUT_GAME == "PAUSE":
        
    
        for i in range(VIE):
            pyxel.blt(4*(i+1), 5, 0, 115, 52, 10, 9, colkey=2)
        pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "PAUSE", 7)





pyxel.run(update, draw)