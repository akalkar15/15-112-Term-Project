
class button():
    def __init__(self, posX, posY, buttonW, buttonH, word):
        self.posX = posX
        self.posY = posY
        self.buttonW = buttonW
        self.buttonH = buttonH
        self.color = color(175, 0, 175)
        self.word = word
        self.clicked = False
        self.over = False
    def updateButton(self, mousePressed):
        if mousePressed == True and mouseX <= self.posX + self.buttonW and mouseX > self.posX:
            if mouseY >= self.posY and mouseY < self.posY + self.buttonH:
                self.clicked = True
        else:
            self.clicked = False
        if self.overButton():
            self.over = True
        else:
            self.over = False
    def drawButton(self):
        if self.over == True:
            self.color = color(175, 0, 175)
        elif self.over == False:
            self.color = color(0, 0, 175)
        fill(self.color)
        rect(self.posX, self.posY, self.buttonW, self.buttonH)
        fill(255)
        textAlign(CENTER)
        text(self.word, self.posX + (self.buttonW/2), self.posY + (self.buttonH/1.4))
    def isClicked(self):
        return self.clicked
    def getSong(self):
        return self.word
    def overButton(self):
        if mouseX > self.posX and mouseX <= self.posX + self.buttonW:
            if mouseY >= self.posY and mouseY < self.posY + self.buttonH:
                return True
        return False
