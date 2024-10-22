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

    def checkEdge(self,node):
        nodeEdge=node.edges[0]
        for edge in self.edges:
                if edge.compareNode(nodeEdge.getToNode()): 
                    edge.addWeight()
                    return True
        self.addEdgeToEdges(nodeEdge)
        return False
    
    def addNodeEdges(self,node):
        if self.getWord() != node.getWord():
            self.edges.append(Edge(node))
            return None
        
    def addEdgeToEdges(self,node):
        if self.getWord() != node.getToNode().getWord():
            self.edges.append(Edge(node.getToNode()))
            return None
    
    def nextNode(self):
        higher=0
        ed=None
        for edge in self.edges:
            finalNode=None
            if edge.getWeight() > higher:
                higher = edge.getWeight()
                finalNode = edge.getToNode()
                ed=edge
        
        if ed:
            self.subtractWeight(ed)
        return finalNode
        
    def addWeight(self,node):
        for edge in self.edges:
            for nodeEdge in node.edges:
                if edge.getToNode().getWord() == nodeEdge.getToNode().getWord():
                    edge.addWeight()
                    break
    def subtractWeight(self,edge):
        for edge in self.edges:
            if edge.getToNode().getWord() == edge.getToNode().getWord():
                edge.reduceWeight()
                break
