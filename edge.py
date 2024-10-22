'''
edge class
TODO implement the class and missing functions
TODO comment the file
'''

class Edge:
    
    
    def __init__(self,node):
        self.toNode = node
        self.weight = 1
    
    def addWeight(self):
        self.weight += 1
    
    def reduceWeight(self):
        self.weight -= 1
    
    def getToNode(self):
        return self.toNode
    
    def getWeight(self):
        return self.weight
    
    def compareNode(self,node):
        if self.toNode.getWord() == node.getWord(): 
            print(f"{self.toNode.getWord()} y {node.getWord()} son iguales")
            return True
        else:
            print(f"{self.toNode.getWord()} y {node.getWord()} NO son iguales")
            return False