import time

class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        h = self.tweets[userId][::]
        for followeeId in self.follows[userId]:
            h.extend(self.tweets[followeeId])
        heapify(h)
        
        ans = []
        for _ in range(10):
            if not h:
                break
            ans.append(heappop(h)[1])
        return ans
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)