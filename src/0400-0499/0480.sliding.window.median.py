from typing import List
from collections import defaultdict

import heapq

class Solution:
  def _search(self, s, k, x):
    l, r = 0, k
    while l < r:
      m = l + (r - l) // 2
      if s[m] >= x:
        r = m
      else:
        l = m + 1
    return l
  def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    """maintain ordered statisitic tree self-balance so insert/delete/findmedian all O(logK), use list to proxy.
    """
    n = len(nums)
    if n == 0:
      return []
    m = [None] * (n - k + 1)
    s = sorted(nums[-1:] + nums[:(k - 1)])
    for i in range(n - k + 1):
      s.remove(nums[i - 1])
      s.insert(self._search(s, k - 1, nums[i + k - 1]), nums[i + k - 1])
      if k % 2:
        m[i] = s[k // 2]
      else:
        m[i] = (s[k // 2] + s[k // 2 - 1]) / 2.0
    return m

class Solution:
  def _pushpop(self, xins, xout):
    # delete, lazy remove by marking of removal ones
    if xout is not None:
      if self.upper and xout == self.upper[0]:
        heapq.heappop(self.upper)
        self.balance -= 1
      elif self.lower and xout == -self.lower[0]:
        heapq.heappop(self.lower)
        self.balance += 1
      else:
        self.remove[xout] += 1
        if xout > self.upper[0]:
          self.balance -= 1
        else:
          self.balance += 1
    # insert + self-balance
    if not self.upper or xins >= self.upper[0]:
      heapq.heappush(self.upper, xins)
      self.balance += 1
    else:
      heapq.heappush(self.lower, -xins)
      self.balance -= 1
    # make sure balance
    while self.balance > 1:
      x = heapq.heappop(self.upper)
      if x not in self.remove:
        heapq.heappush(self.lower, -x)
        self.balance -= 2
      else:
        self.remove[x] -= 1
        if self.remove[x] == 0:
          self.remove.pop(x)
    while self.balance < 0:
      x = -heapq.heappop(self.lower)
      if x not in self.remove:
        heapq.heappush(self.upper, x)
        self.balance += 2
      else:
        self.remove[x] -= 1
        if self.remove[x] == 0:
          self.remove.pop(x)
    # make sure self.upper[0] and self.lower[0] are valid elements, as only values of these two matters to median.
    while self.upper[0] in self.remove:
      x = heapq.heappop(self.upper)
      self.remove[x] -= 1
      if self.remove[x] == 0:
        self.remove.pop(x)
    while self.lower and -self.lower[0] in self.remove:
      x = -heapq.heappop(self.lower)
      self.remove[x] -= 1
      if self.remove[x] == 0:
        self.remove.pop(x)
    return None
  def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
    """Q0295, O(5*logN), keep 2 priority queue + lazy removal for >=median and <median, find median O(1).
    """
    n = len(nums)
    if n == 0:
      return []
    # priority queues
    self.upper = []
    self.lower = []
    # lazy removal
    self.remove = defaultdict(lambda: 0)
    self.balance = 0
    self.ans = []
    for i in range(n):
      xins, xout = nums[i], None
      if i >= k:
        xout = nums[i - k]
      self._pushpop(xins, xout)
      if len(self.upper) + len(self.lower) >= k:
        if k & 1:
          self.ans.append(self.upper[0])
        else:
          self.ans.append((self.upper[0] - self.lower[0]) / 2.0)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], 0),
    ([1], 1),
    ([1,3,-1,-3,5,3,6,7,2], 3),
    ([9,7,0,3,9,8,6,5,7,6], 2),
    ([4,1,7,1,8,7,8,7,7,4], 4),
  ]
  rslts = [solver.medianSlidingWindow(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
