from typing import List

class Solution:
  def minPatches(self, nums: List[int], n: int) -> int:
    """O(M+logN), greedy algorithm.
      Key: For an array that covers [1, miss), add an num x can extend the cover to [1, x + miss),
        so expand [1, miss) each iteration to [1, min(nums[i], miss) + miss) each iteration.
    """
    # miss: upper bound current nums[0..i] can cover
    i, counter, miss = 0, 0, 1
    while miss < n + 1:
      if i < len(nums) and nums[i] <= miss:
        # patch next from nums
        miss += nums[i]
        i += 1
      else:
        # patch next with miss
        miss += miss
        counter += 1
    return counter

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,5,10], 20),
  ]
  rslts = [solver.minPatches(nums, n) for nums, n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")