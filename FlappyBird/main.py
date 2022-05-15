import random
import pygame
from Pipe import Pipe
from Settings import settings
from Bird import Flappybird
pygame.init()

class Game(settings):

    def __init__(self):
        # display
        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        # picture
        self.fBird = Flappybird(200, 200)
        picture = pygame.image.load("fb_pictures/fBird.png")
        self.picture = pygame.transform.scale(picture, self.flappy_bird_size)

        # create events
        self.create_pipe_event = pygame.USEREVENT + 1

        # set timed events
        pygame.time.set_timer(self.create_pipe_event, self.CREATE_PIPE_TIME)

        self.pipes = list()


    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.bird_ramp_up_multiplicator = -5
            elif event.type == self.create_pipe_event:

                pic_down_height = random.randint(0, self.display_height - self.distance_pipe*2)

                # create pipe image
                picture_down = pygame.image.load("fb_pictures/pipe_image.png")
                picture_down = pygame.transform.rotate(picture_down, 180)
                picture_down = pygame.transform.scale(picture_down, (self.pipe_width, pic_down_height))
                
                picture_up = pygame.image.load("fb_pictures/pipe_image.png")
                picture_up = pygame.transform.scale(picture_up, (self.pipe_width, self.display_height - self.distance_pipe - pic_down_height))

                # create pipe object
                self.pipes.append(Pipe(self.display_height, pic_down_height + self.distance_pipe, self.pipe_width, pic_down_height, picture_up, picture_down))

    def background(self):
        self.display.fill(self.color["white"])

    def updatePos(self):
        self.fBird.updatePos(0, self.bird_ramp_up_speed * self.bird_ramp_up_multiplicator)
        self.bird_ramp_up_multiplicator += 0.2

        for pipe in self.pipes:
            pipe.movePipe(self.pipe_speed)

    def draw_picture(self):
        # draw bird
        # delete pipes that go overboard
        if self.pipes and self.pipes[0].pos[0] < 0:
            self.pipes.pop(0)

        for pipe in self.pipes:
            self.display.blit(pipe.picture_up, pipe.pos)
            self.display.blit(pipe.picture_down, (pipe.pos[0], 0))
            
        self.display.blit(self.picture, self.fBird.pos)

    def detectCollision(self):
        # bird position and size
        # pipes position and size
        xPosBird, yPosBird = self.fBird.pos
        for pipe in self.pipes:
            if (xPosBird <= pipe.pos[0] <= xPosBird + self.flappy_bird_size[0]):
                if (0 <= yPosBird <= pipe.height or pipe.height + self.distance_pipe <= yPosBird + self.flappy_bird_size[0] <= self.display_height):                        
                    self.running = False
                break
            elif (xPosBird < pipe.pos[0]):
                break
        
    def main(self):
        clock = pygame.time.Clock()
        while self.running:
            self.background()
            self.handle_event()
            self.updatePos()
            self.draw_picture()
            self.detectCollision()
            pygame.display.update()
            clock.tick(self.fps)


if __name__ == "__main__":
    Game().main()
    pygame.quit()