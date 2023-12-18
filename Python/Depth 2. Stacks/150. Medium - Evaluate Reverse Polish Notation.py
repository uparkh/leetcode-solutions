class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+": stack.append(stack.pop() + stack.pop())
            elif token == "-": stack.append(-stack.pop() + stack.pop())
            elif token == "*": stack.append(stack.pop() * stack.pop())
            elif token == "/":
                divisor = stack.pop()
                stack[-1] = int(stack[-1] / divisor)
            else:
                stack.append(int(token))
        return stack[0]

print(Solution().evalRPN(["4","13","5","/","+"]))
