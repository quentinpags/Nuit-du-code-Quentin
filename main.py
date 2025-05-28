import pyxel
width = 128
height = 128

pyxel.init(width, height, title='cheuvalliay')

class Perso:
    def __init__(self):
        self.width = width
        self.height = height
        self.x = width//2
        self.y = height//2


        pyxel.run(self.update, self.draw)


        def update():
            pass

        def draw():
            pass