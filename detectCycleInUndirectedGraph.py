# This method assumes that the graph doesn’t contain any self-loops. 
class DetectCycleInUndrirectedGraph:
	
	# n: Number of vertices
	# the edges is in the form [ [u1, v1], [u2, v2],... ]
	
    def __init__(self, n, edges):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

        # Intializing as False
        self.containsCycle = False
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            self.union(u, v)        

    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find( self.parent[x] )

        return self.parent[x]

    def union(self, x, y):
        setx = self.find(x)
        sety = self.find(y)

        # if the two vertices belong to the same sets
        if setx == sety:
            self.containsCycle = True
            return

        if self.rank[setx] > self.rank[sety]:
            self.parent[sety] = setx
            self.rank[setx] += self.rank[sety]
        elif self.rank[setx] < self.rank[sety]:
            self.parent[sety] = setx
            self.rank[sety] += self.rank[setx]
        else:
            self.parent[setx] = sety
            self.rank[sety] += self.rank[setx]

    def doesContainsCycle(self):
        return self.containsCycle
