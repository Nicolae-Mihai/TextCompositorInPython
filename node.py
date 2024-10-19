from edge import Edge
'''
node class
TODO implement the class and missing functions
TODO comment the file
'''

class Node:
    
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
        if self.edges:
            self.edges.append(Edge(node))
            return None
        
        if self.word != node.word:
            self.edges.append(Edge(node))
            return None
        
        for edge in self.edges:
            if edge.getToNode() == node:
                edge.addWeight()
                break 
    
    def nextNode(self):
        for edge in self.edges:
            higher=0
            finalNode=None
            if edge.getWeight() > higher:
                higher=edge.getWeight()
                finalNode=edge.getToNode()
        return finalNode.getToNode()
        
            
            
        