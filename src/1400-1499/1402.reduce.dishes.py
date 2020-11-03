from typing import List

class Solution:
  def maxSatisfaction(self, satisfaction: List[int]) -> int:
    ns = sorted(filter(lambda x: x <  0, satisfaction))
    ps = sorted(filter(lambda x: x >= 0, satisfaction))
    ans, score = sum(x * (i + 1) for i, x in enumerate(ps)), sum(ps)
    while ns and score + ns[-1] > 0:
      score += ns.pop()
      ans += score
    return ans

class Solution:
  def maxSatisfaction(self, satisfaction: List[int]) -> int:
    s = sorted(satisfaction)
    ans, run = 0, 0
    while s and run + s[-1] > 0:
      run += s.pop()
      ans += run
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [4,2,3],
    [-4,-1,-5],
    [-1,-8,0,5,-9],
    [-2,5,-1,0,3,-3],
  ]
  rslts = [solver.maxSatisfaction(satisfaction) for satisfaction in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
