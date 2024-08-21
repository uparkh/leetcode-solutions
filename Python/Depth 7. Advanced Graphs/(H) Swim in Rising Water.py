from typing import List
import heapq

# My Original Solution -- 30 minutes
# Time -- O(n^2 * log(n))
# Space -- O(n^2)
# I think this has plenty of room for optimization, especially memory-wise.
# But hey, at least I was able to apply Dijkstra's in a less obvious
# context.
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        min_heap = [(grid[0][0], 0, 0)]  # (elevation, i, j)
        n = len(grid)
        visited = {}  # (i, j) -> min elevation to reach that pt
        def bounded(x, y):
            return 0 <= x < n and 0 <= y < n

        while min_heap:
            e1, i1, j1 = heapq.heappop(min_heap)
            if (i1, j1) in visited:
                continue
            visited[(i1, j1)] = e1
            if i1 == n-1 and j1 == n-1:
                break

            dirs = []
            if bounded(i1 - 1, j1): dirs.append((i1 - 1, j1))
            if bounded(i1 + 1, j1): dirs.append((i1 + 1, j1))
            if bounded(i1, j1 - 1): dirs.append((i1, j1 - 1))
            if bounded(i1, j1 + 1): dirs.append((i1, j1 + 1))

            for i2, j2 in dirs:
                if (i2, j2) not in visited:
                    e2 = grid[i2][j2]
                    heapq.heappush(min_heap, (max(e1, e2), i2, j2))
        
        return visited[(n-1, n-1)]

# NeetCode Solution
# The fundamental idea is the same -- Dijkstra's setup, but with 
# pushing a max() of the elevations to the min heap.
# I did experiment with a cardinal direction array to DRY out the 
# 4 `if` conditionals used. But it's not that serious, the solution works
# with Dijkstra's, and that's what matters more.
# I do really like the naming of the directions -- like in calculus with dr, dc
# Imma use that in the future, looks pretty clean.
class NeetCodeSolution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]  # (time/max-height, r, c)
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        visit.add((0, 0))
        while minH:
            t, r, c = heapq.heappop(minH)
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if (
                    neiR < 0
                    or neiC < 0
                    or neiR == N
                    or neiC == N
                    or (neiR, neiC) in visit
                ):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

        return -1

