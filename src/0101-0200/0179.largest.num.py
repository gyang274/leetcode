from typing import List

class Node:
  def __init__(self, x):
    self.val = x
  def __lt__(self, other):
    if isinstance(other, self.__class__):
      return self.val + other.val < other.val + self.val
class Solution:
  def largestNumber(self, nums: List[int]) -> str:
    """O(NlogN), customized comparator, concatenation is transitive, e.g., a `>` b means concat(a, b) > concat(b, a),
      if concat(a, b) > concat(b, a), and concat(b, c) > concat(c, a), then concat(a, c) > concat(c, a).
    """
    if len(nums) == 0:
      return ''
    if all([x == 0 for x in nums]):
      return '0'
    nums = [Node(str(x)) for x in nums]
    nums.sort(reverse = True)
    return ''.join([node.val for node in nums])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [0, 0],
    [10, 2],
    [121,12],
    [3,30,34,5,9],
    [824,938,1399,5607,6973,5703,9609,4398,8247],
  ]
  rslts = [solver.largestNumber(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")