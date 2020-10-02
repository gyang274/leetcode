from typing import List

import heapq

class Solution:
  def isPossible(self, target: List[int]) -> bool:
    # reverse simulation
    # Key: the total sum always larger than all elements, implies decompose the largest number.
    #  each round get the current maximum value, and replace by the sum of other elements.
    # TC: O(N) or O(NlogN) for priority queue, O(log(xmax) * logN) for loop. SC: O(N).
    q, s = [-x for x in target], sum(target)
    heapq.heapify(q)
    while q:
      x = -heapq.heappop(q)
      s -= x
      if x == 1 or s == 1:
        return True
      if x < s or s == 0 or x % s == 0:
        return False
      # note: x %= s rather than x -= s
      x %= s
      s += x
      heapq.heappush(q, -x)
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1],
    [2],
    [8,5],
    [1,2],
    [1,1,2],
    [9,3,5],
    [1,1,1,2],
    [1,1,4,7],
    [1,100000],
  ]
  rslts = [solver.isPossible(target) for target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
