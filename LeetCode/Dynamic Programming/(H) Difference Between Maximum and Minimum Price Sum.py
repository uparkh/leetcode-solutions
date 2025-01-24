from typing import List
from collections import defaultdict

class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
        cache = {}  # (a, b) -> maximum price sum of node b coming from node a
        # final = {}  # node -> max global price sum for a node
        visited = set()
        def dfs(par, node):
            cur_max = price[node]
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited:
                    if (node, nei) in cache:
                        cur_max = max(cur_max, cache[(node, nei)] + price[node])
                    else:
                        cur_max = max(cur_max, dfs(node, nei) + price[node])
            cache[(par, node)] = cur_max
            visited.remove(node)
            return cur_max

        # final processing outside of dfs
        snt = n + 1 # sentinel
        reslist = []
        for i in range(n):
            reslist.append(dfs(snt, i) - price[i]) # max - min
        return max(reslist)

