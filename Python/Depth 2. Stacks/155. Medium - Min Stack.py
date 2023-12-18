class MinStack:

    def __init__(self):
        self.core = []
        self.minStack = []
        # self.minMap = {} okay, maybe I don't need a map for every single situation
        # general rule: only use maps when keys are to be stored ONLY in this container,
        # nowhere else. Example: if the original nums are stored in self.core, then don't re-store
        # them as keys in a map! Just use that array to store your keys.

        # Or in other words, if the key-value pairs I'm storing are already related to each other
        # by a property given from the problem or some fundamental property, don't use a map/dict!
        # Maps/dicts should only be used when the key and the value don't already have some
        # relationship between them. Otherwise, if I do use them regardless, I will be using
        # unneccessary space and time.

        # Like in this problem, the "key" of the original stack values is related to the "value" I
        # was trying to store, in that both items are in the original stack. 


    def push(self, val: int) -> None:
        self.core.append(val)

        # This does what I intended to do, as in, it "maps" the latest value on the core stack
        # to what the logically minimum value is, but without using a map, just another array
        # to store the "values" of the "keys" from self.core.
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.core.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.core[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
    def __str__(self) -> str:
        return self.core.__str__

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(4)

print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
