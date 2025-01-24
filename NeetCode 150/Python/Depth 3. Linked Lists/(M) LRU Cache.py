from typing import Self

class DequeNode:
    def __init__(self, val: int, prev: Self, next: Self):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    def __init__(self):
        self.head = DequeNode(0, None, None)
        self.tail = DequeNode(0, self.head, None)
        self.head.next = self.tail

    def append(self, val: int):
        new = DequeNode(val, self.tail.prev, self.tail)
        self.tail.prev.next = new
        self.tail.prev = new
        return new

    def pop_node(self, node: DequeNode):
        node.prev.next = node.next
        node.next.prev = node.prev

    def pop_left(self):
        val = self.head.next.val
        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next
        return val

class LRUCache:

    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.hmap = {}  # key -> Node, value
        self.queue = Deque()

    def get(self, key: int) -> int:
        if key in self.hmap:
            node, value = self.hmap[key]
            self.queue.pop_node(node)
            self.hmap[key] = (self.queue.append(key), value)
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hmap:
            node, _ = self.hmap[key]
            self.queue.pop_node(node)
            self.hmap[key] = (self.queue.append(key), value)
            return

        self.hmap[key] = (self.queue.append(key), value)
        self.size += 1

        if self.size > self.cap:
            popped_key = self.queue.pop_left()
            del self.hmap[popped_key]
            self.size -= 1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

lRUCache = LRUCache(2);
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)
