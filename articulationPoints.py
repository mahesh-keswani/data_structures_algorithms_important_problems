from collections import defaultdict

class Graph:

    def __init__(self, v, edges):
        # v = number of vertices in graph
        self.v = v
        self.graph = defaultdict(list)
        self.time = 1

        for edge in edges:
            u = edge[0]
            v = edge[1]

            graph[u].append(v)
            graph[v].append(u)

    def articulationPointHelper(self, u, visited, parent, discovery, low, aps):
        visited[u] = True

        # initializing the dicovery and low time
        discovery[u] = self.time
        low[u] = self.time
    
        self.time += 1

        # to keep track of children of vertices
        children = 0
        
        # visiting it's children
        for v in self.graph[u]:
            if not visited[v]:
                # if the v is not visited
                parent[v] = u
                children += 1
                self.articulationPointHelper(v, visited, parent, discovery, low, aps)

                # formula for low of vertices is
                # min( discovery[u], minOfLowTimeOfChildrenOfU, minOfDiscoveryTimeOfBackEdge )
                low[u] = min(low[u], low[v])

                # if it is root and children > 1, then it is ap
                if parent[u] == -1 and children > 1:
                    aps.append(u)
                elif parent[u] != -1 and discovery[u] <= low[v]:
                    # i.e for v to reach any of the ancestors of u, it has to
                    # pass through u, therefore u is articulation point
                    aps.append(u)
                    
            elif parent[v] != u:
                # i.e v is not a child of u, then there must be backedge
                low[u] = min( low[u], discovery[v] )                

    def articulationPoint(self):
        visited = [False] * self.v
        parent = [-1] * self.v
        discovery = [float("inf")] * self.v
        low = [float("inf")] * self.v
        aps = [] # for storing articulation points
        
        for i in range(self.v):
            # if the vertex is not visited
            if not visited[i]:
                self.articulationPointHelper(i, visited, parent, discovery, low, aps)
                
        return aps
