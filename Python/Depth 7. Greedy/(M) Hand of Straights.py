from typing import List
from collections import defaultdict

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
