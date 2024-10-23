from edge import Edge
'''
Class file for Node that contains it's variables and functions.
'''

class Node:
    
    """
    Constructor for the Node class, it expects a word that will be stored in self.word .
    It also instantiates the edges array.
    """
    def __init__(self, word):
        self.word = word
        self.edges = []
    
    """
    Method that returns the word stored inside the node.
    """
    def getWord(self):
        return self.word

    """
    Method that checks and iserts the edges or adds weight to them depending on
    their existance in the edges list.
    """
    def checkEdge(self,node):
        nodeEdge = node.edges[0]
        for edge in self.edges:
                if edge.compareNode(nodeEdge.getToNode()): 
                    edge.addWeight()
                    break
        self.addEdgeToEdges(nodeEdge)
    
    """
    Method that inserts nodes as edges to another node.
    """
    def addNodeEdges(self,node):
        if self.getWord() != node.getWord():
            self.edges.append(Edge(node))
            return None
        
    """
    Method that inserts edges as edges and checks to make sure their word 
    different from the node's.
    """
    def addEdgeToEdges(self,node):
        if self.getWord() != node.getToNode().getWord():
            self.edges.append(Edge(node.getToNode()))
            return None
    
    """
    Method that returns the next node based on their weight.
    The node with the highest weight are returned first.
    Once a node it's returned it's edge weight is reduced.
    """
    def nextNode(self):
        higher = 0
        ed = None
        finalNode = None
        for edge in self.edges:
            if edge.getWeight() > higher:
                higher = edge.getWeight()
                finalNode = edge.getToNode()
                ed = edge
        
        if ed:
            ed.reduceWeight()
        return finalNode
    
    """
    Method that searches for edges based on the node they contain and reduces
    their edge weight.
    """
    def addWeight(self,node):
        for edge in self.edges:
            for nodeEdge in node.edges:
                if edge.getToNode().getWord() == nodeEdge.getToNode().getWord():
                    edge.addWeight()
                    break