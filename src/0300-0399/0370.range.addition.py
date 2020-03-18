from typing import List

class Solution:
  def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
    """Key: make opearation at start and end + 1, accumulate sum after going through all updates, so 
      each position operated once, length of ende - start + 1 doesn't matter, O(n + k) instead of O(nk)
    """
    nums = [0] * length
    for init, ende, val in updates:
      nums[init] += val
      if ende < length - 1:
        nums[ende + 1] -= val
    for i in range(1, length):
      nums[i] += nums[i - 1]
    return nums

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (5, [[1,3,2],[2,4,3],[0,2,-2]]),
  ]
  rslts = [solver.getModifiedArray(length, updates) for length, updates in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")