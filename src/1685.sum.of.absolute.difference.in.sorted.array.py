class Solution:
  def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
    # TC: O(N), SC: O(1),
    # cursor start at 0 so all on right, moving cursor from left to right, update by O(1)
    s, c, n, ans = sum(nums), 0, len(nums), []
    for i, x in enumerate(nums):
      s = s - (n - 2 * i) * (x - c)
      c = x
      ans.append(s)
    return ans
