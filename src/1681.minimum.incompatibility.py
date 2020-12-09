from collections import Counter
from functools import lru_cache

class Solution:
  def minimumIncompatibility(self, nums: List[int], k: int) -> int:
    # dp + bitmask, TC: O(N * 2^N, 3^N)
    # dp[mask] as the min incompatibility of subset of nums with mask 1s taken
    # dp[mask] = min(dp[submask1] + dp[submask2]) over all submask1 and submask2
    # TC: O(3^N) iterates all submasks https://cp-algorithms.com/algebra/all-submasks.html
    n, m = len(nums), len(nums) // k
    if m == 1:
      return 0
    if max(Counter(nums).values()) > k:
      return -1
    # hamming weight
    def ones(x):
      count = 0
      while x:
        x &= x - 1
        count += 1
      return count
    # basic cases: hash of all mask with size n // k
    @lru_cache(None)
    def recursive(mask):
      if ones(mask) == m:
        # calculate the incompatibility directly
        xs = [nums[i] for i, b in enumerate(bin(mask)[2:].zfill(n)) if b == '1']
        return max(xs) - min(xs) if len(set(xs)) == len(xs) else float('inf')
      else:
        ans, submask = float('inf'), (mask - 1) & mask
        while submask:
          if ones(submask) % m == 0:
            ans = min(ans, recursive(submask) + recursive(mask - submask))
          submask = (submask - 1) & mask
        return ans
    return recursive((1 << n) - 1)

class Solution:
  def minimumIncompatibility(self, nums, k):
    n = len(nums)
    if k == n:
      return 0
    dp = [[float("inf")] * n for _ in range(1<<n)] 
    nums.sort()
    for i in range(n):
      dp[1 << i][i] = 0
    for mask in range(1<<n):
      n_z_bits = [len(bin(mask)) - p - 1 for p, c in enumerate(bin(mask)) if c == "1"]
      if len(n_z_bits) % (n//k) == 1:
        for j, l in permutations(n_z_bits, 2):
          dp[mask][l] = min(dp[mask][l], dp[mask^(1<<l)][j])
        else:
          for j, l in combinations(n_z_bits, 2):
            if nums[j] != nums[l]:
              dp[mask][l] = min(dp[mask][l], dp[mask^(1<<l)][j] + nums[j] - nums[l])              
    return min(dp[-1]) if min(dp[-1]) != float("inf") else -1