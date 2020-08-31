from typing import List
from collections import Counter

# import heapq

# class Solution:
#   def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
#     # divide into continuous subsequence 1,2,3,4,..
#     q = [(nums[0], 1)]
#     for x in nums[1:]:
#       y, k = heapq.heappop(q)
#       if x > y + 1:
#         if k < K:
#           return False
#         heapq.heappush(q, (x, 1))
#       elif x == y + 1:
#         heapq.heappush(q, (x, k + 1))
#       else:
#         heapq.heappush(q, (y, k))
#         heapq.heappush(q, (x, 1))
#     return all(k >= K for _, k in q)

class Solution:
  def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
    return len(nums) // max(Counter(nums).values()) >= K

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,2,3,3,4,4], 3),
    ([5,5,6,6,7,8,9], 4),
  ]
  rslts = [solver.canDivideIntoSubsequences(nums, K) for nums, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
