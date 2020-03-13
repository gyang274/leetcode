import heapq

class HitCounter:

  def __init__(self):
    """Initialize your data structure here.
    """
    # secondCounts: (timestamp, counts)
    # make it scalable, large num of hit at each second, count it and send to priority queue once.
    self.secondCounts = [0, 0]
    # queue: priority queue (timestamp, counts)
    self.queue = []
    heapq.heapify(self.queue)

  def hit(self, timestamp: int) -> None:
    """Record a hit.
      @param timestamp - The current timestamp (in seconds granularity).
    """
    if timestamp == self.secondCounts[0]:
      self.secondCounts[1] += 1
    else:
      heapq.heappush(self.queue, self.secondCounts)
      self.secondCounts = [timestamp, 1]
    
  def getHits(self, timestamp: int) -> int:
    """Return the number of hits in the past 5 minutes.
      @param timestamp - The current timestamp (in seconds granularity).
    """
    # purge queue into last 5mins.
    while self.queue and timestamp - self.queue[0][0] >= 300:
      heapq.heappop(self.queue)
    # numHits (on disk) from self.queue
    numHits = sum([x[1] for x in self.queue])
    # add most recent (in memory) hits from self.secondsCount
    if timestamp - self.secondCounts[0] < 300:
      numHits += self.secondCounts[1]
    return numHits