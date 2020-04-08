from typing import List

class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    # nums: map 0, 1 -> -1, 1, then cumulative sum
    # sum(nums[i:j]) == 0 iff so equal num of 0s, 1s
    n = len(nums)
    if n == 0:
      return 0
    nums[0] = -1 if nums[0] == 0 else 1
    for i in range(1, n):
      if nums[i] ^ 1:
        nums[i] -= 1
      nums[i] += nums[i - 1]
    # hashmap r = sum(nums[:i]) -> i
    # sum(nums[i:j]) == 0 iff sum(nums[:i]) == 0 or sum(nums[:i]) = sum(nums[:j])
    d, maxlen = {}, 0
    for i in range(n):
      r = nums[i]
      if r == 0:
        maxlen = i + 1
      else:
        if r in d:
          maxlen = max(maxlen, i - d[r])
        else:
          d[r] = i
    return maxlen

class Solution:
  def findMaxLength(self, nums: List[int]) -> int:
    # nums: map 0, 1 -> -1, 1, then cumulative sum
    # sum(nums[i:j]) == 0 iff so equal num of 0s, 1s
    d, r, m, n = {}, 0, 0, len(nums)
    # hashmap r = sum(nums[:i]) -> i
    # sum(nums[i:j]) == 0 iff sum(nums[:i]) == 0 or sum(nums[:i]) = sum(nums[:j])
    d[0] = -1
    for i in range(n):
      r += -1 if nums[i] == 0 else 1
      if r in d:
        m = max(m, i - d[r])
      else:
        d[r] = i
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,1,0,0,1],
  ]
  rslts = [solver.findMaxLength(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")