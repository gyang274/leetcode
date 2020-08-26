from typing import List
from collections import Counter
from itertools import accumulate

class Solution:
  def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
    # x: accumulated count of character's frequency
    x = list(accumulate(map(Counter, s), initial=Counter()))
    # rearrangable implies num of replace to make palindrome = (num of odds - ((j - i + 1) & 1) + 1) // 2
    ans, memo = [], {}
    for i, j, k in queries:
      if (i, j) not in memo:
        m, d = 0, x[j + 1] - x[i]
        for u in d:
          m += d[u] & 1
        m -= (j - i + 1) & 1
        memo[(i, j)] = (m + 1) // 2
      ans.append(memo[(i, j)] <= k)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcda", [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]),
  ]
  rslts = [solver.canMakePaliQueries(s, queries) for s, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
