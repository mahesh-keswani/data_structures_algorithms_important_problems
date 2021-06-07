# source: https://www.geeksforgeeks.org/disjoint-set-data-structures/

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n

    def find(self, x):
        # Finds the representative of the set
        # that x is an element of.

        # if x is not the parent of itself
        # Then x is not the representative of
        # its set.
        if x != self.parent[x]:
            self.parent[x] = self.find( self.parent[x] )

            # so we recursively call Find on its parent
            # and move i's node directly under the
            # representative of this set, thereby reducing the
            # height of the tree.
            
        return self.parent[x]

    def union(self, x, y):
        setx = self.find(x)
        sety = self.find(y)

         # If they are already in same set
        if setx == sety:
            return

        # Put smaller ranked item under
        # bigger ranked item if ranks are
        # different
        
        if self.rank[setx] > self.rank[sety]:
            self.parent[sety] = setx
            self.rank[setx] += self.rank[sety]
            
        elif self.rank[setx] < self.rank[sety]:
            self.parent[setx] = sety
            self.rank[sety] += self.rank[setx]
        else:
            # (doesn't matter which one goes where)
            self.parent[setx] = sety
            self.rank[sety] += self.rank[setx]

# having two sets {0, 2, 4} and {1, 3}
obj = DisjointSet(5)
obj.union(0, 2)
obj.union(4, 2)
obj.union(3, 1)

print(obj.parent)
print("\n\n")
print(obj.rank)
