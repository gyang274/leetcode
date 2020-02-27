from typing import List

class Solution:
  def hIndex(self, citations: List[int]) -> int:
    """O(N), hold an array h where h[i] is num of paper with citation i, except h[n] is num paper citation >= n.
      Then, roll from right, until h[i] >= i, hIndex is i.
    """
    n = len(citations)
    # construct h array
    h = [0] * (n + 1)
    for i in citations: 
      h[min(i, n)] += 1
    # roll from right
    for i in range(n, -1, -1):
      if h[i] >= i:
        return i
      h[i - 1] += h[i]
    # return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [0],
    [1],
    [2],
    [1,2],
    [2,3],
    [2,3,0,8,5],
  ]
  rslts = [solver.hIndex(citations) for citations in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")