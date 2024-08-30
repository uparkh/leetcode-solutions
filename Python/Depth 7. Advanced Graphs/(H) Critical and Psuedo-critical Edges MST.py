from typing import List
import heapq


# My Original Incorrect Solution -- 41 minutes
# I had some intuition about the problem, understanding that I needed to simulate the
# "what if" scenarios of removing each edge and seeing if the MST would still be the same.
# I just couldn't quite figure out how to put it in code. I'm just happy I got to write out
# Kruskal's algorithm from scratch.
class MyUnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    def find(self, n):
        p = n
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True


class MySolution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        min_heap = []
        for i, (a, b, w) in enumerate(edges):
            heapq.heappush(min_heap, (w, a, b, i))

        mst = []
        uf = MyUnionFind(n)
        examine = {}
        while len(mst) < n - 1:
            w1, n1, n2, i = heapq.heappop(min_heap)
            if not uf.union(n1, n2):
                continue
            mst.append(i)


class NCUnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, v1):
        while v1 != self.par[v1]:
            self.par[v1] = self.par[self.par[v1]]
            v1 = self.par[v1]
        return v1

    # slightly different from my implementation
    # Rank calculation adds the rank of the child to the parent, rather than just incrementing
    # by 1. This means that for a full tree, the rank of the parent will be the number of nodes
    # in the tree.
    def union(self, v1, v2):
        p1, p2 = self.find(v1), self.find(v2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True


# NeetCode Solution
# Interestingly, he saves on heap space by just repurposing the edges list to store the index
# and then sorting it by weight, which is what Kruskal's needs anyway.
# Wow, he actually just brute forces the solution by removing each edge and checking if the
# MST is still the same. I guess that's the only way to do it. I thought there was a more
# clever way to do it, but maybe I should have just brute forced it and started there.
class NCSolution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Time: O(E^2) - UF operations are assumed to be approx O(1)
        for i, e in enumerate(edges):
            e.append(i) # [v1, v2, weight, original_index]

        edges.sort(key=lambda e: e[2])

        mst_weight = 0
        uf = NCUnionFind(n)
        for v1, v2, w, i in edges:
            if uf.union(v1, v2):
                mst_weight += w

        critical, pseudo = [], []
        for n1, n2, e_weight, i in edges:
            # Try without curr edge
            weight = 0
            uf = NCUnionFind(n)
            for v1, v2, w, j in edges:
                # i != j check for not selecting the current edge
                if i != j and uf.union(v1, v2):
                    weight += w
            # max(uf.rank) != n is a check to see if all nodes are connected
            # weight > mst_weight is a check to see if the MST weight is higher than the accepted
            # weight. If either of these conditions are true, then the edge is critical.
            if max(uf.rank) != n or weight > mst_weight:
                critical.append(i)
                continue

            # Try with curr edge
            uf = NCUnionFind(n)
            uf.union(n1, n2)
            weight = e_weight
            for v1, v2, w, j in edges:
                if uf.union(v1, v2):
                    weight += w
            if weight == mst_weight:
                pseudo.append(i)
        return [critical, pseudo]
