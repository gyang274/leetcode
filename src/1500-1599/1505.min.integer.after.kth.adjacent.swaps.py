from typing import List
from collections import defaultdict, deque

import bisect

class Solution:
  def minInteger(self, num: str, k: int) -> str:
    # greedy, always find the smallest possible and move it to front
    # TC: O(N^2) navie implement, O(NlogN) use binary search tree or segment tree
    n, d = len(num), defaultdict(deque)
    for i, x in enumerate(num):
      d[x].append(i)
    ans, seen = '', []
    for _ in range(n):
      for x in '0123456789':
        if d[x]:
          i = d[x][0]
          # adjusted index after moving some to the front
          j = i + (len(seen) - bisect.bisect(seen, i))
          # num of swaps needed to move this one to the front after previous moves
          m = j - len(seen)
          if m <= k:
            # always, some m will <= k at each step..
            k -= m
            d[x].popleft()
            ans += x
            # this is O(N), but can achieve O(logN) use BST or ST
            # one solution is to use SortedList from sortedcontainers
            bisect.insort(seen, i)
            break
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("9438957234785635408", 23),
  ]
  rslts = [solver.minInteger(num, k) for num, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
