'''
__________________________________________________________________
Created By: George Shea                                    ßeta
Date Created: 2/12/2019
Version: 2.0
Version Update: 5/12/2019

Use:
this program is a simple slot machine
__________________________________________________________________
'''

import random
from graphics import *

def main():
    # full a complete game background
    window = GraphWin( "Slots Game", 500,500)
    window.setCoords(0.0, 0.0, 500, 500)

    # backdrop
    rec = Rectangle(Point(0,0), Point(500,500)).draw(window)
    rec.setFill('black')

    # background
    rec = Rectangle(Point(20,0), Point(480,500)).draw(window)
    rec.setFill('DarkOrange4')
    rec.setOutline('DarkOrange4')


    #
    rec = Rectangle(Point(30,30), Point(130,340)).draw(window)
    rec.setFill('white')
    rec.setWidth(2)

    rec = Rectangle(Point(160,30), Point(260,340)).draw(window)
    rec.setFill('white')
    rec.setWidth(2)

    rec = Rectangle(Point(290,30), Point(390,340)).draw(window)
    rec.setFill('white')
    rec.setWidth(2)

    rec = Rectangle(Point(130, 155), Point(160,180)).draw(window)
    rec.setFill('tan4')
    rec.setWidth(2)

    rec = Rectangle(Point(260, 155), Point(290,180)).draw(window)
    rec.setFill('tan4')
    rec.setWidth(2)

    while True:
        window.getMouse()
        # spot 1 bottom left hand corner
        choice = random.randint(1,5)
        dx = 40
        dx2 = 40
        dy = 120
        dy2 = 120
        if choice == 1:
            cherry = Rectangle(Point(dx,dx2), Point(dy,dy2)).draw(window)
            cherry.setFill('red3')
            slotOne = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx,dx2), Point(dy,dy2)).draw(window)
            lemon.setFill('gold')
            slotOne = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx,dx2), Point(dy,dy2)).draw(window)
            orange.setFill('orange')
            slotOne = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx,dx2), Point(dy,dy2)).draw(window)
            apple.setFill('lime')
            slotOne = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx,dx2), Point(dy,dy2)).draw(window)
            grape.setFill('magenta4')
            slotOne = "Purple"

        # 2 slots middle bottom

        choice = random.randint(1, 5)
        dx = 170
        dx2 = 250
        dy = 40
        dy2 = 120
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotTwo = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotTwo = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotTwo = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotTwo = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotThree = "Purple"

        # slot 3 bottom right corner
        choice = random.randint(1, 5)
        dx = 300
        dx2 = 380
        dy = 40
        dy2 = 120
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotThree = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotThree = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotThree = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotThree = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotThree = "Purple"

        # slot 4 bottom right corner
        choice = random.randint(1, 5)
        dx = 40
        dx2 = 120
        dy = 140
        dy2 = 220
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotFour = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotFour = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotFour = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotFour = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotFour = "Purple"

        # slot 5 bottom right corner
        choice = random.randint(1, 5)
        dx = 170
        dx2 = 250
        dy = 140
        dy2 = 220
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotFive = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotFive = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotFive = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotFive = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotFive = "Purple"

        # slot 6 bottom right corner
        choice = random.randint(1, 5)
        dx = 300
        dx2 = 380
        dy = 140
        dy2 = 220
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotSix = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotSix = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotSix = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotSix = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotSix = "Purple"

        # slot 7 bottom right corner
        choice = random.randint(1, 5)
        dx = 40
        dx2 = 120
        dy = 240
        dy2 = 320
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotSeven = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotSeven = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotSeven = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotSeven = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotSeven = "Purple"

        # slot 8 bottom right corner
        choice = random.randint(1, 5)
        dx = 170
        dx2 = 250
        dy = 240
        dy2 = 320
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotEight = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotEight = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotEight = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotEight = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotEight = "Purple"

        # slot 9 bottom right corner
        choice = random.randint(1, 5)
        dx = 300
        dx2 = 380
        dy = 240
        dy2 = 320
        if choice == 1:
            cherry = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            cherry.setFill('red3')
            slotNine = "Red"
        if choice == 2:
            lemon = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            lemon.setFill('gold')
            slotNine = "Gold"
        if choice == 3:
            orange = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            orange.setFill('orange')
            slotNine = "Orange"
        if choice == 4:
            apple = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            apple.setFill('lime')
            slotNine = "Lime"
        if choice == 5:
            grape = Rectangle(Point(dx, dy), Point(dx2, dy2)).draw(window)
            grape.setFill('magenta4')
            slotNine = "Purple"

        if slotFour == slotFive and slotFive == slotSix:
            text = Text(Point(250,400), "You Are Winner").draw(window)
            text.setSize(12)
            window.getMouse()
            text.undraw()




main()
