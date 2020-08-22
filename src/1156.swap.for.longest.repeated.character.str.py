from collections import Counter
from itertools import groupby

class Solution:
  def maxRepOpt1(self, text: str) -> int:
    # TC: O(N), SC: O(N)
    # get the group's key and length first, e.g. 'aaabaaa' -> [[a , 3], [b, 1], [a, 3]
    A = [[x, len(list(g))] for x, g in groupby(text)]
    # generate a count dict for easy look up e.g. 'aaabaaa' -> {a: 6, b: 1}
    count = Counter(text)
    # only extend 1 more, use min here to avoid the case that there's no extra char to extend
    ans = max(min(k + 1, count[x]) for x, k in A)
    # merge 2 groups together
    for i in range(1, len(A) - 1):
      # if both sides have the same char and are separated by only 1 char
      if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
        # min here serves the same purpose
        ans = max(ans, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i + 1][0]]))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aabbabbaaabb",
  ]
  rslts = [solver.maxRepOpt1(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
