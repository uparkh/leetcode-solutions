from typing import List

# My Original Solution -- 8 minutes 
# n = numCourses, m = len(prerequisites)
# Time: O(n + m) -- explain: processing all nodes, traversing each edge once
# Space: O(n) -- storing visited/completed node lists
# simply just modifying Course Schedule I.py
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        deps = [[] for _ in range (numCourses)]
        for pair in prerequisites:
            course, prereq = pair
            deps[course].append(prereq)
        
        order = []
        cached_completable = set()
        visited = set()
        def completable(cur): # DFS
            if cur in cached_completable:
                return True
            cur_deps = deps[cur]
            if not cur_deps:
                cached_completable.add(cur)
                order.append(cur)
                return True
            if cur in visited: # cycle
                return False
            visited.add(cur)
            for dep in cur_deps:
                dep_satisfied = completable(dep)
                if not dep_satisfied:
                    return False
            visited.remove(cur)
            cached_completable.add(cur)
            order.append(cur)
            return True
                

        for c, _ in enumerate(deps):
            if not completable(c):
                return []
        return order

            
# NeetCode Solution
# Pretty much the same as mine, but they used a dict, which I actually do not
# agree with at all. Dicts would not be faster than arrays in this case.
# Both yield O(1) time lookup, but arrays are significantly faster.
# They did not use an extra `if` for when deps don't exist. Because the loop
# just wouldn't run.
class NeetCodeSolution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit, cycle = set(), set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True

            cycle.add(crs)
            for pre in prereq[crs]:
                if dfs(pre) == False:
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output

