from typing import List

class Solution:
  def findPairs(self, nums: List[int], k: int) -> int:
    # hashset
    if k < 0:
      return 0
    if k == 0:
      seen1, seen2, pairs = set([]), set([]), 0
      for x in nums:
        if x not in seen1:
          seen1.add(x)
        elif x not in seen2:
          pairs += 1
          seen2.add(x)
    else:
      seen, pairs = set([]), 0
      for x in nums:
        if x not in seen:
          if x + k in seen:
            pairs += 1
          if x - k in seen:
            pairs += 1
          seen.add(x)
    return pairs

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([3,1,2,1,4], 0),
    ([3,1,2,1,4], 1),
    ([3,1,2,1,4], 2),
  ]
  rslts = [solver.findPairs(nums, k) for nums, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")