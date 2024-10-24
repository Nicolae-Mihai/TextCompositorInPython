'''
Class file for Edge class that contains it's variables and methods.
'''

class Edge:
    
    '''
    Constructor for the Edge class.
    '''
    def __init__(self, node):
        self.toNode = node
        self.weight = 1
    '''
    Method that adds weight to the edge.
    '''
    def addWeight(self):
        self.weight += 1
    '''
    Method that reduces the weight of the edge.
    '''
    def reduceWeight(self):
        self.weight -= 1
    
    '''
    Method that returns the node that it contains.
    '''
    def getToNode(self):
        return self.toNode

    '''
    Method that returns the weight of the edge
    '''
    def getWeight(self):
        return self.weight
    
    '''
    Method that compares the word of a node to the node word it contains and it 
    returns true or false deppending on the result.
    '''
    def compareNode(self, node):
        if self.toNode.getWord() == node.getWord(): 
            return True
        else:
            return False