import node
from random import random
'''
node class
TODO implement the class and missing functions
TODO comment the file
'''
class graph():
    
    def __init__(self,allNodes):
        self.allNodes = allNodes
    
    def addNode(self, word):
        for nod in self.allNodes:
            if nod.getWord() == word:
                self.allNodes.append(node(word))
    
    def followNodes(self):
        running = True
        startingNode=self.allNodes[random()]
        song=startingNode.getWord
        second=startingNode.nextWord(song)
        
        while running:
            second=second.nextWord(song)
            if second==None:
                running=False

    
    
                
        