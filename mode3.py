from analyze import soundAnalysis
from visuals import star
import random 

class visualizeFunctions():
    def analyze(self, song): #helper function to analyze the song selected
        signal = soundAnalysis(song)
        mixSamples = []
        leftSamples = []
        rightSamples = []
        for i in range(song.bufferSize()): # put all signal data values in a list
            mixSamples.append(round(song.mix.get(i), 2))
            leftSamples.append(song.left.get(i))
            rightSamples.append(song.right.get(i))
        result0 = signal.computeFFT(leftSamples)
        result1 = signal.computeRMS(mixSamples)
        result2 = signal.beatDetection()
        result3 = signal.averageRMS(mixSamples)
        result4 = signal.computeFFT(rightSamples)
        return [result0, result1, result2, result3, result4]
    def visualizeStars(self, allStars):
        for someStar in allStars:
            if someStar.offScreen() == True:
                allStars.remove(someStar)
                newx = random.randrange(width)
                newy = random.randrange(height)
                newr = random.randrange(1, 6)
                allStars.append(star(newx, newy, newr))
        if frameCount % 20 == 0:
            chosen = random.choice(allStars)
            chosen.shoot()
    def numStarsShining(self, song):
        averageE = self.analyze(song)[3]
        return int(averageE*10000)
    def getShinyStars(self, allStars, song):
        totalShine = self.numStarsShining(song)
        for i in range(totalShine):
            chosen = random.choice(allStars)
            chosen.makeShiny()
    def unShine(self, allStars):
        for star in allStars:
            star.unShiny()
            
