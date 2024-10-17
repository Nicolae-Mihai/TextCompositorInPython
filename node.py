import edge
'''
node class
TODO implement the class and missing functions
TODO comment the file
'''

class node():
    
    def __init__(self, word):
        self.word = word
        self.edges = []
    
    def getWord(self):
        return self.word

    def getEdge(self,node):
        for edge in self.edges:
            if edge.getToNode() == node:
                return edge
    
    def addEdges(self,node):
        if node != None:
            for edge in self.edges:
                if edge.getToNode().equals(node):
                    edge.addWeight()
                    break 
            if self.word != node.word:
                self.edges.append(edge(node))
    
    def nextWord(self, song):
        for edge in self.edges:
            higher=0
            finalNode=None
            if edge.getWeight() > higher:
                higher=edge.getWeight()
                finalNode=edge.getToNode()
        song+=" " + finalNode.getWord()
        return finalNode.getToNode
        
            
            
        