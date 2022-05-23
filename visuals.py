from buttons import button
from analyze import soundAnalysis 

class sky():
    def __init__(self, song):
        self.song = song
        self.signal = soundAnalysis(self.song)
        self.beat = self.signal.beatDetection()
        self.RMS = self.signal.computeRMS(self.signal.mixSamples)
    def drawMoon(self, moon):
        imageMode(CENTER)
        if self.beat:
            tint(100)
        else:
            tint(255)
        image(moon, 1360, 80)
class star(): # inspired by https://www.openprocessing.org/sketch/510610
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.shooting = False
        self.alpha = 255
        self.xoff = 0
        self.yoff = 0
        self.shining = False
    def makeShiny(self):
        self.shining = True
    def unShiny(self):
        self.shining = False
    def shoot(self):
        self.shooting = True
        self.xoff = random(-20, 20)
        self.yoff = random(-20, 20)
    def render(self, gameScreen):
        if self.shooting:
            self.x += self.xoff
            self.y += self.yoff
            self.alpha -= 5
        if gameScreen == 3:
            if self.shining == True: #random(1) < 0.005:
                self.shining = True
                self.r = self.r*2
                noStroke()
                #fill(255, 255, 0)
                pushMatrix()
                oneEllipse = createShape(ELLIPSE, self.x, self.y, self.r, self.r)
                oneEllipse.setFill(color(255, 255, 0))
                shape(oneEllipse)
                popMatrix()
                #ellipse(self.x, self.y, self.r+0.03, self.r+0.03)
                red = 232
                green = 196
                blue = 16
                stroke(255)
                strokeWeight(0.01)
                filter(BLUR, 0.2)
                self.r = self.r/2
                #fill(red, green, blue, self.alpha)
                pushMatrix()
                oneEllipse = createShape(ELLIPSE, self.x, self.y, self.r, self.r)
                oneEllipse.setFill(color(red, green, blue, self.alpha))
                shape(oneEllipse)
                #ellipse(self.x, self.y, self.r, self.r)
                popMatrix()
            else:
                self.shining = False
                red = 175
                green = 175
                blue = 175
                noStroke()
                fill(red, green, blue, self.alpha)
                ellipse(self.x, self.y, self.r, self.r)
        elif gameScreen == 4:
            if random(1) < 0.005:
                self.shining = True
                self.r = self.r*2
                noStroke()
                #fill(255, 255, 0)
                pushMatrix()
                oneEllipse = createShape(ELLIPSE, self.x, self.y, self.r, self.r)
                oneEllipse.setFill(color(255, 255, 0))
                shape(oneEllipse)
                popMatrix()
                #ellipse(self.x, self.y, self.r+0.03, self.r+0.03)
                red = 232
                green = 196
                blue = 16
                stroke(255)
                strokeWeight(0.01)
                filter(BLUR, 0.2)
                self.r = self.r/2
                #fill(red, green, blue, self.alpha)
                pushMatrix()
                oneEllipse = createShape(ELLIPSE, self.x, self.y, self.r, self.r)
                oneEllipse.setFill(color(red, green, blue, self.alpha))
                shape(oneEllipse)
                #ellipse(self.x, self.y, self.r, self.r)
                popMatrix()
            else:
                self.shining = False
                red = 175
                green = 175
                blue = 175
                noStroke()
                fill(red, green, blue, self.alpha)
                ellipse(self.x, self.y, self.r, self.r)
    def isShining(self):
        return self.shining
    def offScreen(self):
        if self.x < 0 or self.x > width:
           if self.y < 0 or self.y > height:
                return True
class rollerCoaster():
    def __init__(self, cart, averageE):
        self.cart = cart
        self.averageE = averageE
    def getAngle(self, i):
        if i < 30 and i > 1:
            slope = 50000*(self.averageE[i+1] - self.averageE[i])/1
        else:
            slope = 50000*(self.averageE[i+1] - self.averageE[i])/1 
        theta = atan(slope)
        if slope >= 0: # uphill
            return -1*(theta)*(0.1)
        elif slope < 0: # downhill
            return -1*(theta)*(0.2)
    def drawCoaster(self):
        imageMode(CENTER)
        if len(self.averageE) > 4 and len(self.averageE) <= 30: # when self.averageE has a length of 35, it is halfway across the screen
            for i in range(len(self.averageE)-1):
                if i < len(self.averageE)-2:
                    tint(255, 0) # previous images disappear
                else:
                    tint(255, 255)
                x1 = map(i, 0, 1024, 0, width*20)
                y1 = 538 - self.averageE[i]*50000 # 538 is baseline of track
                x2 = map(i-1, 0, 1024, 0, width*20)
                y2 = 538 - self.averageE[i-1]*50000
                x3 = map(i-2, 0, 1024, 0, width*20)
                y3 = 538 - self.averageE[i-2]*50000
                x4 = map(i-3, 0, 1024, 0, width*20)
                y4 = 538 - self.averageE[i-3]*50000
                x5 = map(i-4, 0, 1024, 0, width*20)
                y5 = 538 - self.averageE[i-4]*50000
                x6 = map(i-5, 0, 1024, 0, width*20)
                y6 = 538 - self.averageE[i-5]*50000
                pushMatrix()
                self.cart.resize(50, 50)
                translate(x1, y1)
                rotate(self.getAngle(i))
                image(self.cart, 0, 0) 
                popMatrix()
                pushMatrix()
                translate(x2, y2)
                rotate(self.getAngle(i-1))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x3, y3)
                rotate(self.getAngle(i-2))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x4, y4)
                rotate(self.getAngle(i-3))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x5, y5)
                rotate(self.getAngle(i-4))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x6, y6)
                rotate(self.getAngle(i-5))
                image(self.cart, 0, 0)
                popMatrix()
        elif len(self.averageE) > 30: # roller coaster fixed in middle of screen
            for i in range(len(self.averageE)):
                if i < len(self.averageE)-2:
                    tint(255, 0)
                else:
                    tint(255, 255)
                x1 = map(29, 0, 1024, 0, width*20)
                y1 = 538 - self.averageE[29]*50000 # len(self.averageE)-32
                x2 = map(28, 0, 1024, 0, width*20)
                y2 = 538 - self.averageE[28]*50000
                x3 = map(27, 0, 1024, 0, width*20)
                y3 = 538 - self.averageE[27]*50000
                x4 = map(26, 0, 1024, 0, width*20)
                y4 = 538 - self.averageE[26]*50000
                x5 = map(25, 0, 1024, 0, width*20)
                y5 = 538 - self.averageE[25]*50000
                x6 = map(24, 0, 1024, 0, width*20)
                y6 = 538 - self.averageE[24]*50000
                pushMatrix()
                translate(x1, y1)
                rotate(self.getAngle(29))
                image(self.cart, 0, 0) 
                popMatrix()
                pushMatrix()
                translate(x2, y2)
                rotate(self.getAngle(28))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x3, y3)
                rotate(self.getAngle(27))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x4, y4)
                rotate(self.getAngle(26))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x5, y5)
                rotate(self.getAngle(25))
                image(self.cart, 0, 0)
                popMatrix()
                pushMatrix()
                translate(x6, y6)
                rotate(self.getAngle(24))
                image(self.cart, 0, 0)
                popMatrix()
        
        
