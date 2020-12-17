from typing import List

class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    """Lexicographic (Binary Sorted) Subsets. YG.
    """
    x, n = [], len(nums)
    for i in range(0, 1 << n):
      z, j, k = [], i, 0
      while j > 0:
        if j % 2:
          z.append(nums[k])
        j //= 2
        k += 1
      x.append(z)
    return x

# class Solution:
#   def subsets(self, nums: List[int]) -> List[List[int]]:
#     """Lexicographic (Binary Sorted) Subsets.
#     """
#     x, n = [], len(nums)
#     for i in range(2**n, 2**(n + 1)):
#       # generate bitmask, from 0..00 to 1..11
#       bitmask = bin(i)[3:]
#       # append subset corresponding to that bitmask
#       x.append([nums[j] for j in range(n) if bitmask[j] == '1'])
#     return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 5, 8],
  ]
  rslts = [solver.subsets(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")