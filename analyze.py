# analyzing the selected sound for frequency distributions, beats, and sound energy

class soundAnalysis(): 
    def __init__(self, signal):
        self.sampleRate = signal.sampleRate()
        self.channels = signal.type() #should be 2, left and right
        self.bufferSize = signal.bufferSize()
        self.left = signal.left
        self.right = signal.right
        self.mix = signal.mix
        self.leftSamples = []
        self.rightSamples = []
        self.mixSamples = []
        for i in range(self.bufferSize): # put all signal data values in a list
            self.leftSamples.append(self.left.get(i))
            self.rightSamples.append(self.right.get(i))
            self.mixSamples.append(self.mix.get(i))
    def reshape(self, L): # reshape function takes a list and returns the 2D version of it (matrx)
        newL = []
        for value in L:
            newL.append([value])
        return newL
    def multiplyMatrices(self, A, B):
        product = [[0 for b in range(len(B[0]))] for a in range(len(A))]
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):
                    product[i][j] += (A[i][k] * B[k][j])
        return product
    def computeDFT(self, x): # discrete fourier transform
        #x = self.mixSamples
        N = len(x)
        n = list(range(N))
        k = self.reshape(n)
        I = complex(0, 1) # imaginary number i
        nk = self.multiplyMatrices([n], k)
        M = (exp(1))**(-I*2*PI*nk[0][0]/N)
        return self.multiplyMatrices([[M]], [x])
    def computeFFT(self, x): # fast fourier transform
        N = len(x) 
        n = list(range(N))
        k = self.reshape(n)
        I = complex(0, 1)
        if N % 2 > 0:
            return None
        elif N <= 10:
            return self.computeDFT(x)
        else:
            evenPart = self.computeFFT(x[::2]) # recursively implements this algorithm
            oddPart = self.computeFFT(x[1::2])
            commonFactor = []
            for num in n:
                commonFactor.append((exp(1))**(-I*2*PI*num/N))
            even = evenPart + self.multiplyMatrices([commonFactor[:N//2]], oddPart)
            odd = evenPart + self.multiplyMatrices([commonFactor[N//2:]], oddPart)
            return (even + odd)
    def computeRMS(self, x): # this computes the volume of the song by calculating RMS of energy
        tempRMS = []
        finalRMS = []
        for i in range(self.bufferSize-1):
            sample = x[i]
            tempRMS.append( sample * sample )
        for rmsVal in tempRMS:
            finalRMS.append((rmsVal/self.bufferSize)**0.5)
        return finalRMS
    def averageRMS(self, x):
        oneSecondL = []
        leftE = self.left.level()
        rightE = self.right.level() # level gets instant energy 
        instant = (leftE)**2 + (rightE)**2
        instantL = []
        while len(oneSecondL) < 100: # 43*1024 = 44032 samples which represents 1 second
            while len(instantL) < 1025: # 1024 samples represent 5 hundreds of a second or an "instant"
                instantL.insert(0, instant)
            e = self.sumOfList(instantL)
            oneSecondL.insert(0, e**2) # insert newest values to beginning
        averageE = (self.sumOfList(oneSecondL))/100
        return averageE
    def sumOfList(self, L):
        return (sum(L)/len(L))
    def beatDetection(self): #using algorithm found here: http://archive.gamedev.net/archive/reference/programming/features/beatdetection/index.html
        leftE = self.left.level()
        rightE = self.right.level() # level gets instant energy 
        instant = (leftE)**2 + (rightE)**2
        instantL = []
        oneSecondL = []
        variance = 0
        while len(oneSecondL) < 44: # 43*1024 = 44032 samples which represents 1 second
            while len(instantL) < 1025: # 1024 samples represent 5 hundreds of a second or an "instant"
                instantL.insert(0, instant)
            e = self.sumOfList(instantL)
            oneSecondL.insert(0, e**2) # insert newest values to beginning
        averageE = (self.sumOfList(oneSecondL))/43
        for i in range(44):
            variance += ((oneSecondL[i] - averageE))
        C = -0.0025714 * variance + 1.5142857
        if e < 0.2: # quieter parts
            if e > C*averageE*500:
                return True
            return False
        elif e >= 0.2: # louder parts
            if e > C*averageE*10:
                return True
            return False
