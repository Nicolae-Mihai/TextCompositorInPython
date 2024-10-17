'''
edge class
TODO implement the class and missing functions
TODO comment the file
'''

class edge():
    
    
    def __init__(self,node):
        self.toNode = node
        self.weight = 0
    
    def addWeight(self):
        self.weight += 1
    
    def getToNode(self):
        return self.toNode
    
    def getWeight(self):
        return self.weight