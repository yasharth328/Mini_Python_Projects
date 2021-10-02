from collections import defaultdict
class Graph:
    def __init__(self, noOfVertices):
        self.graph=defaultdict(list)
        self.noOfVertices=noOfVertices
        
    def addedge(self, vertices,edge):
        self.graph[vertices].append(edge)
        
    def topologicalSort(self,v,visited,stack):
        visited.append(v)
        
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSort(i,visited,stack)
            
        stack.insert(0,v)
    
    def topological(self):
        visited=[]
        stack=[]
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSort(k,visited,stack)
        print(stack)
            
            
customGraph=Graph(8)
customGraph.addedge("A","C")
customGraph.addedge("B","C")
customGraph.addedge("C","E")
customGraph.addedge("D","F")
customGraph.addedge("E","F")
customGraph.addedge("E","H")
customGraph.addedge("F","G")

customGraph.topological()
