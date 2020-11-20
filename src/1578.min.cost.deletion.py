from typing import List

class Solution:
  def minCost(self, s: str, cost: List[int]) -> int:
    d, i, n = [], 0, len(s)
    while i < n - 1:
      if s[i] == s[i + 1]:
        j = i + 1
        while j < n and s[j - 1] == s[j]:
          j += 1
        d.append((i, j))
        i = j
      else:
        i += 1
    return sum([sum(cost[i:j]) - max(cost[i:j]) for i, j in d])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abbccc", [1,1,2,3,5,4]),
  ]
  rslts = [solver.minCost(s, cost) for s, cost in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
