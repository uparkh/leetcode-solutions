from typing import List

# My Original Solution -- 30 minutes
# n = numCourses, m = len(prerequisites)
# Time: O(n + m) -- explain: processing all nodes, traversing each edge once
# Space: O(n) -- storing visited/completed node lists
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        deps = [[] for _ in range (numCourses)]
        for pair in prerequisites:
            course, prereq = pair
            deps[course].append(prereq)
        
        cached_completable = set()

        visited = set()
        def completable(cur): # DFS
            cur_deps = deps[cur]
            if not cur_deps or cur in cached_completable:
                return True
            if cur in visited: # cycle
                return False
            visited.add(cur)
            for dep in cur_deps:
                dep_satisfied = completable(dep)
                if not dep_satisfied:
                    return False
            cached_completable.add(cur)
            visited.remove(cur)
            return True
                

        for c, _ in enumerate(deps):
            if not completable(c):
                return False
        return True

            
# NeetCode Solution
# Pretty much the same as mine, but they used a dict, which I actually do not
# agree with at all. Dicts would not be faster than arrays in this case.
# Both yield O(1) time lookup, but arrays are significantly faster.
class NeetCodeSolution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs
        preMap = {i: [] for i in range(numCourses)}

        # map each course to : prereq list
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return False
            if preMap[crs] == []:
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
 
