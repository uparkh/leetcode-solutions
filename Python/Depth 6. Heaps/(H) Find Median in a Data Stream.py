import heapq

# My Original Solution -- 53 min
# Almost finished all main LC test cases.
# Pretty proud of myself for this.
class MedianFinder:

    def __init__(self):
        self.lower_max_heap = []  # lesser half of sorted data stream
        self.higher_min_heap = []  # greater half of sorted data stream
        self.buf = []  # buffer for balancing each side, max len = 2

    def addNum(self, num: int) -> None:
        self.buf.append(num)
        if len(self.buf) == 2:
            heapq.heappush(self.lower_max_heap, -min(self.buf))
            heapq.heappush(self.higher_min_heap, max(self.buf))
            self.buf.clear()
    
    def balance(self):
        # balance before doing anything else
        # prefer higher_min_heap to have odd median
        while len(self.lower_max_heap) < len(self.higher_min_heap) - 1:
            heapq.heappush(self.lower_max_heap, -heapq.heappop(self.higher_min_heap))
        while len(self.lower_max_heap) > len(self.higher_min_heap):
            heapq.heappush(self.higher_min_heap, -heapq.heappop(self.lower_max_heap))


    def findMedian(self) -> float:
        if self.lower_max_heap:  # one must imply both have smth
            left_mid = -self.lower_max_heap[0]
            right_mid = self.higher_min_heap[0]
            # flush buffer 
            if self.buf: # logically must have one value here if not empty
                val = self.buf.pop()
                if val < left_mid:
                    heapq.heappush(self.lower_max_heap, -val)
                elif val <= right_mid:  # in between
                    heapq.heappush(self.higher_min_heap, val)
                else:
                    heapq.heappush(self.higher_min_heap, val)
                self.balance()
            if len(self.lower_max_heap) == len(self.higher_min_heap):
                left_mid = -self.lower_max_heap[0]
                right_mid = self.higher_min_heap[0]
                return (left_mid + right_mid)/2
            else:
                return self.higher_min_heap[0]
        # no heap elems, func must be called after >= 1 elem in buf
        return self.buf[0]
        

