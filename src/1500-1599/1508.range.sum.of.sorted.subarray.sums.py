from typing import List

class Solution:
  def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
    # TC: O(N^2) naive solution
    # TC: O(NlogS), S = sum(nums), binary search
    # n = len(nums)
    # p: prefix sum of nums
    p = [0] * (n + 1)
    for i in range(n):
      p[i + 1] = p[i] + nums[i]
    # q: prefix sum of prefix sum of nums, e.g., prefix sum of p
    q = [0] * (n + 1)
    for i in range(n):
      q[i + 1] = q[i] + p[i + 1]
    # count num of partial sums <= s, O(N)
    def count(s):
      ans, i = 0, 0
      for j in range(1, n + 1):
        while p[j] - p[i] > s:
          i += 1
        ans += j - i
      return ans
    # binary saerch, find the k-th partial sum s, O(NlogS)
    def getKth(k):
      l, r = 0, p[n]
      while l < r:
        m = l + (r - l) // 2
        if count(m) >= k:
          r = m
        else:
          l = m + 1
      return l
    # sum of partials sums with index <= k, O(N)
    def qpsum(k):
      ans, i, s = 0, 0, getKth(k)
      for j in range(1, n + 1):
        while p[j] - p[i] > s:
          i += 1
        # sum of p[j] - p[i], p[j] - p[i + 1], .., p[j] - p[j - 1]
        #  = p[j] * (j - i) - sum(p[i:j]) = p[j] * (j - i) - (q[j] - q[i - 1])
        ans += p[j] * (j - i) - (q[j] - (q[i - 1] if i else 0))
      # (count(s) - k) * s in case of duplicated s in partials sum, e.g., k-th, k+1-th, k+2-th partial sum all == s
      ans -= (count(s) - k) * s
      return ans
    return (qpsum(right) - qpsum(left - 1)) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4], 4, 2, 3),
    ([1,2,3,4], 4, 2, 4),
    ([1,2,3,4], 4, 2, 5),
    ([1,2,3,4], 4, 3, 4),
    ([1,2,3,4], 4, 1, 8),
  ]
  rslts = [solver.rangeSum(nums, n, left, right) for nums, n, left, right in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
