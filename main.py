# -*- coding: utf-8 -*-
"""
Created on Wed May 28 08:07:37 2025

@author: Hugo
"""

import pyxel
from random import randint

SCORE = 0







pyxel.init(128, 128, title="Chevalliay")

pyxel.load("2.pyxres")
WIDTH = pyxel.width
HEIGHT = pyxel.height


RESSOURCES_TUILES = {"TUILE_ZOMBIE" :[128,16, 12,14],
                     "TUILE_POTION_SOIN" : [16,48],
                     "SKIN_BALLES": [{"x":0,"y":80},{"x":16,"y":80},{"x":32,"y":80}],
                        "FLECHES": {"x":132,"y":72, "taille_x":9,"taille_y":1}
                     }
PLAYER = {"PLAYER_X" : 0 ,
          "PLAYER_Y" : 50,
            "VIE" :3,
              "ETAT" : ["NORMAL",0],
                "MODE": "PLAYING",
                "HITBOX" : 8,
                  "POTION" : 3,
                    "VITESSE" : 3,
                    "VIE_MAX" : 3}
LISTE_ENTITES =[]
LIST_FLECHES = []
HITBOX_ENNEMIS = 6

DEV = False

LIMITE_VITESSE_BALLES_NIVEAU = 3
TEMPS_IMMUNITE = 5
VITESSE_MAX_BALLES = 3
STATUT_GAME = "DIDACTICIEL"



def collision():
    '''Verifie les collisions entre le joueur et les balles ennemies'''
    global LISTE_ENTITES, PLAYER,LIMITE_VITESSE_BALLES_NIVEAU
    
    for v in LISTE_ENTITES:
        if v["valeur_x_balle"] <= PLAYER["PLAYER_X"] + PLAYER["HITBOX"] and v["valeur_x_balle"] >= PLAYER["PLAYER_X"] -PLAYER["HITBOX"]:
            # verifie les collisions sur les x
            if v["valeur_y_balle"] <= PLAYER["PLAYER_Y"] + PLAYER["HITBOX"]+5 and v["valeur_y_balle"] >= PLAYER["PLAYER_Y"] -PLAYER["HITBOX"]:
                # verifie les collisions sur les y
                try:
                    effet_vie("-1")
                    v["valeur_x_balle"] = -30
                    v["valeur_x_balle"] = v["valeur_x"]
                    v["vitesse_balle"] = randint(1,LIMITE_VITESSE_BALLES_NIVEAU)
                    
                except:
                    pass
                
    
                
            # si le bullet est inferieur 


def creation_mob():
        '''Cree les mages ennemis'''
        global LISTE_ENTITES,WIDTH,HEIGHT,LIMITE_VITESSE_BALLES_NIVEAU
        
        


        if randint(0, 5) == 0 and len(LISTE_ENTITES) < 8:
            tirage = randint(0,1)
            if tirage == 0:
                val_y = randint(10, HEIGHT//2)
            else:
                val_y = randint(HEIGHT//2, HEIGHT-10)

            val_x = WIDTH-12
            
            
            LISTE_ENTITES.append({"valeur_x": val_x, "valeur_y" :val_y, "valeur_x_balle" :val_x, "valeur_y_balle" :val_y, "vitesse_balle" :randint(1,LIMITE_VITESSE_BALLES_NIVEAU), "SKIN_BALLE":randint(0,2),"SUPR":False})
            
       
            


    

def effet_vie(effet):
    global TEMPS_IMMUNITE, PLAYER
    '''Degats recus par le joueur
        peut etre "+1" , "-1"
    '''
     
    if PLAYER["ETAT"][0] != "IMMUNITE" and not DEV:

        if effet == "-1":
            PLAYER["VIE"] -=1
            immunite(TEMPS_IMMUNITE)
            

    if effet == "+1":
        if PLAYER["VIE"] < PLAYER["VIE_MAX"]:
            PLAYER["VIE"] += 1
    
    if effet =="potion +1" and PLAYER["POTION"] >0 and PLAYER["VIE"] <PLAYER["VIE_MAX"]:
        PLAYER["VIE"] = PLAYER["VIE_MAX"]
        PLAYER["POTION"] -=1

            

def collision_ennemi():
    global HITBOX_ENNEMIS,SCORE
    
    for fleches in LIST_FLECHES:
        i = -1
        for ennemis in LISTE_ENTITES:
            i+=1
            try:
                if fleches["FLECHE_X"] > ennemis["valeur_x"] -HITBOX_ENNEMIS and fleches["FLECHE_X"] < ennemis["valeur_x"] +HITBOX_ENNEMIS:
                    if fleches["FLECHE_Y"] > ennemis["valeur_y"] -1 and fleches["FLECHE_Y"] < ennemis["valeur_y"] +14:
                        print("collision ennemi")
                        
                        print(ennemis["valeur_y"])
                        print(LISTE_ENTITES[i]["valeur_y"])
                        
                        del LISTE_ENTITES[i]["valeur_x"]
                        LISTE_ENTITES[i]["SUPR"] = "WAITING"
                        SCORE +=1
                        
            except:
                pass
                    



        



def mort():
    global STATUT_GAME,PLAYER
    STATUT_GAME = "END"

def creation_fleche():        
    """creation de fleches de list_fleche"""
    pyxel.blt(PLAYER["PLAYER_X"] +3, PLAYER["PLAYER_Y"] +7, 0, 132, 72, 8, 1)

def bouger_fleches():
    global LIST_FLECHES
    for v in LIST_FLECHES:
        v["FLECHE_X"] += v["VITESSE"]

def supr_sprite():
    i=-1
    for v in LISTE_ENTITES:
        i +=1
        if v["SUPR"] == True:
            del LISTE_ENTITES[i]

def update():
    global STATUT_GAME,PLAYER,VITESSE_MAX_BALLES, SCORE,LIST_FLECHES
    print(SCORE)

    if STATUT_GAME == 'DIDACTICIEL':
        if pyxel.btnp(pyxel.KEY_KP_ENTER) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
            STATUT_GAME = "PLAYING"

    
    

    if PLAYER["VIE"] == 0:
            mort()

    if PLAYER["ETAT"][0] == 'IMMUNITE':
            
        PLAYER["ETAT"][1] -= 1
        if PLAYER["ETAT"][1] == 0:
            PLAYER["ETAT"][0] = "NORMAL"
     
    



    if STATUT_GAME == "PLAYING":
        if pyxel.btnp(pyxel.KEY_H):
            STATUT_GAME = "DIDACTICIEL"
        creation_mob()
        bouger_balles()
        collision_ennemi()
        supr_sprite()
        try:
            bouger_fleches()
            

        except:
            pass

        
        
        pyxel.frame_count +=1
        if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_A):
            effet_vie("potion +1")

        if pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_X):  
            pyxel.play(0, 3,tick=1)
            LIST_FLECHES.append({"FLECHE_X": PLAYER["PLAYER_X"] +8,"FLECHE_Y": PLAYER["PLAYER_Y"] +8, "VITESSE":PLAYER["VITESSE"]})

        
        if pyxel.btn(pyxel.KEY_UP)or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_UP):
            
            if PLAYER["PLAYER_Y"] > 15:
                PLAYER["PLAYER_Y"] -= PLAYER["VITESSE"]
        
        

        elif pyxel.btn(pyxel.KEY_DOWN)or pyxel.btn(pyxel.GAMEPAD1_BUTTON_DPAD_DOWN):
            if PLAYER["PLAYER_Y"] < pyxel.height-20:
                PLAYER["PLAYER_Y"] += PLAYER["VITESSE"]
        collision()

        
    
    if pyxel.btnp(pyxel.KEY_RIGHT) or pyxel.btnp(pyxel.GAMEPAD1_BUTTON_START):
        
        if STATUT_GAME == "PAUSE":
            STATUT_GAME = "PLAYING"

        elif not STATUT_GAME == "END":
            STATUT_GAME = "PAUSE"

    if pyxel.btnp(pyxel.KEY_D) and PLAYER["MODE"]== "DEV":
            print("TEST de mort",mort())
    
    if STATUT_GAME == "END" and pyxel.btnp(pyxel.KEY_KP_ENTER) :
        
        global LISTE_ENTITES
        LISTE_ENTITES =[]
        LIST_FLECHES = []
        STATUT_GAME = "PLAYING"
        PLAYER = {"PLAYER_X" : 0 ,
          "PLAYER_Y" : 50,
            "VIE" :3,
              "ETAT" : ["NORMAL",0],
                "MODE": "DEV",
                "HITBOX" : 8,
                  "POTION" : 3,
                    "VITESSE" : 3,
                    "VIE_MAX" : 3}
        SCORE = 0
        
            

    
        
        
        
        
        
    return
    
def immunite(temps):
    '''Donne l'immotalite au joueur pendant la duree determinee'''
    global PLAYER
    temps_immunite = 30 * temps
    PLAYER["ETAT"] = ["IMMUNITE",temps_immunite]

    
def bouger_balles():
    global LIMITE_VITESSE_BALLES_NIVEAU, LISTE_ENTITES
    i = -1
    for v in LISTE_ENTITES:
        i += 1
        try:

            v["valeur_x_balle"] -= v["vitesse_balle"]
            if v["valeur_x_balle"] < -20:
                if v["SUPR"] == "WAITING":
                     v["SUPR"] = True

                v["valeur_x_balle"] = v["valeur_x"]
                
                v["vitesse_balle"] = randint(1,LIMITE_VITESSE_BALLES_NIVEAU)
                
        except:
            pass

    



def draw():
    global LISTE_ENTITES,STATUT_GAME,PLAYER,RESSOURCES_TUILES,SCORE

    if STATUT_GAME == 'DIDACTICIEL':
        pyxel.cls(6)
        pyxel.text(2, 10, "H : HELP", 8)
        pyxel.text(2, 18, "KEYBOARD commands:", 0)
        
        pyxel.text(2, 26, "UP/DOWN : Move player", 0)
        pyxel.text(2,34 , "LEFT : HEAL", 0)
        pyxel.text(2, 42, "RIGHT : PAUSE", 0)
        pyxel.text(2, 42+8, "SPACE : SHOOT", 0)


        pyxel.text(2, 62+8-5, "GAMEPAD commands:", 0)
        
        pyxel.text(2, 70+8-5, "UP/DOWN : Move player", 0)
        pyxel.text(2,78 +8-5, "B : HEAL", 0)
        pyxel.text(2, 86+8-5, "RIGHT : PAUSE", 0)
        pyxel.text(2, 86+8+8-5, "X : SHOOT", 0)

        pyxel.text(2, 86+8+8+8, "START or ENTER for start", 0)







        
        




    
    
    

    

    if STATUT_GAME == "PLAYING":
        pyxel.cls(6)
        
        

        
            
        
    
        for i in range(PLAYER["VIE"]):
            pyxel.blt(9*(i+1)-7, 5, 0, 115, 52, 10, 9, colkey=2)
        for i in range(PLAYER["POTION"]):
            pyxel.blt(20+7*(i+1),2 , 0, RESSOURCES_TUILES["TUILE_POTION_SOIN"][0], RESSOURCES_TUILES["TUILE_POTION_SOIN"][1], 16, 16, colkey=2)
        for v in LIST_FLECHES:
            pyxel.blt(v["FLECHE_X"], v["FLECHE_Y"],0,RESSOURCES_TUILES["FLECHES"]["x"],
                        RESSOURCES_TUILES["FLECHES"]["y"],RESSOURCES_TUILES["FLECHES"]["taille_x"],
                                                                                       RESSOURCES_TUILES["FLECHES"]["taille_y"])

        
        for v in LISTE_ENTITES:
            # affichage des balles
            
            pyxel.blt(v["valeur_x_balle"],v["valeur_y_balle"],0,0,80,-16,16, colkey=2)

        

        
        pyxel.text(55,7,f"SCORE:{SCORE}",0)
        pyxel.blt(PLAYER["PLAYER_X"], PLAYER["PLAYER_Y"], 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(PLAYER["PLAYER_X"] -1, PLAYER["PLAYER_Y"] +5, 0, 32, 112, 16, 16, colkey=2)
        
        for i in range(len(LISTE_ENTITES)):
            try:

                pyxel.blt(LISTE_ENTITES[i]["valeur_x"], LISTE_ENTITES[i]["valeur_y"], 0, RESSOURCES_TUILES["TUILE_ZOMBIE"][0], RESSOURCES_TUILES["TUILE_ZOMBIE"][1], RESSOURCES_TUILES["TUILE_ZOMBIE"][2],RESSOURCES_TUILES["TUILE_ZOMBIE"][3], colkey=2)
            except:
                pass
        
    
    if STATUT_GAME == "END":
        
        
        

        
        
        
        


        
        pyxel.cls(6)
        
        pyxel.blt(PLAYER["PLAYER_X"],PLAYER["PLAYER_Y"], 0,48,112, 16,16, colkey=2)
        pyxel.blt(PLAYER["PLAYER_X"]-1, PLAYER["PLAYER_Y"]+5, 0, 32, 112, 16, 16, colkey=2)

        
        
        
    
    
        if pyxel.frame_count % 30 < 25:  # visible pendant 15 frames sur 30
            pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "You Lose", 7)
            
            chaine_de_caractere = "PUSH ENTER TO START"
            # pyxel.text((pyxel.height-114)//2, (pyxel.width-114)//2, 7)
            pyxel.text((pyxel.width - len(chaine_de_caractere) * 4) // 2, (pyxel.height - 8) // 2, chaine_de_caractere, 7)
            pyxel.text((pyxel.width - len(f"Score: {SCORE}") * 4) // 2, (pyxel.height - 8) // 2+7, f"Score: {SCORE}", 0)

        
    
    if STATUT_GAME == "PAUSE":
        pyxel.text((pyxel.height-30)//2, (pyxel.width-30)//2, "PAUSE", 7)





pyxel.run(update, draw)