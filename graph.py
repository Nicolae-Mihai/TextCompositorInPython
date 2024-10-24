'''
Class file for graph that contains it's variables and methods.
'''

class Graph:
    
    '''
    Constructor for the graph.
    '''    
    def __init__(self):
        self.allNodes = []
        self.nodeWords=[]

    '''
    Method that inserts the Nodes into the graph, checking that they are not
    already in the graph, if they are it increases the weight of the edge shared 
    by the nodes.
    If the list is empty it automaticaly inserts the node. 
    '''
    def addNode(self, node):
        if self.allNodes:
            if self.nodeExists(node.getWord()):
                for listNode in self.allNodes:
                    if listNode.getWord() == node.getWord():
                        listNode.checkEdge(node)
                        break
            else:
                self.allNodes.append(node)
        else:
            self.allNodes.append(node)
            
    '''
    Method that returns the node in the position corresponding to the ID passed.
    '''
    def getNodeID(self,nodeID):
        return self.allNodes[nodeID]
    
    '''
    Method that returns the node that contains the word sent.
    '''
    def getNodeWord(self,word):
        for node in self.allNodes:
            if node.getWord() == word:
                return node
    
    '''
    Method that checks to see if a node containing the word exists in the list
    or not.
    '''
    def nodeExists(self,word):
        for node in self.allNodes:
            if node.getWord() == word:
                return True
        return False
        
                
        