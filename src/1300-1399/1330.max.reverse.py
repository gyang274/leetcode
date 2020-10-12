from typing import List

class Solution:
  def maxValueAfterReverse(self, nums: List[int]) -> int:
    # TC: O(N), SC: O(1), one pass
    # 1. reverse A[0] -- A[i], improve abs(A[0] - A[i+1]) - abs(A[i] - A[i+1])
    # 2. reverse A[i+1] -- A[n-1], improve abs(A[n-1] - A[i]) - abs(A[i] - A[i+1])
    # 3. reverse A[i+1] -- A[j], improve abs(A[i] - A[j]) + abs(A[i+1] - A[j+1]) - abs(A[i] - A[i+1]) - abs(A[j]-A[j+1])
    #   let A[i], A[i+1], A[j], A[j+1] be u, v, x, y and say u = max(u, v, x, y) will always be +u after disclose abs(),
    #   and y = min(u, v, x, y) will always be -y after disclose abs(), so they wil cancel out, and the improve will be
    #   2v - 2x if v >= x or 2x - 2v otherwise, e.g., (max(min(A[i], A[i+1])) - min(max(A[j], A[j+1]))) * 2
    ans, imp1, min2, max2 = 0, 0, float('inf'), -float('inf')
    for x, y in zip(nums[:-1], nums[1:]):
      ans += abs(x - y)
      imp1 = max(imp1, abs(nums[0] - y) - abs(x - y), abs(nums[-1] - x) - abs(x - y))
      min2, max2 = min(min2, max(x, y)), max(max2, min(x, y))
    return ans + max(imp1, (max2 - min2) * 2)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,5,4],
    [2,4,9,24,2,1,10],
  ]
  rslts = [solver.maxValueAfterReverse(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
