import os
from pathlib import Path

product_path = Path("text_folder/product.txt")

picture_files = [file_name[:-4] for file_name in os.listdir("picture_folder")] # remove .png from picture name

products = list()
with open(product_path, "r") as f:

    for line in f.readlines():
        products.append(line.split()[0])
    print(products)

with open(product_path, 'a') as f:
    for picture_file in picture_files:
        if picture_file not in products:
            average_price = int(input("Type the Average Price for " + picture_file + '\n'))
            f.write('\n' + picture_file + ' ' + str(average_price))

print("Done")