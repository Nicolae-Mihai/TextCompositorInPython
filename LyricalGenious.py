'''
TODO implement the class and missing functions
TODO comment the file
'''
from locale import normalize
import os,glob
import random
from unidecode import unidecode
import re
from graph import Graph


class LyricalGenious():
        
    def fillGraph(self):
        self.graph=Graph()
        path="songs/"
        cleanedWords=[]
        
        for filename in glob.glob(os.path.join(path,"*.txt")):
            
            with open(os.path.join(os.getcwd(),filename),"r") as file:        
                fileWords=self.cleanLines(file.read())
                file.close()
            
            for word in fileWords:
                cleanedWords.append(word)
                self.graph.addNode(word)
                      
    def createSong(self):
        running = True
        startingNode = self.graph.getNode(int(random.randrange(0,self.graph.allNodes.__len__())))
        song = startingNode.getWord()
        following = startingNode.nextNode()

        while running:
            # song += " " + following.getWord()
            print(following.nextNode())
            following = following.nextNode()
            if following == None:
                running = False
        return song

    
    def cleanLines(self,song):
        
        normalisedWords=song.encode("windows-1252").decode("utf-8")
        unicodedWords=unidecode(normalisedWords)
        onlyWords = re.sub('[^A-Za-z0-9]+', ' ', unicodedWords).strip().lower()
        cleanedWords=onlyWords.split()
        return cleanedWords
    
    
lg=LyricalGenious()
lg.fillGraph()
lg.createSong()