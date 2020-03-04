from typing import List

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    """O(N^2): maintain a LIS for each item and update for each item after via dynamic programming.
      dp[i] = max(dp[j]) + 1, where 0 <= j < i and nums[i] > nums[j].
    """
    n = len(nums)
    if n == 0:
      return 0
    dp = [1] * n
    for i in range(n):
      for j in range(i):
        if nums[i] > nums[j]:
          dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

class Solution:
  def lengthOfLIS(self, nums: List[int]) -> int:
    """O(NlogN): https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithm
      modified so that all array indexed from 0.
    """
    n = len(nums)
    if n == 0:
      return 0
    # Array M and P, indexed from 0
    M, P = [None] * n, [None] * n
    # Binary search for the largest positive j <= L, such that X[M[j]] < X[i]
    L = 0
    for i in range(n):
      l, r = 0, L
      while l < r:
        m = l + (r - l) // 2
        if nums[M[m]] < nums[i]:
          l = m + 1
        else:
          r = m
      # After searching, l is the length of the longest prefix of X[i], 
      # e.g., l is length of LIS ended with X[i] without X[i] itself so length is l + 1
      # The predecessor of X[i] is the last index of the subsequence of length l, e.g., index l -1
      if l > 0:
        P[i] = M[l - 1]
      M[l] = i
      # If we found a subsequence longer than any we've found yet, update L
      L = max(L, l + 1)
      # # Reconstruct the longest increasing subsequence
      # S = [0] * L
      # k = M[L - 1]
      # for j in range(L - 1, -1, -1):
      #   S[j] = nums[k]
      #   k = P[k]
      # print(f"{i=}, {nums[i]=}, {l=}, {M=}, {P=}, {L=}, {S=}")
    return L

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    [1],
    [1,2],
    [10,9,2,5,3,7,101,18],
    [0,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15],
  ]
  rslts = [solver.lengthOfLIS(nums) for nums in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")