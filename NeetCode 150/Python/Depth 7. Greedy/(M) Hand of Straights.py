from typing import List
from collections import defaultdict
import heapq

# My Original Incorrect Solution
# I was getting close to the solution, but couldn't quite get it.
# Failed this test case, and I'd need a way of *not* adding a new card
# if it was already encountered
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # next numbers being sought after, len == groupSize at True return
        looking_for = defaultdict(int)
        for card in hand:
            print('--------------------------------')
            print(f'card: {card}')
            print(f'looking_for: \n{looking_for}')
            if looking_for[card] > 0:  # in map
                looking_for[card] -= 1  # mark it as found
            else:  # not being sought after? new set needs to be found
                for next_card in range(card+1, card + groupSize):
                    looking_for[next_card] += 1
        
        groups = sum(looking_for.values())
        print('------------ EOI -------------')
        print(f'looking_for: \n{looking_for}')
        print(groups)
        return groups == 0


# NeetCode Solution
# Interesting, used a heap. I guess there is some semblance to priority
# lower card values need to be handled first.
class NeetCodeSolution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:  # this card in set DNE, False
                    return False
                count[i] -= 1
                if count[i] == 0:  # if front set card isn't dropping to 0
                    if i != minH[0]: # other sets won't complete == Fale
                        return False
                    heapq.heappop(minH)  # remove front set card
        return True

