from typing import List

class Solution:
  def findLengthOfShortestSubarray(self, nums: List[int]) -> int:
    n = len(nums)
    # longest sorted prefix (s)
    prefix = [0]
    for x in nums:
      if x >= prefix[-1]:
        prefix.append(x)
      else:
        break
    # longest sorted suffix (r)
    suffix = [float('inf')]
    for x in nums[::-1]:
      if x <= suffix[-1]:
        suffix.append(x)
      else:
        break
    suffix = suffix[::-1]
    # merge prefix + suffix
    i, np = 0, len(prefix)
    j, ns = 0, len(suffix)
    m = 0
    while i < np and j < ns:
      while suffix[j] < prefix[i]:
        j += 1
      m = max(m, i + ns - 1 - j)
      i += 1
    return max(0, n - m)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [1,2,3,7,4,2,3,5],
  ]
  rslts = [solver.findLengthOfShortestSubarray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
