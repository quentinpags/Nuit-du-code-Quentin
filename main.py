# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint










pyxel.init(128, 128, title="Chevalliay")

pyxel.load("2.pyxres")
WIDTH = pyxel.width
HEIGHT = pyxel.height


RESSOURCES_TUILES = {"TUILE_ZOMBIE" :[128,16, 12,14],
                     "TUILE_POTION_SOIN" : [16,48],
                     "SKIN_BALLES": [{"x":0,"y":80},{"x":16,"y":80},{"x":32,"y":80}]
                     }
PLAYER = {"PLAYER_X" : 0 ,
          "PLAYER_Y" : 50,
            "VIE" :3,
              "ETAT" : ["NORMAL",0],
                "MODE": "DEV",
                "HITBOX" : 8,
                  "POTION" : 3,
                    "VITESSE" : 3,
                    "VIE_MAX" : 3}
LISTE_ENTITES =[]



LIMITE_VITESSE_BALLES_NIVEAU = 3
TEMPS_IMMUNITE = 5

STATUT_GAME = "PLAYING"



def collision():
    '''Verifie les collisions entre le joueur et les balles ennemies'''
    global LISTE_ENTITES, PLAYER,LIMITE_VITESSE_BALLES_NIVEAU
    
    for v in LISTE_ENTITES:
        if v["valeur_x_balle"] <= PLAYER["PLAYER_X"] + PLAYER["HITBOX"] and v["valeur_x_balle"] >= PLAYER["PLAYER_X"] -PLAYER["HITBOX"]:
            # verifie les collisions sur les x
            if v["valeur_y_balle"] <= PLAYER["PLAYER_Y"] + PLAYER["HITBOX"]+5 and v["valeur_y_balle"] >= PLAYER["PLAYER_Y"] -PLAYER["HITBOX"]:
                # verifie les collisions sur les y
                print('collision', v)
                v["valeur_x_balle"] = v["valeur_x"]
                v["vitesse_balle"] = randint(1,LIMITE_VITESSE_BALLES_NIVEAU)
                effet_vie("-1")
                
    
                
            # si le bullet est inferieur 


def creation_mob():
        '''Cree les mages ennemis'''
        global LISTE_ENTITES,WIDTH,HEIGHT,LIMITE_VITESSE_BALLES_NIVEAU
        
        
        


        if randint(0, 5) == 0 and len(LISTE_ENTITES) < 8:
            if len(LISTE_ENTITES) <4:
                val_y = randint(10, HEIGHT//2)
            else:
                val_y = randint(HEIGHT//2, HEIGHT-10)

            val_x = WIDTH-12
            
            
            LISTE_ENTITES.append({"valeur_x": val_x, "valeur_y" :val_y, "valeur_x_balle" :val_x, "valeur_y_balle" :val_y, "vitesse_balle" :randint(1,LIMITE_VITESSE_BALLES_NIVEAU), "SKIN_BALLE":randint(0,2)})
            
       
            


    

def effet_vie(effet):
    global TEMPS_IMMUNITE, PLAYER
    '''Degats recus par le joueur
        peut etre "+1" , "-1"
    '''
     
    if PLAYER["ETAT"][0] != "IMMUNITE":

        if effet == "-1":
            PLAYER["VIE"] -=1
            immunite(TEMPS_IMMUNITE)
            

    if effet == "+1":
        if PLAYER["VIE"] < PLAYER["VIE_MAX"]:
            PLAYER["VIE"] += 1
    
    if effet =="potion +1" and PLAYER["POTION"] >0 and PLAYER["VIE"] <PLAYER["VIE_MAX"]:
        PLAYER["VIE"] = PLAYER["VIE_MAX"]
        PLAYER["POTION"] -=1

            




def mort():
    global STATUT_GAME
    STATUT_GAME = "END"

    
    
def update():
    global STATUT_GAME,PLAYER
    

    if PLAYER["VIE"] == 0:
            mort()

    if PLAYER["ETAT"][0] == 'IMMUNITE':
            
        PLAYER["ETAT"][1] -= 1
        if PLAYER["ETAT"][1] == 0:
            PLAYER["ETAT"][0] = "NORMAL"
     
    
    
    if STATUT_GAME == "PLAYING":
        creation_mob()
        bouger_balles()
    
        pyxel.frame_count +=1
        if pyxel.btnp(pyxel.KEY_LEFT):
            effet_vie("potion +1")


        if pyxel.btn(pyxel.KEY_UP):
            
            if PLAYER["PLAYER_Y"] > 15:
                PLAYER["PLAYER_Y"] -= PLAYER["VITESSE"]
        
        

        elif pyxel.btn(pyxel.KEY_DOWN):
            if PLAYER["PLAYER_Y"] < pyxel.height-20:
                PLAYER["PLAYER_Y"] += PLAYER["VITESSE"]
        collision()

        

    if pyxel.btnp(pyxel.KEY_RIGHT):
        
        if STATUT_GAME == "PAUSE":
            STATUT_GAME = "PLAYING"

        elif not STATUT_GAME == "END":
            STATUT_GAME = "PAUSE"

    if pyxel.btnp(pyxel.KEY_T) and PLAYER["MODE"]== "DEV":
            print("TEST de mort",mort())
            
            

    
        
        
        
        
        
    return
    
def immunite(temps):
    '''Donne l'immotalite au joueur pendant la duree determinee'''
    global PLAYER
    temps_immunite = 30 * temps
    PLAYER["ETAT"] = ["IMMUNITE",temps_immunite]

    
def bouger_balles():
    global LIMITE_VITESSE_BALLES_NIVEAU
    
    for v in LISTE_ENTITES:
        v["valeur_x_balle"] -= v["vitesse_balle"]
        if v["valeur_x_balle"] < -20:
            v["valeur_x_balle"] = v["valeur_x"]
            v["vitesse_balle"] = randint(1,LIMITE_VITESSE_BALLES_NIVEAU)

    



def draw():
    global LISTE_ENTITES,STATUT_GAME,PLAYER
    
    
    
    

    if STATUT_GAME == "PLAYING":
        pyxel.cls(6)
        

        
            
        
    
        for i in range(PLAYER["VIE"]):
            pyxel.blt(9*(i+1)-7, 5, 0, 115, 52, 10, 9, colkey=2)
        for i in range(PLAYER["POTION"]):
            pyxel.blt(20+7*(i+1),2 , 0, RESSOURCES_TUILES["TUILE_POTION_SOIN"][0], RESSOURCES_TUILES["TUILE_POTION_SOIN"][1], 16, 16, colkey=2)
        
        
        for v in LISTE_ENTITES:
            # affichage des balles
            
            pyxel.blt(v["valeur_x_balle"],v["valeur_y_balle"],0,0,80,-16,16, colkey=2)

        

        
        pyxel.blt(PLAYER["PLAYER_X"], PLAYER["PLAYER_Y"], 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(PLAYER["PLAYER_X"] -1, PLAYER["PLAYER_Y"] +5, 0, 32, 112, 16, 16, colkey=2)
        
        for i in range(len(LISTE_ENTITES)):
            pyxel.blt(LISTE_ENTITES[i]["valeur_x"], LISTE_ENTITES[i]["valeur_y"], 0, RESSOURCES_TUILES["TUILE_ZOMBIE"][0], RESSOURCES_TUILES["TUILE_ZOMBIE"][1], RESSOURCES_TUILES["TUILE_ZOMBIE"][2],RESSOURCES_TUILES["TUILE_ZOMBIE"][3], colkey=2)
        
        
    
    if STATUT_GAME == "END":
        
        

        
        
        
        


        
        pyxel.cls(6)
        
        pyxel.blt(PLAYER["PLAYER_X"],PLAYER["PLAYER_Y"], 0,48,112, 16,16, colkey=2)
        pyxel.blt(PLAYER["PLAYER_X"]-1, PLAYER["PLAYER_Y"]+5, 0, 32, 112, 16, 16, colkey=2)

        
        
        
    
    
        if pyxel.frame_count % 30 < 25:  # visible pendant 15 frames sur 30
            pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "You Lose", 7)
            chaine_de_caractere = "PUSH ENTER TO START"
            # pyxel.text((pyxel.height-114)//2, (pyxel.width-114)//2, 7)
            pyxel.text((pyxel.width - len(chaine_de_caractere) * 4) // 2, (pyxel.height - 8) // 2, chaine_de_caractere, 7)
    
    if STATUT_GAME == "PAUSE":
        pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "PAUSE", 7)





pyxel.run(update, draw)