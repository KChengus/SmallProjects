from Settings import settings


class Flappybird():
    def __init__(self, xPos, yPos):
        self.pos = [xPos, yPos]
        self.bird_ramp_up_multiplicator = 1
        self.bird_ramp_up_speed = 50
        self.isFlying = False
        
    def jump(self):
        pass

    def updatePos(self, xChange, yChange):
        self.pos[0] += xChange
        self.pos[1] += yChange