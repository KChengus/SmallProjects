
class Pipe:
    def __init__(self, xPos, yPos, width, height, picture_up, picture_down):
        self.width = width
        self.height = height
        self.pos = [xPos, yPos]
        self.picture_up = picture_up
        self.picture_down = picture_down
    

    def movePipe(self, xChange):
        self.pos[0] += xChange

