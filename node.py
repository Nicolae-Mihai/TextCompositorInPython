from random import Random
from edge import Edge

'''
Class file for Node that contains it's variables and functions.
'''

class Node:
    
    '''
    Constructor for the Node class, it expects a word that will be stored in self.word .
    It also instantiates the edges array.
    '''
    def __init__(self, word):
        self.word = word
        self.edges = []
    
    '''
    Method that returns the word stored inside the node.
    '''
    def getWord(self):
        return self.word

    '''
    Method that checks and iserts the edges or adds weight to them depending on
    their existance in the edges list.
    If the Node has no edges it is skipped from inserting in the Graph
    '''
    def checkEdge(self, node):
        if node.edges:
            nodeEdge = node.edges[0]
            for edge in self.edges:
                    if edge.compareNode(nodeEdge.getToNode()): 
                        edge.addWeight()
                        break
            self.addEdgeToEdges(nodeEdge)
    
    '''
    Method that inserts nodes as edges to another node.
    '''
    def addNodeEdges(self, node):
        if self.getWord() != node.getWord():
            self.edges.append(Edge(node))
            return True
        
    '''
    Method that inserts edges as edges and checks to make sure their word 
    different from the node's.
    '''
    def addEdgeToEdges(self, node):
        if self.getWord() != node.getToNode().getWord():
            self.edges.append(Edge(node.getToNode()))
            return True
    
    '''
    Method that returns the next node based on their weight.
    If the array has more than 5 edges the node with the highest weight are 
    stored in the top array which is first filled with the first element of 
    edges. Once all the edges have been compared a random int selects the node 
    to be returned from the array top. If the array has less than 5 edges they 
    are returned at random.
    '''
    def nextNode(self):
        top = [self.edges[0],self.edges[0],self.edges[0],self.edges[0],self.edges[0]]
        finalNode = None
        
        if self.edges.__len__()>5:
            for edge in self.edges:
                num=edge.getWeight()

                match num:
                    case num if num > top[0].getWeight() :
                        top[0] = edge
                        
                    case num if num > top[1].getWeight() :
                        top[1] = edge
                    
                    case num if num > top[2].getWeight() :
                        top[2] = edge
                    
                    case num if num > top[3].getWeight() :
                        top[3] = edge
                    
                    case num if num > top[4].getWeight() :
                        top[4] = edge
            
            rand=Random().randint(0,top.__len__()-1)
            finalNode=top[rand].getToNode()
        else:
            rand=Random().randint(0,self.edges.__len__()-1)
            finalNode=self.edges[rand].getToNode()
            
        return finalNode
    
    '''
    Method that searches for edges based on the node they contain and reduces
    their edge weight.
    '''
    def addWeight(self, node):
        for edge in self.edges:
            for nodeEdge in node.edges:
                if edge.getToNode().getWord() == nodeEdge.getToNode().getWord():
                    edge.addWeight()
                    break