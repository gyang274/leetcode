from typing import List
from collections import Counter

class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    x = Counter(map(lambda x: x % 60, time))
    count = 0
    for i in x:
      if i == 0 or i == 30:
        count += x[i] * (x[i] - 1)
      else:
        count += x[i] * x[60 - i]
    return count // 2

class Solution:
  def numPairsDivisibleBy60(self, time: List[int]) -> int:
    r = [0] * 60
    count = 0
    for t in time:
      count += r[-t % 60]
      r[t % 60] += 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [30,20,150,100,40,60,60,60],
  ]
  rslts = [solver.numPairsDivisibleBy60(time) for time in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
