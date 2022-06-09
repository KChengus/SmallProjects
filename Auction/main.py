from itertools import product
from pathlib import Path
import pygame
import auction_classes as ac
import random
import time
from math import floor
pygame.init()



# display settings
display_width = 800
display_height = 600
clock = pygame.time.Clock()
clock.tick(30)

# render the window
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Auction")
auction_hall_path = Path("animation_folder/auction_hall.png")
background = pygame.image.load(auction_hall_path)
background = pygame.transform.scale(background, (display_width, display_height))

# settings
current_product = random.choice(ac.all_product_instances)
running = True
current_time = time.time()
prev_time = 0
time_limit = 10

myfont = pygame.font.SysFont("monospace", 20)
labels = [ myfont.render("1", 1, (0,0,0)), myfont.render("2", 1, (0,0,0)),
        myfont.render("3", 1, (0,0,0)), myfont.render("4", 1, (0,0,0)) ]


background_pos = (0, 0)
auctioneer_pos = (355, 300)
product_pos = (300, 200)
buyer_hand_pos = [(100, 300), (200, 400), (500, 300), (600, 400)]

def change_picture(current_picture):
    choice = random.choice(ac.all_product_instances)
    if (choice == current_picture):

        return change_picture(current_picture)
    return choice

def bid_money(buyer, current_product_price):
    # TODO set a time limimt
    global current_time, prev_time
    current_time = time.time()
    prev_time = 0
    if (buyer.money < current_product_price):
        return current_product_price
    money = -1
    while (money <= current_product_price or money > buyer.money):
        print(f"Buyer Id: {buyer.id}\tBuyer Name: {buyer.name}\tYour Money: {buyer.money}\tCost: {current_product_price}")
        money = int(input("Enter Your Bidding Price (-1 for cancel):\n"))
        if (money == -1):
            current_time = time.time()

            return current_product_price
    ac.auctioneer.current_buyer = buyer.name
    print(f"The product now costs {money}. The current bidder is currently number {buyer.name}")
    current_time = time.time()
    return money


print("Current price of " + current_product.name + ": " + str(current_product.average_price))
print("type 1 through 4 to bid money of whom with that associated number")
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                current_product = change_picture(current_product)
                print(current_product.average_price)

            if event.key == pygame.K_1:
                current_product.average_price = bid_money(ac.buyers_instances[0], current_product.average_price)
            elif event.key == pygame.K_2:
                current_product.average_price = bid_money(ac.buyers_instances[1], current_product.average_price)
            elif event.key == pygame.K_3:
                current_product.average_price = bid_money(ac.buyers_instances[2], current_product.average_price)
            elif event.key == pygame.K_4:
                current_product.average_price = bid_money(ac.buyers_instances[3], current_product.average_price)

    # handle time
    diff = floor(time.time() - current_time)
    if (diff > prev_time):
        prev_time = diff
        print(diff)
    if (diff >= time_limit):
        running = False

    # display pictures
    gameDisplay.blit(background, background_pos)
    gameDisplay.blit(ac.auctioneer.auctioneer_picture, auctioneer_pos)
    gameDisplay.blit(current_product.image, product_pos)

    for i, buyers in enumerate(ac.buyers_instances):
        gameDisplay.blit(buyers.auction_hand_picture, buyer_hand_pos[i])
        gameDisplay.blit(labels[i], (buyer_hand_pos[i][0]+35, buyer_hand_pos[i][1]+35))

    pygame.display.update()

if ac.auctioneer.current_buyer:
    print("Sold to " + ac.auctioneer.current_buyer)

pygame.quit()
