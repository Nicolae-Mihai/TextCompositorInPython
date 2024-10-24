import os,glob
import random
from unidecode import unidecode
import re
from graph import Graph
from node import Node

'''
Main class of the project
'''

class LyricalGenious():
    songLength=300
    previousNode = None
    
    '''
    Method that navigates to the file whose path is determined using the path 
    variable and starts opening the files one by one and extracting their
    content. Once a file has been opened and it's content extracted the file 
    content is stripped down to only lowercase words.
    After cleaning the content the words are converted to nodes and inserted to
    the graph.
    '''
    def fillGraph(self):
        self.graph = Graph()
        path = "songs/"
        
        for filename in glob.glob(os.path.join(path,"*.txt")):
            
            with open(os.path.join(os.getcwd(),filename),"r") as file:        
                fileWords = self.cleanLines(file.read())
                file.close()
            for word in fileWords:
                self.createNode(word)
            self.previousNode=None
    '''
    Method that creates the song by following the nodes and stitching their 
    words to the "song" variable.
    The method generates a random int between 0 and the number of nodes in the
    graph and uses the int to select the first node in the series.
    The while loop stops if the desired song length is reached. 
    '''
    def createSong(self):
        running = True
        number = int(random.randrange(0,self.graph.allNodes.__len__()))
        startingNode = self.graph.getNodeID(number)
        song = startingNode.getWord()
        following = startingNode.nextNode()
        wordCount = 1
        
        while running and wordCount<self.songLength:
            
            if following != None:
                followingWord = following.getWord()
                song += " " + followingWord
                following = self.graph.getNodeWord(following.getWord()).nextNode()
                wordCount += 1
            else:
                number = int(random.randrange(0,self.graph.allNodes.__len__()))
                following = self.graph.getNodeID(number)
                
        return song
    
    '''
    Method that cleans and normalises the content extracted from the files.
    In order to get rid of the accents it encodes and then decodes the content
    in order to prepare them for the normalisation where the accents are 
    stripped away.
    After normalisation it uses regex to leave behind only the words and none 
    of the punctuation marks and splits the content to generate the word array. 
    '''
    def cleanLines(self, song):

        normalisedWords = song.encode("windows-1252").decode("utf-8")
        unicodedWords = unidecode(normalisedWords)
        onlyWords = re.sub('[^A-Za-z0-9]+', ' ', unicodedWords).strip().lower()
        cleanedWords = onlyWords.split()
        return cleanedWords
    
    '''
    Method that creates a node in the graph.
    in the first iteration it recieves only word, which will pass on to become 
    self.previousNode in the second iteration and the new word becomes the edge
    Node.
    If a duplicate appears,since it can't edge with itself it is stored in
    duplicate until a different word appears and it bonds duplicate to it.
    '''
    def createNode(self, word):
        self.duplicate = None
        edgeNode=None
        if self.previousNode:
            if word:  
                if not self.duplicate:
                    currentNode = self.previousNode
                    edgeNode=Node(word)
                    self.previousNode.addNodeEdges(edgeNode)
                    if currentNode.edges:
                        self.graph.addNode(currentNode)
                    else:
                        duplicate = currentNode
                elif self.duplicate.getWord() != self.previousNode():
                    self.duplicate.addNodeEdges(Node(word))
                    self.graph.addNode(duplicate)
                    self.duplicate = None
            else:
                self.graph.addNode(self.previousNode)
        else: 
            self.previousNode=Node(word)
            self.graph.addNode(self.previousNode)
            return None
        
        self.previousNode = edgeNode
            
lg = LyricalGenious()
lg.fillGraph()
print(lg.createSong())