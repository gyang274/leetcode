from collections import defaultdict, deque

import heapq

class Twitter:

  def __init__(self):
    """Initialize your data structure here.
    """
    self.users = defaultdict(lambda: {
      'tweets': deque([]), 'followed': set([])
    })
    # numTweets: num of tweets in the news feed
    self.numTweets = 10
    # idxTweets: record the recency of a tweets
    self.idxTweets = -1

  def postTweet(self, userId: int, tweetId: int) -> None:
    """Compose a new tweet.
    """
    self.users[userId]['tweets'].appendleft((self.idxTweets, tweetId))
    self.idxTweets -= 1
    if len(self.users[userId]['tweets']) > self.numTweets:
      self.users[userId]['tweets'].pop()

  def getNewsFeed(self, userId: int) -> List[int]:
    """Retrieve the 10 most recent tweet ids in the user's news feed. 
      Each item in the news feed must be posted by users who the user followed or by the user herself. 
      Tweets must be ordered from most recent to least recent.
    """
    q = [(idx, tweet) for idx, tweet in self.users[userId]['tweets']]
    heapq.heapify(q)
    for followeeId in self.users[userId]['followed']:
      for idx, tweet in self.users[followeeId]['tweets']:
        if (idx, tweet) not in q:
          heapq.heappush(q, (idx, tweet))
    r = []
    while q and len(r) < self.numTweets:
      r.append(heapq.heappop(q)[1])
    return r

  def follow(self, followerId: int, followeeId: int) -> None:
    """Follower follows a followee. If the operation is invalid, it should be a no-op.
    """
    self.users[followerId]['followed'].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    """Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    """
    self.users[followerId]['followed'].discard(followeeId)