from typing import List

class Solution:
  def minNumberOfSemesters(self, n: int, dependencies: List[List[int]], k: int) -> int:
    # TC: O(2^n * 2^k), bitmask
    # prep[i]: bitmask of i-th course (0-indexed) prerequisite
    prep = [0] * n
    for i, j in dependencies:
      prep[j - 1] |= 1 << (i - 1)
    # ones: number of 1s in a bitmask
    ones = [0] * (1 << n)
    for x in range(1 << n):
      ones[x] = bin(x).count('1')
    # dynamic programming
    # dp[x] is the min days to complete all courses reprsented by bitmask x, which is upper bounded by n
    dp = [n] * (1 << n)
    # init
    dp[0] = 0
    # main
    #  loop through bitmask
    for x in range(1 << n):
      # x is the bitmask of all courses taken
      if dp[x] == n:
        continue
      # y is the bitmask of all courses can be taken after x
      y = 0
      for i in range(n):
        # all prerequisite of course i satisified
        if x & prep[i] == prep[i]:
          y |= 1 << i
      # and delete all courses taken, no re-taken
      y &= ~x
      # enumerate over all subsets of a bit representation
      z = y
      while z:
        # enumerate all bit 1s combinations of y, where num 1s <= k
        if ones[z] <= k:
          # this combinations has less than k courses that all available to take, so take them all in one semester.
          dp[x | z] = min(dp[x | z], dp[x] + 1)
        z = (z - 1) & y
    return dp[-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (4, [[2,1],[3,1],[1,4]], 2),
    (5, [[2,1],[3,1],[4,1],[1,5]], 2),
  ]
  rslts = [solver.minNumberOfSemesters(n, dependencies, k) for n, dependencies, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
