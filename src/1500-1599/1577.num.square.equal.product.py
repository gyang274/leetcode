from typing import List
from collections import defaultdict

class Solution:
  def squareSplit(self, nums1, nums2):
    d1, d2 = defaultdict(lambda: 0), defaultdict(lambda: 0)
    for x in nums1:
      d1[x * x] += 1
    for i in range(len(nums2)):
      for j in range(i + 1, len(nums2)):
        d2[nums2[i] * nums2[j]] += 1
    return sum([d1[k] * d2[k] for k in d1])
  def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
    return self.squareSplit(nums1, nums2) + self.squareSplit(nums2, nums1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([2,3,1,1,4], [2,2,1,0,4,8,6]),
  ]
  rslts = [solver.numTriplets(nums1, nums2) for nums1, nums2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
