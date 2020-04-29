from typing import List

class Solution:
  def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    n = len(nums)
    # lk[i]: sum of subarray [i - k, i), max subarray of k on left of [i, i + k), and smallest index achieved such max
    lk = [[0, 0, -1] for _ in range(n)]
    # init lk
    lk[k] = [sum(nums[:k]), sum(nums[:k]), 0]
    for i in range(k + 1, n - 2 * k + 1):
      lk[i][0] = lk[i - 1][0] + nums[i - 1] - nums[i - 1 - k]
      lk[i][1:] = [lk[i][0], i - k] if lk[i][0] > lk[i - 1][1] else lk[i - 1][1:]
    # rk[i]: sum of subarray [i + k, i), max subarray of k on right of [i, i + k), and smallest index achieved such max
    rk = [[0, 0, -1] for _ in range(n)]
    # init rk
    rk[n - k] = [sum(nums[(n - k):]), sum(nums[(n - k):]), n - k]
    for i in range(n - k - 1, 2 * k - 1, -1):
      rk[i][0] = rk[i + 1][0] + nums[i] - nums[i + k]
      rk[i][1:] = [rk[i][0], i] if rk[i][0] >= rk[i + 1][1] else rk[i + 1][1:]
    # maximize lk[i][1] + nums[i:(i + k)] + rk[i + k][1]
    s = sum(nums[k:(k + k)])
    xmax = lk[k][1] + s + rk[k + k][1]
    imax = [lk[k][2], k, rk[k + k][2]]
    for i in range(k + 1, n - 2 * k + 1):
      s += nums[i + k - 1] - nums[i - 1]
      x = lk[i][1] + s + rk[i + k][1]
      if x > xmax:
        xmax, imax = x, [lk[i][2], i, rk[i + k][2]]
    return imax

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,1,2,6,7,5,1], 2),
    ([1,2,1,2,1,2,1,2,1], 2),
  ]
  rslts = [solver.maxSumOfThreeSubarrays(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
