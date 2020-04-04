from typing import List

import heapq

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    queue = []
    great = {}
    for x in nums2:
      while queue and x > queue[0]:
        great[heapq.heappop(queue)] = x
      heapq.heappush(queue, x)
    return [great.get(x, -1) for x in nums1]

class Solution:
  def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    stack = []
    great = {}
    for x in nums2:
      while stack and x > stack[-1]:
        great[stack.pop()] = x
      stack.append(x)
    return [great.get(x, -1) for x in nums1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([4,2], [1,2,3,4]),
    ([2,1,4], [1,3,4,2]),
  ]
  rslts = [solver.nextGreaterElement(nums1, nums2) for nums1, nums2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  