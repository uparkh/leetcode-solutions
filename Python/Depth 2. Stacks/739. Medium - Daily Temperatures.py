# O(n^2) brute-force solution
# class Solution:
#     def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
#         stacks = [[t] for t in temperatures]
#         for i, stack in enumerate(stacks):
#             found = False
#             first = stack[-1]
#             for temp in temperatures[i+1:]:
#                 if first < temp:
#                     found = True
#                     break
#                 else: stack.append(temp)
#             if not found: stack.clear()
        
#         return [len(s) for s in stacks]


# Tip that I have learned: write out the psuedo-code/code for the algorithm as I am thinking about
# the problem and drawing it. Oftentimes while drawing the decision-making process about how the
# solution is build from the input, important boolean expressions are checked using properties
# derived from the problem, or I am looping through something a certain way, and I need to 
# write down these things, it will help me build my algorithm. It can also help me detect where
# things go wrong.

# That, or alternatively, as I am drawing it out, be conscious about the steps I am taking.
# Always think: can I do this next thing in one discrete step? Remember that the drawn solution
# must be able to be done in one-by-one steps (an algorithm), so be conscious of every step I take.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res, stack = [0] * len(temperatures), []
        for i, temp in enumerate(temperatures):
            # res.append(0)
            # if len(stack) != 0:
            while (len(stack) != 0 and temp > temperatures[stack[-1]]):
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return res

print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))
