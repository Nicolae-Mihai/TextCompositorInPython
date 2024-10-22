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
from node import Node


class LyricalGenious():
    previousWord=None
    
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
                self.createNode(word,self.previousWord)

                      
    def createSong(self):
        self.graph.test()
        running = True
        number=int(random.randrange(0,self.graph.allNodes.__len__()))
        startingNode = self.graph.getNodeID(number)
        song = startingNode.getWord()
        following = startingNode.nextNode()
        i=0
        if following:
            while running:
                followingWord=following.getWord()
                song += " " + followingWord
                print(followingWord)
                following = self.graph.getNodeWord(following.getWord()).nextNode()
                
                # if i<300:
                #     number=int(random.randrange(0,self.graph.allNodes.__len__()))
                #     following = self.graph.getNodeID(number)
                    
                if following == None:
                    if i>300:
                        running = False
                    else:
                        number=int(random.randrange(0,self.graph.allNodes.__len__()))
                        following=self.graph.getNodeID(number)
                i+=1
            return song
        else:
            self.createSong()
    
    def cleanLines(self,song):
        normalisedWords=song.encode("windows-1252").decode("utf-8")
        unicodedWords=unidecode(normalisedWords)
        onlyWords = re.sub('[^A-Za-z0-9]+', ' ', unicodedWords).strip().lower()
        cleanedWords=onlyWords.split()
        # print(cleanedWords)
        return cleanedWords
    
    def createNode(self,word,prev=None ):
        if prev:
                node=Node(self.previousWord)
                node.addNodeEdges(Node(word))
                self.graph.addNode(node)  

        self.previousWord=word
    
lg=LyricalGenious()
lg.fillGraph()
print(lg.createSong())