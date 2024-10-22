from node import Node
'''
graph class
TODO implement the class and missing functions
TODO comment the file
TODO add edges
'''
class Graph:
    
    def __init__(self):
        self.allNodes =[]
        self.ingraph=[]
    def addNode(self, node):
        if self.allNodes and node.edges:
            if self.nodeExists(node.getWord()):
                for listNode in self.allNodes:
                    if listNode.getWord() == node.getWord():
                        self.ingraph.append(node.getWord())
                        listNode.checkEdge(node)
                        break
            else:
                self.ingraph.append(node.getWord())
                self.allNodes.append(node)
        else:
            self.ingraph.append(node.getWord())
            self.allNodes.append(node)
            
    def getNodeID(self,nodeID):
        return self.allNodes[nodeID]
    
    def getNodeWord(self,word):
        for node in self.allNodes:
            if node.getWord() == word:
                return node
    
    def nodeExists(self,word):
        for node in self.allNodes:
            if node.getWord() == word:
                return True
        return False
    def test(self):
        self.ingraph=list(set(self.ingraph))
                
        