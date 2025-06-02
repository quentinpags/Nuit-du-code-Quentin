# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint
zombie =[[128,16, 12,14]]#position de tuile
SKIN = 0

#fleche perso
SKIN_FLECHE=[132,72,8,0]
LIST_FLECHES= []
VITESSE_BALLE = 4

width = 128
height = 128
pyxel.init(width, height, title="Chevalliay")
#play(0, 2,loop= True)#import de sons
pyxel.load("2.pyxres")
pyxel.playm(0,loop= True)#import de sons


x = width//2
y = height//2


PLAYER_X = 0
PLAYER_Y = 50
VITESSE = 3
MODE = "DEV"
VIE = 3
STATUT_GAME = "PLAYING"

LISTE_ENTITES =[]






def tir_fleche_joueur(pos_x, pos_y):#du joueur
    """ajout fleche ds list_fleche"""
    global LIST_FLECHES
    if pyxel.btn(pyxel.KEY_SPACE):
        
        
        pyxel.play(0, 3,tick=1)
               
        LIST_FLECHES.append([pos_x+8, pos_y+8])
        
def creation_fleche(pos_x, pos_y):        
    """creation de fleches de list_fleche"""
    pyxel.blt(pos_x+3, pos_y+7, 0, 132, 72, 8, 1)
    
def mouv_fleche(fleche):
    global VITESSE_BALLE
    fleche[0] += VITESSE_BALLE
def verif_mort(fleches):
    #TODO: modifier fonction pour qu'elle marche 
    #TODO: changer collision avec les mobs
    """arg fleches avec [0] et [1]"""
    global LIST_FLECHES, LISTE_ENTITES, width
    
    for hostiles in LISTE_ENTITES:
        
        if hostiles[0] + 15 > fleches[0] and hostiles[0]< fleches[0] and hostiles[1]+13 > fleches[1] and hostiles[1] < fleches[1]:
            LIST_FLECHES.remove(fleches)
            LISTE_ENTITES.remove(hostiles)
            break
        elif fleches[0]>= 128:
            LIST_FLECHES.remove(fleches)
            break
        #TODO: kill les fleches
                
            
def creation_mob():
        global LISTE_ENTITES
        #TODO: faire en sorte que si mob sont les uns sur autres on change position
        
        if pyxel.frame_count % randint(10, 20) == 0 and len(LISTE_ENTITES) < 5:
            LISTE_ENTITES.append([110, randint(20,128)])
            #LISTE_ENTITES.append([pyxel.width-15, randint(10, pyxel.height-10)])
            
       
            
        

    
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
        
        

        if pyxel.btn(pyxel.KEY_UP):
            global PLAYER_Y, VITESSE
            if PLAYER_Y > 15:
                PLAYER_Y -= VITESSE
            

        elif pyxel.btn(pyxel.KEY_DOWN):
            if PLAYER_Y < pyxel.height-20:
                PLAYER_Y += VITESSE

        

    if pyxel.btnp(pyxel.KEY_RIGHT):
        
        if STATUT_GAME == "PAUSE":
            STATUT_GAME = "PLAYING"

        else:
            STATUT_GAME = "PAUSE"

    if pyxel.btn(pyxel.KEY_LEFT):
            global VIE
            
            mort()
    tir_fleche_joueur(PLAYER_X, PLAYER_Y)
    for fleches in LIST_FLECHES:
        
        mouv_fleche(fleches)
        
        verif_mort(fleches)
        
        

    

#TODO: attaque des mobs ennemis

def draw():
    
    global LISTE_ENTITES,STATUT_GAME
    
    
    
    

    if STATUT_GAME == "PLAYING":
        pyxel.cls(6)
        

        
            
        
    
        for i in range(VIE):
            pyxel.blt(4*(i+1), 5, 0, 115, 52, 10, 9, colkey=2)
        

        

        
        pyxel.blt(PLAYER_X, PLAYER_Y, 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(PLAYER_X-1, PLAYER_Y+5, 0, 32, 112, 16, 16, colkey=2)
        
        for entite in LISTE_ENTITES:
            mob(entite[0], entite[1], zombie)
        
        for fleche in LIST_FLECHES:
            creation_fleche(fleche[0], fleche[1])
    
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