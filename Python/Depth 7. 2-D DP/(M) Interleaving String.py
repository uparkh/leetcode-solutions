# My Original Solution
# Time and Space is exponential
# Brute force unoptimized backtracking solution, did not pass time limit cases
class BadSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        stack = [(0, 0, 0)]  # (p1, p2, p3)
        while stack:
            p1, p2, p3 = stack.pop()
            if (p1, p2, p3) == (len(s1), len(s2), len(s3)):
                return True
            if p3 >= len(s3):
                continue
            if p1 < len(s1) and s1[p1] == s3[p3]:
                stack.append((p1+1, p2, p3+1))
            if p2 < len(s2) and s2[p2] == s3[p3]:
                stack.append((p1, p2+1, p3+1))

        return False


# My Original DP Solution -- too long
# Time -- O(s1.length * s2.length)
# Space -- O(s2.length)
# Would have solved this sooner if I had realized to cover the edge case
# of the two component strings not being able to make the target string
# if sum of the lengths was not the same as the length of the target.
# Lesson learned: cover the edge cases with exit clauses as soon as I think of
# them.
# Anyway -- proud that I was able to get the DP solution! That is hard
# but I came up with the algorithm in about 30m once I moved past debugging
# the recursive solution. I think any time problems are involving 2 strings
# I should think about a 2D matrix to help solve it.
class DPSolution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        dp = [-1] * (len(s2) + 1)
        for j, c2 in enumerate(s2):
            if c2 != s3[j]:
                break
            dp[j+1] = j

        simplest_matched = False
        for i, c1 in enumerate(s1):
            cur = [-1] * (len(s2) + 1)
            if c1 == s3[i] and not simplest_matched:
                cur[0] = i
            else:
                simplest_matched = True

            for j, c2 in enumerate(s2):
                left, top = -1, -1
                if cur[j] <= dp[j+1] and c1 == s3[dp[j+1] + 1]:
                    top = dp[j+1] + 1
                if cur[j] >= dp[j+1] and c2 == s3[cur[j] + 1]:
                    left = cur[j] + 1
                cur[j+1] = max(cur[j+1], left, top)

            dp = cur

        return dp[-1] == len(s3) - 1

