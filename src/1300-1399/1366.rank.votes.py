from typing import List
from collections import defaultdict

class Solution:
  def rankTeams(self, votes: List[str]) -> str:
    m, n = len(votes), len(votes[0])
    d = defaultdict(lambda: [0] * n)
    for vote in votes:
      for i in range(n):
        d[vote[i]][i] -= 1
    r = sorted([(d[k], k) for k in d])
    return ''.join([x[1] for x in r])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["ABC","ACB","ABC","ACB","ACB"],
  ]
  rslts = [solver.rankTeams(votes) for votes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
