edges={("A","B"),("C","D"),("A","D"),("C","B"),("B","E"),("A","E")}
class Graph:
    def __init__(self,Nodes, is_directed=True):
        self.Nodes=Nodes
        self.is_directed=is_directed
        self.adj_lst={}
        for node in self.Nodes:
            self.adj_lst[node]=[]

    def print(self):
        for node in self.Nodes:
            print(node,"->",self.adj_lst[node])

    def add_edge(self,u,v):
        self.adj_lst[u].append(v)
        if  not self.is_directed:
         self.adj_lst[v].append(u)


    def degree(self,node):
        deg=len(self.adj_lst[node])
        print("degree of "+node+" is=",deg)

nodes=["A","B","C","D","E"]
graph=Graph(nodes)
for u,v in edges:
    graph.add_edge(u,v)
graph.print()
graph.degree("C")






