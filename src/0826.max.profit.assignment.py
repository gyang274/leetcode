from typing import List

import bisect

class Solution:
  def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    """TC: O(WlogN), W is num of worker, N is num of jobs (difficulty, profit).
    """
    # (difficulty, profit): filter so that profit increase as difficulty increase, 
    # and then assign each worker to the most difficult aka profitable possible one
    dp = sorted([(d, -p) for d, p in zip(difficulty, profit)])
    ds, ps = [0], [0]
    for d, p in dp:
      if d > ds[-1] and -p > ps[-1]:
        ds.append(d)
        ps.append(-p)
    return sum(ps[bisect.bisect(ds, w) - 1] for w in worker)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,4,4,6,8,10], [10,22,20,30,40,50], [4,5,6,7]),
  ]
  rslts = [solver.maxProfitAssignment(difficulty, profit, worker) for difficulty, profit, worker in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
