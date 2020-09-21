class Solution:
  def findNumbers(self, nums: List[int]) -> int:
    return sum(map(lambda x: (len(str(x)) & 1) ^ 1, nums))
