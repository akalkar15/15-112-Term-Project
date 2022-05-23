from analyze import soundAnalysis 

class waves():
    def __init__(self, song, data):
        self.song = song
        self.data = data
        self.signal = soundAnalysis(song)
        self.mixSamples = self.signal.mixSamples
        self.fftValues = self.signal.computeFFT(self.mixSamples)
    def drawCurve(self):
        smooth()
        stroke(200)
        strokeWeight(4)
        strokeJoin(ROUND)
        strokeCap(ROUND)
        noFill()
        beginShape()
        if len(self.data) > 2 and len(self.data) < 55: 
        # 55 is max num of data points that can fit on screen
            for i in range(len(self.data)-1):
                x = map(i, 0, self.song.bufferSize(), 0, width*20) 
                if i == 0 or i == len(self.data)-1:
                    curveVertex(x, 550 - self.data[i]*50000)
                curveVertex(x, 550 - self.data[i]*50000)    
        elif len(self.data) >= 55:
            self.data.remove(self.data[0])
            for i in range(len(self.data)-1):
                x = map(i, 0, self.song.bufferSize(), 0, width*20) 
                if i == 0 or i == len(self.data)-1:
                    curveVertex(x, 550 - self.data[i]*50000)
                curveVertex(x, 550 - self.data[i]*50000)
        endShape()
    def drawRCSticks(self):
        stroke(200)
        strokeWeight(4)
        strokeJoin(ROUND)
        strokeCap(ROUND)
        if len(self.data) > 3:
            for i in range(len(self.data)-1):
                x = map(i, 0, self.song.bufferSize(), 0, width*20)
                rect(x-1, height-20, 1, -height+20+(550-(self.data[i])*50000))
    def drawTimeWaveform(self): # algorithm from http://minimpython.blogspot.com/2016/08/minim-6-draw-waveform-and-level.html
        stroke(255)
        strokeWeight(1)
        strokeJoin(ROUND)
        strokeCap(ROUND)
        for i in range(self.song.bufferSize()-1): # buffer size is amount of time to process some digital signal
            x1 = map(i, 0, self.song.bufferSize(), 0, width/3)
            x2 = map(i+1, 0, self.song.bufferSize(), 0, width/3)
            x3 = map(i, 0, self.song.bufferSize(), width/3, 2*width/3)
            x4 = map(i+1, 0, self.song.bufferSize(), width/3, 2*width/3)
            x5 = map(i, 0, self.song.bufferSize(), 2*width/3, width)
            x6 = map(i+1, 0, self.song.bufferSize(), 2*width/3, width)
            line( x1, 600 + self.song.left.get(i)*10,  # left time waveform
                x2, 600 + self.song.left.get(i+1)*10)
            line( x3, 600 + self.song.mix.get(i)*30,  # mix time waveform
                x4, 600 + self.song.mix.get(i+1)*30)
            line( x5, 600 + self.song.right.get(i)*10, # right time waveform 
                x6, 600 + self.song.right.get(i+1)*10)
    def drawLFFT(self, data): # https://processing.org/examples/lineargradient.html
        colorMode = RGB
        red = color(255, 0, 0, 255)
        purple = color(255, 0, 255, 255)
        for valList in data:
            for val in valList:
                frac = float(valList.index(val)+1)/float(len(valList))
                left = 0
                right = int(abs(val))*5
                top = int(680 + frac*200 - 15)
                bottom = top + 15
                currentStroke = red
                step = 0
                smooth()
                for i in range(left, right):
                    step = map(i, left, right, 0.0, 1.0)
                    currentStroke = lerpColor(red, purple, step, colorMode)
                    stroke(currentStroke)
                    line(i, top, i, bottom) 
    def drawRFFT(self, data):
        colorMode = RGB
        red = color(255, 0, 0, 255)
        purple = color(255, 0, 255, 255)
        for valList in data:
            for val in valList:
                frac = float(valList.index(val)+1)/float(len(valList))
                left = width - int(abs(val))*5
                right = width
                top = int(680 + frac*200 - 15)
                bottom = top + 15
                currentStroke = purple
                step = 0
                smooth()
                for i in range(left, right):
                    step = map(i, left, right, 0.0, 1.0)
                    currentStroke = lerpColor(purple, red, step, colorMode)
                    stroke(currentStroke)
                    line(i, top, i, bottom) 
        
