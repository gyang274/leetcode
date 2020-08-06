from typing import List

class Solution:
  def sumOfDigits(self, A: List[int]) -> int:
    x, z = min(A), 0
    while x > 0:
      z += x % 10
      x //= 10
    return (z & 1) ^ 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.sumOfDigits(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
