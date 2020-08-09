from typing import List

class Solution:
  def twoSumLessThanK(self, A: List[int], K: int) -> int:
    n = len(A)
    # O(NlogN) sort
    A.sort()
    # O(N) two pointer
    i, j, s = 0, n - 1, -1
    while i < j:
      while i < j and A[i] + A[j] >= K:
        j -= 1
      if i < j:
        s = max(s, A[i] + A[j])
      i += 1
    return s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], 5),
    ([34,23,1,24,75,33,54,8], 60),
  ]
  rslts = [solver.twoSumLessThanK(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
