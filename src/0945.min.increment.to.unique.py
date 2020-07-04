from typing import List

class Solution:
  def minIncrementForUnique(self, A: List[int]) -> int:
    A.sort()
    count = 0
    for i in range(1, len(A)):
      if A[i] <= A[i - 1]:
        count += A[i - 1] + 1 - A[i]
        A[i] = A[i - 1] + 1
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
    [3,2,1,2,1,7],
  ]
  rslts = [solver.minIncrementForUnique(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
