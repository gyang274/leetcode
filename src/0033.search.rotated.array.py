from typing import List


class Solution:
  def search(self, nums: List[int], target: int) -> int:
    n = len(nums)
    i = 0
    j = n - 1
    while i < j:
      k = (i + j) // 2

    return -1



if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([4,5,6,7,0,1,2],  0),
    ([4,5,6,7,0,1,2], -1),
  ]
  rslts = [solver.search(nums, target) for nums, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
