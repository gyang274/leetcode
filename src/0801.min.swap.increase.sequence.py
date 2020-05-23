from typing import List

class Solution:
  def minSwap(self, A: List[int], B: List[int]) -> int:
    """dynamic programmin + memoryless -> status machine
    """
    n = len(A)
    # x, s: num of swaps if A[i], B[i] stay at place, swap with each other.
    x0, s0  = 0, 1
    for i in range(1, n):
      x1 = s1 = float('inf')
      if A[i] > A[i - 1] and B[i] > B[i - 1]:
        x1, s1 = min(x1, x0), min(s1, s0 + 1)
      if A[i] > B[i - 1] and B[i] > A[i - 1]:
        x1, s1 = min(x1, s0), min(s1, x0 + 1)
      x0, s0 = x1, s1
    return min(x0, s0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,5], [2,3,5,8]),
    ([1,3,5,4], [1,2,3,7]),
  ]
  rslts = [solver.minSwap(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
