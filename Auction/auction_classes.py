import pygame
from pathlib import Path

buyer_hand_width = 75
buyer_hand_height = 150

buyer_hand_path = Path("animation_folder/auction_hand.png")

auctioneer_width = 75
auctioneer_height = 100
auctioneer_path = "animation_folder/auctioneer.png"

buyers_info_path = "text_folder/people.txt"


# product instance initializer
all_product_instances = list()
product_file = "text_folder/product.txt"
product_and_price = {}
auction_item_dimension_width = 200
auction_item_dimension_height = 100


class People:
    def __init__(self, money):
        self.money = money


class Buyer(People):
    def __init__(self, name, age, social_class, money, id):
        super().__init__(money)
        self.name = name
        self.age = age
        self.social_class = social_class
        self.id = id

    bought_items = {}
    # hand picture
    auction_hand_picture = pygame.image.load(buyer_hand_path)
    auction_hand_picture = pygame.transform.scale(auction_hand_picture, (buyer_hand_width, buyer_hand_height))
    x = y = 0
    # If the bidding price is within their money range, return True otherwise False

    def bid(self, bid_price):
        if (self.money >= bid_price):
            return True
        else:
            return False

    def buy(self, price, product):
        self.bought_items[product] = price
        self.money += price


class Auctioneer(People):
    def __init__(self, money):
        super().__init__(money)
        self.available_items = list()
        auctioneer_picture = pygame.image.load(auctioneer_path)
        self.auctioneer_picture = pygame.transform.scale(auctioneer_picture, (auctioneer_width, auctioneer_height))
        self.current_buyer = None

    def sold(self, price):
        self.money += price

    def sold_item(self, item):
        self.available_items.remove(item)


class Product:
    def __init__(self, name, average_price, image):
        self.name = name
        self.average_price = average_price
        self.image = image


# auctioneer
auctioneer_money = 10 ** 5
auctioneer = Auctioneer(auctioneer_money)

# Buyers text file. The number of rows represents the num of buyers
# Each row has four columns. (Name Age Class Money)
buyers_instances = list()
with open(buyers_info_path, "r") as f:
    for i, buyers_attribute in enumerate(f.readlines()):
        buyers_attribute = buyers_attribute.split(" ")
        if (len(buyers_attribute) == 4):
            name, age, social_class, money = buyers_attribute
            buyer = Buyer(name, int(age), social_class, int(money), i + 1)
            buyers_instances.append(buyer)





with open(product_file, "r") as f:
    for prod in f.readlines():
        product_name, average_price = prod.split()

        product_and_price[product_name] = average_price

for product_name, price in product_and_price.items():
    name = product_name.replace("_", " ")
    path = Path("picture_folder/" + product_name + ".png")
    image = pygame.image.load(path)
    image = pygame.transform.scale(image, (auction_item_dimension_width, auction_item_dimension_height))
    product_instance = Product(name, int(price), image)
    all_product_instances.append(product_instance)




