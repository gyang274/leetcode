from typing import List

class Solution:
  def totalHammingDistance(self, nums: List[int]) -> int:
    """O(NL), L = int(log(max(nums), 2))
    """
    if len(nums) == 0:
      return 0
    # count num of 0s and 1s at each index
    n = max(nums).bit_length()
    z = [[0, 0] for _ in range(n)]
    for x in nums:
      for i in range(n):
        if x > 0:
          z[i][x & 1] += 1
          x >>= 1
        else:
          z[i][0] += 1
    return sum([n0 * n1 for n0, n1 in z])

class Solution:
  def totalHammingDistance(self, nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
      return 0
    # count num of 1s at each index
    z = [0] * 32
    for x in nums:
      i = 0
      while x > 0:
        z[i] += x & 1
        x >>= 1
        i += 1
    return sum([n1 * (n - n1) for n1 in z])

class Solution:
  def totalHammingDistance(self, nums: List[int]) -> int:
    return sum((b.count('0') * b.count('1')) for b in zip(*map('{:032b}'.format, nums)))
    
if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,4,2,42],
  ]
  rslts = [solver.totalHammingDistance(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")