from typing import List

class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    """O(N^2), amortized O(1) for identifying k, s.t. argmax_{k}(nums[k] < nums[i] + nums[j]).
    """
    n, count = len(nums), 0
    nums.sort()
    for i in range(n - 2):
      if nums[i] <= 0:
        continue
      k = i + 2
      for j in range(i + 1, n - 1):
        while k < n and nums[k] < nums[i] + nums[j]:
          k += 1
        count += k - j - 1
        if k == n:
          count += (((n - 1) - (j + 1)) + 1) * ((n - 1) - (j + 1)) // 2
          break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,2,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.triangleNumber(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")