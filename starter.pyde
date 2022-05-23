# this is the starter file

add_library("minim")
import random
import time
import os
from allSetups import setUps
from analyze import soundAnalysis
from buttons import button
from graph import waves
from visuals import sky
from visuals import star
from visuals import rollerCoaster
from mode2 import songFunctions
from mode3 import visualizeFunctions

def setup():
    fullScreen() # 1440 by 900 for Mac Air
    background(0)
    global gameScreen
    gameScreen = 0
    global allSetUps
    allSetUps = setUps()
    global smallFont
    global medF
    global font
    global goButton
    global questionB
    global starterBg
    global f2
    global f3
    smallFont, medF, font, f2, f3, goButton, questionB, starterBg = allSetUps.start()
    global playB
    playB = allSetUps.help()
    global recordPlayerBg
    global songButtons
    global fullSongNames
    global visualButton
    global gameButton
    global song
    global songCheck
    songCheck = True
    song = None
    global time
    global time2
    time = millis()
    time2 = millis()
    global dtheta
    dtheta = 0
    global curveText
    curveText = False
    global songSelected
    songSelected = None
    visualButton, gameButton, recordPlayerBg, songButtons, fullSongNames = allSetUps.songSelect()
    global bg
    global averageE
    global moon
    global cart
    global allStars
    global score
    score = 0
    bg, averageE, moon, cart, allStars = allSetUps.visual()
    global againB
    global changeSong
    global files
    againB, changeSong, files = allSetUps.playAgain()
def draw():
    global gameScreen
    global song
    global averageE
    global textAlpha
    global score
    if gameScreen == 0:
        startScreen()
    elif gameScreen == 1:
        helpScreen()
    elif gameScreen == 2:
        songSelectScreen()
    elif gameScreen == 3: # visualize
        visualizeOrGameMode() 
    elif gameScreen == 4: # game
        visualizeOrGameMode()
    elif gameScreen == 5: # end visualize
        endGame()
    elif gameScreen == 6: # end game
        endGame()
        
def startScreen():
    global gameScreen
    global starterBg
    textAlign(CENTER)
    textFont(font, 100)
    fill(0)
    background(starterBg)
    text("INVERTI-", width/2-160, height/2+10)
    textFont(medF, 30)
    text("Press 'GO' to play or '?' for instructions", width/2, height/2 + 110)
    textFont(font, 100)
    goButton.updateButton(mousePressed)
    goButton.drawButton()
    textFont(f2, 30)
    questionB.updateButton(mousePressed)
    questionB.drawButton()
    if goButton.isClicked():
        gameScreen = 2
    if questionB.isClicked():
        gameScreen = 1

def helpScreen():
    global starterBg
    global playB
    global gameScreen
    background(starterBg)
    fill(255)
    textFont(f3, 60)
    fill(0)
    text("How to play?", width/2, 200)
    textFont(medF, 30)
    textAlign(CENTER)
    text("First, select a song by clicking one of the buttons and select", width/2, 260)
    text("either visualize or game mode.", 430, 300)
    text("Visualize mode: Enjoy the song! Pay attention to the track and \n stars to see the average energy of the song change as the song  ", width/2, 360)
    text("progresses. Some more features include the moon which flashes if \n a beat is heard and the graphs at the bottom which represent the  ", 740, 430)
    text(" left and right frequency domain graphs", 485, 500)
    text("Game mode: Press the space bar if the first cart is at a peak  \non the average energy roller coaster track to score points!    ", width/2, 560)
    text("Click play to get started!", width/2, 660)
    playB.updateButton(mousePressed)
    playB.drawButton()
    if playB.isClicked():
        gameScreen = 2

def songSelectScreen():
    global songSelected
    global gameScreen
    global song
    global songCheck
    global time
    global dtheta
    global message
    global curveText
    global font
    global averageE
    background(recordPlayerBg)
    fill(0)
    theta = 0
    textFont(smallFont, 20)
    noStroke()
    visualButton.updateButton(mousePressed)
    visualButton.drawButton()
    gameButton.updateButton(mousePressed)
    gameButton.drawButton()
    if songCheck == False: # displays warning message 
        fill(0)
        textFont(font, 48)
        if millis() < time + 6000: # https://forum.processing.org/two/discussion/25769/how-do-i-display-a-text-for-2-seconds
            text("Please select a song!", width/2, 90)
    if visualButton.isClicked() and song != None:
        songCheck = True
        gameScreen = 3
    elif gameButton.isClicked() and song != None:
        songCheck = True
        gameScreen = 4
    elif visualButton.isClicked() or gameButton.isClicked():
        songCheck = False
    for button in songButtons:
        fill(175)
        textAlign(CENTER)
        textFont(smallFont, 20)
        noStroke()
        button.updateButton(mousePressed)
        button.drawButton()
        if button.isClicked():
            songSelected = fullSongNames[songButtons.index(button)]
            minim = Minim(this)
            song = minim.loadFile("music/"+songSelected)
            curveText = True
            averageE = []
    if curveText == True: 
        fill(0)
        textFont(font, 48)
        textAlign(CENTER)
        helpers = songFunctions()
        helpers.drawCurveText(songSelected, dtheta)    
        dtheta += 0.04
    
def visualizeOrGameMode():
    global song
    global gameScreen
    global bg
    global averageE
    global allStars
    global score
    global time2
    if len(averageE) > 6:
        if not song.isPlaying() and averageE[24] == 0: # 24 is index of last cart
            if gameScreen == 4:
                gameScreen = 6
            elif gameScreen == 3:
                gameScreen = 5
    helpers = visualizeFunctions()
    background(bg)
    song.play() 
    LfftValues = helpers.analyze(song)[0]
    #rmsValues = helpers.analyze(song)[1]
    beat = helpers.analyze(song)[2]
    avgRMS = helpers.analyze(song)[3]
    RfftValues = helpers.analyze(song)[4]
    averageE.append(avgRMS)
    skyVisuals = sky(song)
    skyVisuals.drawMoon(moon)
    graphs = waves(song, averageE)
    graphs.drawCurve()
    graphs.drawRCSticks()
    helpers.visualizeStars(allStars)
    helpers.getShinyStars(allStars, song)
    for star in allStars:
        star.render(gameScreen)
    helpers.unShine(allStars) 
    if gameScreen == 3: # just visualizer mode
        #graphs.drawTimeWaveform() 
        graphs.drawLFFT(LfftValues)
        graphs.drawRFFT(RfftValues)
    if gameScreen == 4: # just game mode
        rc = rollerCoaster(cart, averageE) 
        rc.drawCoaster()
        if len(averageE) > 6:
            place = len(averageE) - 1
            if place < 29:
                index = place
            else: # roller coaster is stationary
                index = 29
            currValue = (averageE[index])*50000
            if keyPressed == True and currValue > 2:
                if rc.getAngle(index) < 0 and rc.getAngle(index-1) > 0:
                    score += 10
            fill(255)
            textFont(font, 48)
            text("score: " + str(score), 150, 70)
        
def keyPressed():
    if key == "SPACE":
        return True

def endGame():
    global bg
    global score
    global gameScreen
    global song
    global songSelected
    global averageE
    global files
    background(bg)
    fill(255)
    textFont(font, 48)
    if gameScreen == 6:
        text("Your final score is: " + str(score), width/2, 300)
        all = loadStrings(songSelected[:len(songSelected)-4]+"Scores.txt")
        allScores = []
        for num in all:
            allScores.append(num)
        for prevScore in allScores:
            if score > int(prevScore):
                text("HIGH SCORE!", width/2, 200)
        newData = allScores.append(str(score))
        file = songSelected[:len(songSelected)-4]+"Scores.txt"
        saveStrings(file, allScores)
        for file in files:
            file.flush()
            file.close()
    fill(0)
    textFont(medF, 30)
    noStroke()
    againB.updateButton(mousePressed)
    againB.drawButton()
    changeSong.updateButton(mousePressed)
    changeSong.drawButton()
    if againB.isClicked():
        averageE = []
        minim = Minim(this)
        score = 0
        song = minim.loadFile("music/"+songSelected)
        gameScreen = 4
    if changeSong.isClicked():
        score = 0
        gameScreen = 2
        
