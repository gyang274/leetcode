from typing import List

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    """O(n): hashmap keyed by consecutive sequence boundaries, update boundary when go through.
      upper: upper bound -> length
      lower: lower bound -> length
      paired through upper - lower = length, all lower + 1, ..., upper - 1 are seen from list.
    """
    # if seen x, x + 1, x + 2 then keyed by lower[x - 1] = 3, upper[x + 3] = 3
    lower, upper, seen = {}, {}, set([])
    for x in nums:
      if x not in seen:
        if x in upper and x in lower:
          # seen (x - 1) and (x + 1) before, merge (x - n, x - 1) and (x + 1, x + m)
          n = upper.pop(x)
          m = lower.pop(x)
          lower[x - n - 1] = n + m + 1
          upper[x + m + 1] = n + m + 1
        elif x in upper:
          # see (x - 1) before, extend (x - n, x - 1) to (x - n, x)
          n = upper.pop(x)
          upper[x + 1] = n + 1
          lower[x - n - 1] = n + 1
        elif x in lower:
          m = lower.pop(x)
          lower[x - 1] = m + 1
          upper[x + m + 1] = m + 1
        else:
          upper[x + 1] = 1
          lower[x - 1] = 1
      seen.add(x)
    consec = 0
    for k, v in upper.items():
      consec = max(consec, v)
    return consec

class Solution:
  def longestConsecutive(self, nums: List[int]) -> int:
    """Hashset
    """
    consec, nums = 0, set(nums)
    for x in nums:
      if x - 1 not in nums:
        n, s = 1, x
        while s + 1 in nums:
          n += 1
          s += 1
        consec = max(consec, n)
    return consec


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    # [4, 42, 1, 22, 3, 87, 2], 
    [-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7],
  ]
  rslts = [solver.longestConsecutive(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
        