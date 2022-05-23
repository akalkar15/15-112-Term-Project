add_library("minim")
from buttons import button 
from mode2 import songFunctions
from visuals import star
import random 
import time
song = None

class setUps():
    def start(self):
        global starterBg
        starterBg = loadImage("pastel.jpg")
        global f
        f = loadFont("Trebuchet-BoldItalic-100.vlw")
        f2 = loadFont("TrebuchetMS-Bold-30.vlw")
        f3 = loadFont("Trebuchet-BoldItalic-60.vlw")
        smallF = loadFont("AndaleMono-20.vlw")
        medF = loadFont("AndaleMono-30.vlw")
        goButton = button(width/2 + 50, height/2 - 100, 250, 150, "GO!")
        questionB = button(width - 100, height - 80, 70, 50, "?")
        return smallF, medF, f, f2, f3, goButton, questionB, starterBg
    def songSelect(self):
        global recordPlayerBg
        recordPlayerBg = loadImage("recordPlayer.png")
        textAlign(CENTER)
        visualButton = button(1250, 50, 150, 70, "VISUALIZE!")
        gameButton = button(60, 50, 150, 70, "GAME!")
        helpers = songFunctions()
        songNames, fullSongNames = helpers.getSongLists()
        songButtons = []
        for i in range(len(songNames)):
            margin = 10
            x = margin + (180*i)
            y = 780
            buttonH = 40
            buttonW = 150
            if x+buttonW > width:
                x = margin + 180*(i % 8) # 8 songs per row
                y = 780 + 55
            newButton = button(x, y, buttonW, buttonH, songNames[i])
            songButtons.append(newButton)
        return visualButton, gameButton, recordPlayerBg, songButtons, fullSongNames
    def help(self):
        fill(0)
        playB = button(width/2 - 50, 720, 120, 60, "PLAY!")
        return playB
    def visual(self):
        global bg
        bg = loadImage("background.png")
        background(bg)
        global averageE
        averageE = []
        global moon
        global cart
        moon = loadImage("moon.png")
        cart = loadImage("cart.png")
        global allStars
        allStars = []
        numStars = 200
        global minStarSize
        global maxStarSize
        minStarSize = 3
        maxStarSize = 8
        for i in range(numStars):
            x = random.randrange(width)
            y = random.randrange(0, 2*height/3)
            r = random.randrange(minStarSize, maxStarSize)
            if 1330 < x < 1360 and 10 < y < 1030: # no star in same location as moon
                x = random.randrange(width)
                y = random.randrange(0, 2*height/3)
            allStars.append(star(x, y, r))
        return bg, averageE, moon, cart, allStars
    def playAgain(self):
        textAlign(CENTER)
        againB = button(width/2 - 125, 350, 250, 75, "Play again!")
        changeSong = button(width/2 - 125, 450, 250, 75, "Change Song")
        helpers = songFunctions()
        songNames, fullSongNames = helpers.getSongLists()
        files = []
        for song in songNames:
            file = createWriter(song+"Scores.txt")
            files.append(file)
            saveStrings(song + "Scores.txt", ["0"])
        return againB, changeSong, files
    
