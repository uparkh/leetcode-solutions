# My Original Incorrect Solution 
# I was on the right path, I think I was right in knowing that we had to track
# which wildcards needed to be which type of parenthesis. And for that we need
# to do at least one pass through the string.
# Unfortunately I could not figure out a good way to verify the correctness
# of the parentheses within a reasonable amount of time.
class Solution:
    def checkValidString(self, s: str) -> bool:
        order = []
        count_wild = 0
        for c in s:
            if c == '(':
                order.append(')')
            elif c == ')':
                if not order:
                    order.append('(')
                elif order[-1] == ')':
                    order.pop()  # what we were looking for
                else:  # order top == '('
                    order.append('(')
            elif c == '*':
                count_wild += 1

        print(order, count_wild)
        return len(order) <= count_wild


# NeetCode Solution
# ***************** "If you cannot maintain 2 necessary states in one variable
# ***************** then that's a hint you need more variables."

# ***************** Wildcards create diverging state branches.


# Pretty clever, track range of possible left '(' states due to wildcards.
# If possible to close all of them (leftMin == 0), there is a state that
# exists to solve the string.

# Dynamic Programming: O(n^2)
# Greedy: O(n)
class NeetCodeSolution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:  # '*' creates diverging states
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:  # no valid states possible
                return False
            if leftMin < 0:  # required because -> s = ( * ) (
                leftMin = 0
        return leftMin == 0


