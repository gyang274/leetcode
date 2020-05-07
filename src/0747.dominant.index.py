import heapq

class Solution:
  def dominantIndex(self, nums: List[int]) -> int:
    queue = [(-x, i) for i, x in enumerate(nums)]
    heapq.heapify(queue)
    x, i = heapq.heappop(queue)
    if queue:
      y, j = heapq.heappop(queue)
      if -y * 2 > -x:
        return -1
    return i