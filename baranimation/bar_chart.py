import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

import random

# Functions

def countFreqOfLetters():
    # gather words in list
    file = "baranimation\\allWords.txt"
    arrWords = list()
    with open(file, "r") as f:
        arrWords = f.read().strip().split("\n")

    # break down each word and count freq of letters
    d = dict()
    for word in arrWords:
        for letter in word:
            if (letter not in d):
                d[letter] = 0
            d[letter] += 1
    d = sorted(d.items(), key=lambda x: x[0])
    print(d)
    return d

lst1=[random.randint(0, 100) for i in range(1000)]
lst2=[random.randint(0, 100) for i in range(100000)]
fig = plt.figure(figsize = (8,6))


ax = fig.add_subplot(111)
ax.set_ylim([0, 100])
bar = ax.bar(["one", "two"], [0, 0])

def animate(i):
    global bar
    print(i)
    y1=lst1[i]
    y2=lst2[i]
    bar.remove()
    bar = ax.bar(["one", "two"], [y1,y2], color="b")

# VARIABLES

# freqOfLetters is a 2d array because of sorted function
freqOfLetters = countFreqOfLetters()
N = len(freqOfLetters)
ind = np.arange(N)



# matplotlib graph


plt.style.use("seaborn")

# plt.bar(ind, [i[1] for i in freqOfLetters])

ani = FuncAnimation(fig, animate, interval=100)

# ax.set_xticks(ind, labels=[i[0] for i in freqOfLetters])
# ax.bar(ind, [i[1] for i in freqOfLetters], 0.35)
# show the graph
plt.show()