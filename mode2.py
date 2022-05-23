import os 
import time

class songFunctions():
    def listFiles(self, path): # https://www.cs.cmu.edu/~112/notes/notes-recursion-part2.html
        if os.path.isfile(path):
            return [ path ]
        else:
            files = [ ]
            for filename in os.listdir(path):
                files += self.listFiles(path + '/' + filename)
            return files
    def getSongLists(self):
        songs = self.listFiles('/Users/ankita_kalkar/Documents/Processing/music')
        songNames = []
        fullSongNames = []
        for song in songs:
            print("song", song)
            title = song.split("/")[6]
            print("title", title)
            if title != ".DS_Store": # only on macs
                fullSongNames.append(title)
                songNames.append(title[:len(title)-4])
        return songNames, fullSongNames
    def drawCurveText(self, songSelected, dtheta):
        global time
        arcLength = 0
        r = 230
        textAlign(CENTER, CENTER)
        for i in range(len(songSelected)):
            currentChar = songSelected[i]
            w = textWidth(currentChar)
            arcLength += w/2
            theta = PI + arcLength / r
            pushMatrix()
            translate(r*cos(theta+dtheta), r*sin(theta+dtheta))
            translate(590, 450) # center of disk
            rotate(theta+ PI/2 + dtheta)
            fill(255)
            text(currentChar,0,0)
            popMatrix()
            arcLength += w/2
      
        
        

     
