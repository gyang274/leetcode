from typing import List
from collections import defaultdict

class Solution:
  def splitArray(self, nums: List[int]) -> bool:
    """O(N^2) or O(N) on average, i, k two pointers from init and ende, and j scan in-between i and k.
      O(N^3) when [1,0,...,0,1] all 0, and O(NlogN) when elements are all positive using binary search over j.
    """
    n = len(nums)
    if n < 7:
      return False
    # d: key -> set of i, k, e.g., key == sum(nums[:i]) == sum(nums[(k+1):])
    d = defaultdict(lambda: dict(i = [], k = []))
    # si, sk: cumulative sum from left and right
    si, sk = nums.copy(), nums.copy()
    for i in range(1, n):
      si[i] += si[i - 1]
      d[si[i - 1]]["i"].append(i)
    for k in range(n - 2, -1, -1):
      sk[k] += sk[k + 1]
      d[sk[k + 1]]["k"].append(k)
    # j, s.t. si[j - 1] - si[i] == sk[j + 1] - sk[k]
    for s in d:
      for i in d[s]["i"]:
        for k in d[s]["k"]:
          if k - i > 3:
            for j in range(i + 2, k - 1):
              if si[j - 1] - si[i] == s and sk[j + 1] - sk[k] == s:
                return True
          else:
            break
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,2,1,2,1,2,1],
  ]
  rslts = [solver.splitArray(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
      