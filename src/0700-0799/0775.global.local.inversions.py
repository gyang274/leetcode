from typing import List

class Solution:
  def isIdealPermutation(self, A: List[int]) -> bool:
    for i, x in enumerate(A):
      if x < i - 1 or x > i + 1:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,0,2],
    [1,2,0],
  ]
  rslts = [solver.isIdealPermutation(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
