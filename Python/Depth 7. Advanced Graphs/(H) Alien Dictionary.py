from typing import List
# I couldn't figure this out. I knew I needed to use topological sort, but
# couldn't figure out how to set up the Directed Acyclic Graph (DAG) to apply it.


# NeetCode Solution Notes
# He just compared each pair of words and added the first different character to the graph.
# Where the first pair's different char comes before the second pair's different char.
# He then used topological sort to get the order of the characters.
# Cycles mean an incorrect input ordering, so no real solution exists.
class NCSolution:
    def alienOrder(self, words: List[str]) -> str:
        # could have just used defaultdict
        adj = {char: set() for word in words for char in word}

        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2))
            # if w1 is larger than w2 and the first minLen characters are the same
            # w2 can't come before w1, invalid ordering
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    print(w1[j], w2[j])
                    adj[w1[j]].add(w2[j])
                    break

        visited = {}  # {char: bool} False visited, True current path
        res = []

        # topological sort
        def dfs(char):
            if char in visited:
                return visited[char]

            visited[char] = True

            for neighChar in adj[char]:
                if dfs(neighChar):
                    return True

            visited[char] = False
            res.append(char)

        for char in adj:
            # if there is a cycle (True rv), return ""
            if dfs(char):
                return ""

        res.reverse()
        return "".join(res)
