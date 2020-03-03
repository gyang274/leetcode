from typing import List

class Solution:
  def hIndex(self, citations: List[int]) -> int:
    """modified binary search to find i, s.t., c[-i] >= i, c[-(i+1)] < i + 1
    """
    n = len(citations)
    # citations is sorted (better if sorted reversely)
    l, r = 0, n - 1
    while l <= r:
      m = l + (r - l) // 2
      if citations[m] == n - m:
        return n - m
      elif citations[m] < n - m:
        l = m + 1
      else:
        r = m - 1
    return n - l

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [0],
    [1],
    [2],
    [1,2],
    [2,3],
    [0,2,3,5,8],
  ]
  rslts = [solver.hIndex(citations) for citations in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")