from typing import List
from collections import defaultdict, deque
import heapq

# My Original Solution -- 34 minutes
# Got stuck in analysis paralysis for so long I didn't even attempt
# the problem for 16 minutes
class Twitter:

    def __init__(self):
        self.global_feed = []  # of (-<tweet_id>, <user_id>)
        self.user_following = defaultdict(set[int])  # List[ids]

    def postTweet(self, userId: int, tweetId: int) -> None:
        # assume higher tweet IDs = more recent?
        heapq.heappush(self.global_feed, (-tweetId, userId))
        if userId not in self.user_following:
            self.user_following[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = [-tw[0] for tw in self.global_feed 
                     if tw[1] in self.user_following[userId]]
        news_feed.sort(reverse=True)  # this feels very inefficient...
        return news_feed[:10]         # O(n * log(n)) where n=num tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId != followeeId and
            followeeId in self.user_following[followerId]
        ):
            self.user_following[followerId].remove(followeeId)


# so it seems that higher tweet IDs = more recent isn't true for actual LC
# website
# My 2nd Solution
# Actually just uses a stack (faster than O(n log n) getting news feed)
class Twitter2:

    def __init__(self):
        self.global_feed = deque() # of (<tweet_id>, <user_id>)
        self.user_following = defaultdict(set[int])  # List[ids]

    def postTweet(self, userId: int, tweetId: int) -> None:
        # assume higher tweet IDs != more recent
        self.global_feed.appendleft((tweetId, userId))
        if userId not in self.user_following:
            self.user_following[userId].add(userId)

    def getNewsFeed(self, userId: int) -> List[int]:
        news_feed = [tw[0] for tw in self.global_feed 
                     if tw[1] in self.user_following[userId]][:10]  # O(n)
        return news_feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.user_following:
            self.user_following[followerId].add(followerId)
        if followerId != followeeId:
            self.user_following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if (
            followerId != followeeId and
            followeeId in self.user_following[followerId]
        ):
            self.user_following[followerId].remove(followeeId)


# NeetCode Solution
# He forced the use of a heap here to organize order of tweets, but I don't
# actually think this is a better solution in practice. List comprehension
# and array lookup is gonna be faster than moving all that memory around.
class NeetCodeTwitter:
    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)  # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

