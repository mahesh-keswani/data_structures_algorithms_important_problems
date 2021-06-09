def topologicalSort(vertices, dependencies):
    graph = Graph(vertices, dependencies)
    return getOrdered(graph)

def getOrdered(graph):
    nodes = graph.nodes

    # this will contain actual topological ordering
    orderedNodes = []
    
    for node in nodes:
        containsCycle = depthFirstSearch(node, orderedNodes)

        # if containsCycle return empty list
        if containsCycle:
            return []

    return orderedNodes

def depthFirstSearch(node, orderedNodes):
    # if the current Node is already visited, then we don't want to explore again,
    # so return False, False indicates there is no cycle
    if node.visited:
        return False

    # if the node is already in progress, that is, it was in progress and not yet explored completly
    # but during exploration we reached the same node, i.e there is cycle, so return True
    if node.visiting:
        return True

    # now we know the node is not visited, so we start exploring
    node.visiting = True
    for prereq in node.prereqs:
        containsCycle = depthFirstSearch(prereq, orderedNodes)
        if containsCycle:
            return True

    orderedNodes.append(node.val)
    node.visited = True
    node.visiting = False

    return False
    
class Graph:

    def __init__(self, vertices, dependencies):
        # here we will put the instance of the nodes and not the values of the nodes
        self.nodes = []

        # this mapping will have mapping from value of node to it's actual node
        self.mapping = {}

        for vertex in vertices:
            self.addNode(vertex)

        # after creating nodes we will add edges in the graph
        self.addEdges(dependencies)

    def addNode(self, vertex):
        newNode = Node(vertex)
        self.nodes.append(newNode)
        self.mapping[vertex] = newNode

    def addEdges(self, dependencies):
        for prereq, vertex in dependencies:
            # getting the actual node for prereq
            prereqNode = self.getNode(prereq)

            self.mapping[vertex].prereqs.append(prereqNode)

    def getNode(self, vertex):
        return self.mapping[vertex]
    
class Node:

    def __init__(self, val):
        self.val = val
        self.visited = False
        self.visiting = False
        self.prereqs = []

vertices = [1, 2, 3, 4]
edges = [ [1, 2], [3, 2], [4, 2], [1, 3], [4, 3] ]

print( topologicalSort(vertices, edges) )      


# ======================================================================================================================================================
def topologicalSort(vertices, edges):
    graph = Graph(vertices, edges)
    return getOrderedJobs(graph)

def getOrderedJobs(graph):
    nodes = graph.nodes
    orderedJobs = []

    queue = [ nodes[0] ]
    while len(queue):
        node = queue.pop(0)

        if node.visited:
            continue

        if node.visiting:
            return []

        node.visiting = True
        for prereq in node.prereqs:
            if not prereq.visited:
                queue.append( prereq )

        node.visiting = False
        node.visited = True

        orderedJobs.append(node.value)
    
    return orderedJobs

class Graph:

    def __init__(self, vertices, edges):
        self.nodes = []
        self.graph = {}

        for vertex in vertices:
            node = Node(vertex)
            self.nodes.append( node )
            self.graph[vertex] = node

        self.addEdges(edges)

    def addEdges(self, edges):
        for prereq, node in edges:
            prereqNode = self.graph[prereq]
            self.graph[node].prereqs.append( prereqNode )
    

class Node:

    def __init__(self, value):
        self.visiting = False
        self.visited = False
        self.value = value
        self.prereqs = []
