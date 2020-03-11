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

class Solution:
  def hammingWeight(self, n: int) -> int:
    """bit manipulation:
      n & (n - 1) flip the rightmost 1 into 0
      n & ~(n - 1) or n & (-n) get out rigthmost 1 with trailing zeros, e.g., rightmost 1's index
    """
    ans = 0
    while n > 0:
      n &= (n - 1)
      ans += 1
    return ans
  def countBits(self, num: int) -> List[int]:
    """Q191
    """
    x = [0] * (num + 1)
    for i in range(1, num + 1):
      x[i] = self.hammingWeight(i)
    return x

class Solution:
  def countBits(self, num: int) -> List[int]:
    """dyanmic programming + least significant bit
    """
    x = [0] * (num + 1)
    for i in range(1, num + 1):
      x[i] = x[i >> 1] + (i & 1)
    return x

class Solution:
  def countBits(self, num: int) -> List[int]:
    """dyanmic programming + last set bit
    """
    x = [0] * (num + 1)
    for i in range(1, num + 1):
      x[i] = x[i & (i - 1)] + 1
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2,3,5,8,
  ]
  rslts = [solver.countBits(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")