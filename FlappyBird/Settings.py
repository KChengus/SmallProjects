import pygame
class settings:
    running = True
    display_width = 800
    display_height = 600

    fps = 100

    # high score
    highScoreFile = "highScore.txt"


    # bird settings
    bird_ramp_up_multiplicator = 1
    bird_ramp_up_speed = 2
    flappy_bird_size = (50, 50)
    display_center = (display_width // 2, display_height // 2)

    # pipe settings
    CREATE_PIPE_TIME = 1500
    pipe_speed = -2
    pipe_width = 50
    distance_pipe = 200
    color = {"white" : (255, 255, 255), "black": (0, 0, 0), "blue": (0, 0, 255), "red": (255, 0, 0), "green": (0, 255, 0)}

