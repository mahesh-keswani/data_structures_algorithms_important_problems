class Graph:

    # v: number of vertices
    # edges: they are in the form of [ [u1, v1, weight1], [u2, v2, weight2],...]
    def __init__(self, v, edges):
        self.v = v
        self.graph = edges

    def find(self, parent, x):
        if x != parent[x]:
            parent[x] = self.find( parent, parent[x] )

        return parent[x]

    def union(self, parent, rank, x, y, rootx, rooty):
        
        if rank[rootx] > rank[rooty]:
            parent[rooty] = rootx
            rank[rootx] += rank[rooty]
        elif rank[rootx] < rank[rooty]:
            parent[rootx] = rooty
            rank[rooty] += rank[rootx]
        else:
            parent[rooty] = rootx
            rank[rootx] += rank[rooty]

    def kruskalMST(self):
        parent = [i for i in range(self.v)]
        rank = [1] * self.v

        # sort the edges based on the weights
        self.graph = sorted( self.graph, key = lambda x: x[2] )

        # to store the resultant edges and cost
        result = []
        minWeight = 0

        # The number of edges in min spanning tree should be v-1
        e = 0

        # for iterating over edges
        i = 0
        while e <= (self.v - 1):
            u, v, w = self.graph[i]
            i = i + 1

            rootx = self.find(parent, u)
            rooty = self.find(parent, v)

            # i.e graph contains cycle
            if rootx != rooty:
                self.union( parent, rank, u, v, rootx, rooty )
                result.append( [u, v] )
                minWeight += w

                # increase the number of edges
                e = e + 1

        print("Minimum cost of spanning tree", minWeight)
        print("The edges are...")

        for edge in result:
            print(edge)
