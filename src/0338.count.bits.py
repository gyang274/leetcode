from typing import List

class Solution:
  def countBits(self, num: int) -> List[int]:
    """num bits:
      0 -> 1
      0, 1 -> 1, 2
      0, 1, 1, 2 -> 1, 2, 2, 3
    """
    x = [0]
    while len(x) < num + 1:
      x.extend([i + 1 for i in x])
    return x[:(num + 1)]

class Solution:
  def countBits(self, num: int) -> List[int]:
    """num bits:
      0 -> 1
      0, 1 -> 1, 2
      0, 1, 1, 2 -> 1, 2, 2, 3
    """
    # allocate space all at once
    x = [0] * (num + 1)
    # assign value w.r.t double plus rule
    j = 1
    while j < num + 1:
      for i in range(j, min(j * 2, num + 1)):
        x[i] = x[i % j] + 1
      j *= 2
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2,3,5,8,
  ]
  rslts = [solver.countBits(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")