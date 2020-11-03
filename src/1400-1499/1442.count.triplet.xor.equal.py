from typing import List
from itertools import accumulate

class Solution:
  def countTriplets(self, nums: List[int]) -> int:
    # TC: O(N^3), SC: O(1), prefix + brute force
    n, x = len(nums), list(accumulate(nums, lambda x, y: x ^ y, initial=0))
    count = 0
    for i in range(1, n + 1 - 1):
      for j in range(i + 1, n + 1):
        for k in range(j + 0, n + 1):
          if x[i - 1] ^ x[j - 1] == x[j - 1] ^ x[k]:
            count += 1
    return count

class Solution:
  def countTriplets(self, nums: List[int]) -> int:
    # TC: O(N), SC: O(1), prefix + math
    n = len(nums)
    # a == b => a^a = a^b => a^b = 0
    # nums[i] ^ nums[i+1] ^ .. ^ nums[k] = 0
    # prefix: x[i] = x[k + 1], any j within i <j <= k works
    x, seen, count = 0, {0: (1, 0)}, 0
    for i in range(n):
      x ^= nums[i]
      freq, dist = seen.get(x, (0, 0))
      count += freq * i - dist
      seen[x] = (freq + 1, dist + i + 1)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3],
    [1,1,1,1,1],
    [1,3,5,7,9],
    [2,3,1,6,7],
    [7,11,12,9,5,2,7,17,22],
  ]
  rslts = [solver.countTriplets(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
