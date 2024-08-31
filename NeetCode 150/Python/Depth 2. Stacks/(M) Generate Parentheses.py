# Recursive solution, but does not work for n >= 6, not sure why. Should have used stacks,
# considering that this problem was under the "Stacks" section of NC150.
# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         if n == 1: return ["()"]
#         else:
#             res = []
#             for i in range(n-1, 0, -1):
#                 prev = Solution().generateParenthesis(n-i)
#                 res += ["("*i + elem + ")"*i for elem in prev]
#                 res += ["("*i + ")"*i + elem for elem in prev]
#                 res += [elem + "("*i + ")"*i for elem in prev]
#             return list(set(res))

# From watching NC's video solution, I realized that stacks should be used with anything
# that needs to be processed in order, and which also will have to be reprocessed when coming back.
# - can only add closing parenthesis when openCount < closeCount
# - can have n opening and n closing parentheses = 2n total parentheses
# From these 2 rules for this problem, you can build the decision-making tree, and only add
# the states that have length = 2n
# In general, when encountering any "all possible combinations questions" I think going through
# each decision to build out a possible combination helps a lot with solving the problem.

# Like in Discrete when dealing with combinations/permutation questions, sometimes the answer is
# arrived at by first finding what is possible from a base state, then looking at what can happen
# after a decision at the base state, etc, until we find the total number of possible combinations.

# Similarly, when dealing with all possible combination/permutation problems coding-wise, it seems
# just as helpful to start at the base state, and make a decision-tree about where I can go from
# a given state. Doing this helps me figure out different rules/conditions I can use in my algorihtm.
# If the same conditions govern every decision, then there's a chance recursion is used.
# Recursion is still inherently useful in solving these types of problems, so I was correct in that
# regard.

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res


print(Solution().generateParenthesis(4))

