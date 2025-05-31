# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint
TUILE_ZOMBIE =[[128,16, 12,14]]#position de tuile
SKIN = 0

HITBOX = 8
LISTE_ENTITES =[]
LIMITE_VITESSE_BALLES_NIVEAU = 3


pyxel.init(128, 128, title="Chevalliay")
#play(0, 2,loop= True)#import de sons
pyxel.load("2.pyxres")
WIDTH = pyxel.width
HEIGHT = pyxel.height





PLAYER_X = 0
PLAYER_Y = 50
VITESSE = 3
MODE = "PLAYER"
VIE = 3
STATUT_GAME = "PLAYING"



def collision():
    '''renvoie true s'il y a collision'''
    global LISTE_ENTITES, PLAYER_X,PLAYER_Y,HITBOX,LIMITE_VITESSE_BALLES_NIVEAU
    
    for v in LISTE_ENTITES:
        if v[2] <= PLAYER_X + HITBOX and v[2] >= PLAYER_X-HITBOX:
            # verifie les collisions sur les x
            if v[3] <= PLAYER_Y + HITBOX+5 and v[3] >= PLAYER_Y-HITBOX:
                # verifie les collisions sur les y
                print('collision')
                v[3] += WIDTH
                v[4] = randint(1,LIMITE_VITESSE_BALLES_NIVEAU)
                degats_player("-1")
    
                
            # si le bullet est inferieur 


def creation_mob():
        global LISTE_ENTITES,WIDTH,HEIGHT,LIMITE_VITESSE_BALLES_NIVEAU
        
        
        


        if randint(0, 5) == 0 and len(LISTE_ENTITES) < 8:
            if len(LISTE_ENTITES) <4:
                val_y = randint(10, HEIGHT//2)
            else:
                val_y = randint(HEIGHT//2, HEIGHT-10)

            val_x = WIDTH-12
            
            
            LISTE_ENTITES.append([val_x, val_y,val_x,val_y, randint(1,LIMITE_VITESSE_BALLES_NIVEAU)])
            
       
            


    

def degats_player(effet):
    '''Degats recus par le joueur
        peut etre "+1" , "-1"
    '''
    global MODE, VIE
    if MODE == "DEV":
        return
    if effet == "-1":
        VIE -=1
        

    if effet == "+1":
        if VIE < 3:
            VIE += 1

    
            




def mort():
    global STATUT_GAME
    STATUT_GAME = "END"

    
    
def update():
    global SKIN,STATUT_GAME,VIE

    if VIE == 0:
            mort()
     
    
    
    if STATUT_GAME == "PLAYING":
        creation_mob()
        bouger_balles()
    
        pyxel.frame_count +=1

        if pyxel.btn(pyxel.KEY_UP):
            global PLAYER_Y, VITESSE
            if PLAYER_Y > 15:
                PLAYER_Y -= VITESSE
            

        elif pyxel.btn(pyxel.KEY_DOWN):
            if PLAYER_Y < pyxel.height-20:
                PLAYER_Y += VITESSE
        collision()

        

    if pyxel.btnp(pyxel.KEY_RIGHT):
        
        if STATUT_GAME == "PAUSE":
            STATUT_GAME = "PLAYING"

        elif not STATUT_GAME == "END":
            STATUT_GAME = "PAUSE"

    if pyxel.btn(pyxel.KEY_LEFT):
            
            mort()
            

    
        
        
        
        
        
    return
    
    
    
def bouger_balles():
    global VITESSE_BALLES, LIMITE_VITESSE_BALLES_NIVEAU
    
    for v in LISTE_ENTITES:
        v[2] -= v[4]
        if v[2] < -20:
            v[2] = v[0]
            v[4] = randint(1,LIMITE_VITESSE_BALLES_NIVEAU)

    



def draw():
    global LISTE_ENTITES,STATUT_GAME,PLAYER_X, PLAYER_Y,LISTE_BALLES
    
    
    
    

    if STATUT_GAME == "PLAYING":
        pyxel.cls(6)
        

        
            
        
    
        for i in range(VIE):
            pyxel.blt(4*(i+1), 5, 0, 115, 52, 10, 9, colkey=2)
        
        
        for v in LISTE_ENTITES:
            # affichage des balles
            pyxel.blt(v[2],v[3],0,0,80,-16,16, colkey=2)

        

        
        pyxel.blt(PLAYER_X, PLAYER_Y, 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(PLAYER_X-1, PLAYER_Y+5, 0, 32, 112, 16, 16, colkey=2)
        
        for i in range(len(LISTE_ENTITES)):
            pyxel.blt(LISTE_ENTITES[i][0], LISTE_ENTITES[i][1], 0, TUILE_ZOMBIE[SKIN][0], TUILE_ZOMBIE[SKIN][1], TUILE_ZOMBIE[SKIN][2],TUILE_ZOMBIE[SKIN][3], colkey=2)
        
        
    
    if STATUT_GAME == "END":
        
        

        
        
        
        


        
        pyxel.cls(6)
        
        pyxel.blt(PLAYER_X,PLAYER_Y, 0,48,112, 16,16, colkey=2)
        pyxel.blt(PLAYER_X-1, PLAYER_Y+5, 0, 32, 112, 16, 16, colkey=2)

        
        
        
    
    
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