import pyxel
width = 128
height = 128

pyxel.init(width, height, title='cheuvalliay')
pyxel.load("2.pyxres")

class Perso:
    def __init__(self):
        self.width = width
        self.height = height
        self.x = width//2
        self.y = height//2


        pyxel.run(self.update, self.draw)


        def update():
            if pyxel.btn(pyxel.KEY_RIGHT):
                self.x += 1

        def draw():
            pyxel.blt(self.x, self.y, 0, 0, 16, 16, 16)