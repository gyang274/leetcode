from typing import List

class Solution:
  def sumSubarrayMins(self, A: List[int]) -> int:
    # note: A[i] >= 1, otherwise stack = [(-float("inf"), -1)]
    stack, m, s = [(0, -1)], 0, 0
    for i, x in enumerate(A):
      # amortized O(1)
      while x <= stack[-1][0]:
        y, j = stack.pop()
        m -= (j - stack[-1][1]) * y
      m += (i - stack[-1][1]) * x
      stack.append((x, i))
      s += m
    return s % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,1,2,4],
    [2,3,1,1,4],
    [3,2,1,5,4],
  ]
  rslts = [solver.sumSubarrayMins(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
