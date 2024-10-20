from node import Node
'''
graph class
TODO implement the class and missing functions
TODO comment the file
TODO add edges
'''
class Graph:
    
    def __init__(self):
        self.allNodes = []
        self.alreadyInGraph = []
        self.node = None
    def addNode(self, word):
        edgeNode=Node(word) 
        
        if not self.node:
            self.node=edgeNode
            return None
            
        if not self.allNodes:
            self.alreadyInGraph.append(self.node.getWord())
            self.node.addEdges(edgeNode)
            self.allNodes.append(self.node)
            self.node=edgeNode
            return None
        
        for node in self.allNodes:
           
            if not self.alreadyInGraph.__contains__(self.node.getWord()):
                self.allNodes.append(self.node)
                self.alreadyInGraph.append(self.node.getWord())
                self.node.addEdges(edgeNode)
                self.node=edgeNode
                break
           
            else:
                if node.getWord() == self.node.getWord:
                    node.addEdges(edgeNode)
                    self.node=edgeNode
                    self.alreadyInGraph.append(self.node.getWord())
                    break
        print(self.node.getWord() + " no ha entrado")
    def getNode(self,nodeID):
        return self.allNodes[nodeID]
    
    
                
        