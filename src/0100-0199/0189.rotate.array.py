from typing import List

class Solution:
  def rotate(self, nums: List[int], k: int) -> None:
    """Do not return anything, modify nums in-place instead.
    Key:
      1. deque: pop() and appendleft().
      2. push replacement through cyclic replacement
      3. double reverse: reverse nums[:], and then reverse nums[:k] and nums[k:] respectively
    """
    n = len(nums)
    i, count = 0, 0
    while count < n:
      j = (i + k) % n
      while not j == i:
        nums[i], nums[j] = nums[j], nums[i]
        count += 1
        j = (j + k) % n
      # the last swap complete the replacement of 2 indices
      count += 1
      i += 1

class Solution:
  def reverse(self, nums, i, j):
    while i < j:
      nums[i], nums[j] = nums[j], nums[i]
      i += 1
      j -= 1
  def rotate(self, nums: List[int], k: int) -> None:
    if len(nums) > 0:
      k %= len(nums)
      self.reverse(nums, 0, len(nums) - 1)
      self.reverse(nums, 0, k - 1)
      self.reverse(nums, k, len(nums) - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], 2),
    ([1], 2),
    ([1,2], 2),
    ([1,2,3], 2),
    ([1,2,3,4,5,6], 2),
    ([1,2,3,4,5,6], 3),
    ([1,2,3,4,5,6,7], 5),
  ]
  rslts = [solver.rotate(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
    