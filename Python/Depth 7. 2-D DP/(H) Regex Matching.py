# Gave this problem 40 mins, then gave up lmao

# I might have started with the top-down approach, but honestly I knew how
# to recursively match wildcards already, and the bottom-up approach just
# seemed more fun to try to figure out. In an interview, though, I'm just
# gonna always do recursion.

# Also made a mistake reading the problem: it asked if the string matched the
# pattern **fully** not partially. So both strings have to be done parsing
# in order to return a True. This would have helped me solve the problem so
# much more easily, but I wanna work out, so I'm not gonna sweat it right now.

# BOTTOM-UP Dynamic Programming
class DPSolution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        cache[len(s)][len(p)] = True

        for i in range(len(s), -1, -1):
            for j in range(len(p) - 1, -1, -1):
                match = i < len(s) and (s[i] == p[j] or p[j] == ".")

                if (j + 1) < len(p) and p[j + 1] == "*":
                    cache[i][j] = cache[i][j + 2]
                    if match:
                        cache[i][j] = cache[i + 1][j] or cache[i][j]
                elif match:
                    cache[i][j] = cache[i + 1][j + 1]

        return cache[0][0]


# TOP DOWN MEMOIZATION
# Just noting how easy it is to arrive at the true DP solution from
# the memoization recursive solution. It's almost as simple as replacing
# the recursive `dfs` calls with calls to the cache. Almost all the other
# logic remains unchanged...
class TDMSolution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if (j + 1) < len(p) and p[j + 1] == "*":
                cache[(i, j)] = dfs(i, j + 2) or (  # dont use *
                    match and dfs(i + 1, j)
                )  # use *
                return cache[(i, j)]
            if match:
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            cache[(i, j)] = False
            return False

        return dfs(0, 0)


