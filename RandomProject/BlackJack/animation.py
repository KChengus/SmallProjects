import pygame

import main
pygame.init()

class Card_position:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image
# display settings
display_width = 800
display_height = 600

# render the window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("BlackJack")

# variables
run = True
directory = "C:\\Users\\Kevin\\PycharmProjects\\pythonProject\\BlackJack\\cards_folder"

card_instances = list()
space_between_cards = 20
player_card_x_beginning_pos = 320
player_card_y_beginning_pos = 50
player_card_x_current_pos = player_card_x_beginning_pos
player_card_y_current_pos = player_card_y_beginning_pos


#images
cards_width = 700 // 10
cards_height = 1100 // 10

# functions
def make_image(file_name):
    print(file_name)
    return pygame.image.load('cards_folder\\' + file_name)

def display_cards(x, y, image):
    display = pygame.transform.scale(image, (cards_width, cards_height))
    gameDisplay.blit(display, (x, y))


def animation():
    pass

def reset():
    pass

# Before loop
game = main.Game()
#game.main()

# loop
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # draw card
            if game.players_turn:
                picked_card = game.player.play()
                img = make_image(picked_card + '.png')
                new_card = Card_position(player_card_x_current_pos, player_card_y_current_pos, img)
                card_instances.append(new_card)
                player_card_x_current_pos += space_between_cards
                if not game.player._continue():
                    game.players_turn = False
                    player_card_x_current_pos = player_card_x_beginning_pos
                    player_card_y_current_pos = player_card_y_beginning_pos + 350
            else:
                picked_card = game.player.play()
                img = make_image(picked_card + '.png')
                new_card = Card_position(player_card_x_current_pos, player_card_y_current_pos, img)
                card_instances.append(new_card)
                player_card_x_current_pos += space_between_cards
                if not game.dealer._continue():
                    game.ending(50)


    for card_instance in card_instances:
        display_cards(card_instance.x, card_instance.y, card_instance.image)

    pygame.display.update()

pygame.quit()