from typing import List

class Solution:
  def splitArray(self, nums: List[int], m: int) -> int:
    """dynamic programming: O(N^2 * M)
      dp[i][j] = min(max(dp[i-k][j-1], sum(nums[(i-k+1):(i+1)]), for k = 1...), split nums[:i] into j subarrays.
    """
    n = len(nums)
    if m == 1:
      return sum(nums)
    if m >= n:
      return max(nums)
    # nums to partial sum
    for i in range(1, n):
      nums[i] += nums[i - 1]
    smin = nums[-1]
    dp = [[nums[i]] * m for i in range(n)]
    for i in range(1, n):
      for j in range(1, m):
        k = 1
        while i - k + 1 >= j - 1:
          dp[i][j] = min(dp[i][j], max(dp[i - k][j - 1], nums[i] - nums[i - k]))
          if dp[i - k][j-1] < nums[i] - nums[i - k]:
            break
          k += 1
    return dp[n - 1][m - 1]

class Solution:
  def _numSplits(self, nums, x):
    """min num of splits needed if any split/subarray has sum <= x.
    """
    n, s = 1, 0
    for v in nums:
      if s + v > x:
        n += 1
        s = 0
      s += v
    return n
  def splitArray(self, nums: List[int], m: int) -> int:
    """binary search + brute force, O(N*log(sum(nums)))
    """
    n = len(nums)
    if m == 1:
      return sum(nums)
    if m >= n:
      return max(nums)
    l, r = max(nums), sum(nums)
    while l < r:
      x = l + (r - l) // 2
      if self._numSplits(nums, x) > m:
        l = x + 1
      else:
        r = x
    return l

# class Solution:
#   def recursive(self, i, j, k):
#     if (i, j, k) not in self.memo:    
#       if k == 1:
#         self.memo[(i, j, k)] = sum(self.nums[i:j])
#       elif k >= j - i:
#         self.memo[(i, j, k)] = max(self.nums[i:j])
#       else:
#         self.memo[(i, j, k)] = sum(self.nums)
#         l, r = i + k // 2 - 1, j - (k - k // 2) + 1
#         while l < r:
#           m = l + (r - l) // 2
#           sl = self.recursive(i, m, k // 2)
#           sr = self.recursive(m, j, k - k // 2)
#           self.memo[(i, j, k)] = min(max(sl, sr), self.memo[(i, j, k)])
#           if sl == sr:
#             break
#           elif sl < sr:
#             l = m + 1
#           else:
#             r = m
#     # print(f"{i=}, {j=}, {k=}, {self.memo[(i, j, k)]=}")
#     return self.memo[(i, j, k)]
#   def splitArray(self, nums: List[int], m: int) -> int:
#     """binary search + divide and conquer: T(N) = (T(N/2) + T(N/2)) * logN = 2logNT(N/2), O(N*(logN)^(logN))
#     """
#     self.memo, self.nums = {}, nums
#     self.recursive(0, len(nums), m)
#     return self.memo[(0, len(nums), m)]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0], 1),
    ([1], 1),
    ([2,1,2], 1),
    ([2,1,2], 2),
    ([2,1,5,6,2,3], 2),
    ([2,1,5,6,2,3], 3),
    ([2,3,1,2,4,3], 5),
    ([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3], 5),
  ]
  rslts = [solver.splitArray(nums, m) for nums, m in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")