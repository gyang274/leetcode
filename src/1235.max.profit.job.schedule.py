from typing import List

import bisect

class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # dp, O(NlogN), go through by (endTime, max-profit)
    # dp[e] = max(dp[e], dp[s-] + profit), s- <= s max of profit
    dp = [(0, 0)]
    # x: sorted (e, s, p)
    x = sorted((e, s, p) for s, e, p in zip(startTime, endTime, profit))
    for e, s, p in x:
      i = bisect.bisect_right(dp, (s, float('inf')))
      m = max(dp[-1][1], dp[i - 1][1] + p)
      while dp[-1][0] == e:
        dp.pop()
      dp.append((e, m))
    return dp[-1][1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,1,1], [2,3,4], [5,6,4]),
    ([1,2,3,3], [3,4,5,6], [50,10,40,70]),
    ([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]),
  ]
  rslts = [solver.jobScheduling(startTime, endTime, profit) for startTime, endTime, profit in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

      

    
