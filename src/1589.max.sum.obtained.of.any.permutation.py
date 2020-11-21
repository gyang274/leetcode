from typing import List

class Solution:
  def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
    # TC: O(N) construct r + O(NlogN) sort, SC: O(N).
    n = len(nums)
    # r: num of times each index is used across all requests
    r = [0] * n
    for i, j in requests:
      r[i] += 1
      if j + 1 < n:
        r[j + 1] -= 1
    for i in range(1, n):
      r[i] += r[i - 1]
    return sum(x * y for x, y in zip(sorted(nums), sorted(r))) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5], [[1,3],[0,1]]),
    ([2,3,5,8,10], [[0,2],[1,3],[1,1]]),
  ]
  rslts = [solver.maxSumRangeQuery(nums, requests) for nums, requests in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
