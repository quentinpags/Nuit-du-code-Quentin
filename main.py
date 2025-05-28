import pyxel

width = 128
height = 128
MODE ="DEV"

pyxel.init(width, height, title='cheuvalliay')
pyxel.load("2.pyxres")

class Perso:
    def __init__(self):
        self.width = width
        self.height = height
        self.x = width//2
        self.y = height//2
        print("self.y", self.y)


        pyxel.run(self.update, self.draw)


    def update(self):
        # if pyxel.btn(pyxel.KEY_RIGHT):
        #     self.x += 1
        #     print(self.x)
        # elif pyxel.btn(pyxel.KEY_LEFT):
        #     self.x -= 1
        if pyxel.btn(pyxel.KEY_UP):
            self.y += -1
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += +1


    def draw(self):
        pyxel.cls(0)
        pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16, colkey=2, )
        pyxel.blt(self.x, self.y+8, 0, 32, 112, 16, 16, colkey=2)


        

        
        
        
        
        




Perso()
