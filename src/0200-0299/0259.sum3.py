from typing import List
from collections import defaultdict

class Solution:
  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    """Sort O(NlogN) + for each k from n - 1 -> 2: O(N), find (i, j) using two pointers: O(N), so O(N^2).
    """
    nums.sort()
    counter = 0
    for k in range(len(nums) - 1, 1, -1):
      i = 0
      for j in range(k - 1, 0, -1):
        # Note: i is inherit from previous j, since nums[j - 1] < nums[j], after sorting the nums,
        # so if nums[i] + nums[j] + nums[k] < target then nums[i] + nums[j - 1] + nums[k] < target
        # Thus, i and j together is O(N), e.g., go through 0 -> k once.
        while i < j and nums[i] + nums[j] + nums[k] < target:
          i += 1
        # once j moved backward enough, when nums[j] * 2 + nums[k] < target, then no need to move i back, 
        # because we simply know that all i, i < j, will satisify nums[i] + nums[j] + nums[k] < target.
        # counter += min(i, j - 1 + 1), since i is pointing to the 1st nums[i] + nums[j] + nums[k] >= target
        # whereas j is pointing to nums[j] * 2 + nums[k] < target
        counter += min(i, j)
    return counter

class Solution:
  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    """Sort O(NlogN) + for each k from n - 1 -> 2: O(N), find (i, j) using two pointers: O(N), so O(N^2).
    """
    nums.sort()
    counter = 0
    # further re-use the i, j for each k, similar as re-use i for j.
    imax = defaultdict(lambda: 0)
    for k in range(len(nums) - 1, 1, -1):
      if nums[k] * 3 >= target:
        i = imax[k - 1]
        for j in range(k - 1, 0, -1):
          # Note: i is inherit from previous j, since nums[j - 1] < nums[j], after sorting the nums,
          # so if nums[i] + nums[j] + nums[k] < target then nums[i] + nums[j - 1] + nums[k] < target
          # Thus, i and j together is O(N), e.g., go through 0 -> k once.
          while i < j and nums[i] + nums[j] + nums[k] < target:
            i += 1
          imax[j] = min(i, j)
          # once j moved backward enough, when nums[j] * 2 + nums[k] < target, then no need to move i back, 
          # because we simply know that all i, i < j, will satisify nums[i] + nums[j] + nums[k] < target.
          # counter += min(i, j - 1 + 1), since i is pointing to the 1st nums[i] + nums[j] + nums[k] >= target
          # whereas j is pointing to nums[j] * 2 + nums[k] < target
          # counter += min(i, j)
          if i < j:
            counter += i
          else:
            counter += (j + 1) *  j // 2
            break
      else:
        print('break at k', k)
        counter += (k + 1) * k * (k - 1) // 6
        break
    return counter

class Solution:
  def threeSumSmaller(self, nums: List[int], target: int) -> int:
    """Sort O(NlogN) + for each k from n - 1 -> 2: O(N), find (i, j) using two pointers: O(N), so O(N^2).
    """
    nums.sort()
    counter = 0
    # further re-use the i, j for each k, similar as re-use i for j.
    imax = defaultdict(lambda: 0)
    for k in range(len(nums) - 1, 1, -1):
      i = imax[k - 1]
      if i < k - 1:
        for j in range(k - 1, 0, -1):
          # Note: i is inherit from previous j, since nums[j - 1] < nums[j], after sorting the nums,
          # so if nums[i] + nums[j] + nums[k] < target then nums[i] + nums[j - 1] + nums[k] < target
          # Thus, i and j together is O(N), e.g., go through 0 -> k once.
          while i < j and nums[i] + nums[j] + nums[k] < target:
            i += 1
          imax[j] = min(i, j)
          # once j moved backward enough, when nums[j] * 2 + nums[k] < target, then no need to move i back, 
          # because we simply know that all i, i < j, will satisify nums[i] + nums[j] + nums[k] < target.
          # counter += min(i, j - 1 + 1), since i is pointing to the 1st nums[i] + nums[j] + nums[k] >= target
          # whereas j is pointing to nums[j] * 2 + nums[k] < target
          # counter += min(i, j)
          if i < j:
            counter += i
          else:
            counter += (j + 1) *  j // 2
            break
      else:
        counter += (k + 1) * k * (k - 1) // 6
        break
    return counter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([], 0),
    ([0,0,0], 0),
    ([0,0,0], 1),
    ([-2,0,1,3], 2),
    ([3,2,-2,6,2,-2,6,-2,-4,2,3,0,4,4,1], 3),
  ]
  rslts = [solver.threeSumSmaller(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")