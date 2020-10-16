from typing import List

class Solution:
  def maxScore(self, cardPoints: List[int], k: int) -> int:
    s = sum(cardPoints[:k])
    m = s
    for i in range(1, k + 1):
      s += cardPoints[-i] - cardPoints[k - i]
      m = max(m, s)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 2),
    ([3,2,1,0,4], 3),
  ]
  rslts = [solver.maxScore(cardPoints, k) for cardPoints, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
