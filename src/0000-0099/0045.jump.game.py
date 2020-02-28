from typing import List
from collections import OrderedDict

class Solution:
  def jump(self, nums: List[int]) -> int:
    """Dynamic Programming: O(n^2).
    """
    n = len(nums)
    nums[n - 1] = 0
    for i in range(n - 2, -1, -1):
      if nums[i] > 0:
        s = set(nums[(i + 1):(i + nums[i] + 1)])
        s.discard(-1)
        if len(s) > 0:
          nums[i] = min(s) + 1
        else:
          nums[i] = -1
      else:
        nums[i] = -1
    return nums[0]


class Solution:
  def jump(self, nums: List[int]) -> bool:
    """Greedy Approach: O(n^2).
      Keep a list [(i, j), ..] for boundary i of each min step j, where i1 > i2 for j1 < j2.
    """
    n = len(nums)
    # r: reachable boundary, for each k (r key), left most i (nums index, r value) that can reach last index with step k
    r = OrderedDict()
    # nums: in-place update nums[i] to k, num of step to reach last index, from right to left
    nums[n - 1] = 0
    # init
    r[0] = n - 1
    for i in range(n - 2, -1, -1):
      for j, k in r.items():
        if i + nums[i] >= k:
          nums[i] = j + 1
          r[j + 1] = i
          break
      # yes, else outside for loop in case all if in for loop fails
      else:
        nums[i] = -1
      # print(f"{r=}, {nums=}")
    return nums[0]


class Solution:
  def jump(self, nums: List[int]) -> bool:
    """BFS.
    """
    # k: step, v: visited, b: boundary, e: extended
    k, v, b, e, n = 0, set(), {0}, set(), len(nums)
    while not (n - 1) in b:
      while b:
        i = b.pop()
        v.add(i)
        for j in range(nums[i] + 1):
          if not ((i + j in v) or (i + j) in b):
            e.add(i + j)
      e, b = b, e
      k += 1
    return k


class Solution:
  def jump(self, nums: List[int]) -> bool:
    """BFS.
    """
    k, l, r, n = 0, 0, 0, len(nums)
    while r < n - 1:
      l, r = r + 1, max(i + nums[i] for i in range(l, r + 1))
      k += 1
    return k


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [2,3,1,1,4], # 2
    [2,3,0,1,4], # 2
  ]
  rslts = [solver.jump(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")