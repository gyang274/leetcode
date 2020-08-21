from typing import List
from collections import defaultdict, Counter

import itertools

class Solution:
  def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    visit = sorted((t, u, w) for u, t, w in zip(username, timestamp, website))
    # d: user -> (1-sequence, 2-sequence, 3-sequence)
    d = defaultdict(lambda: [set(), set(), set()])
    for t, u, w in visit:
      d[u][2] |= {x + '-' + w for x in d[u][1]}
      d[u][1] |= {x + '-' + w for x in d[u][0]}
      d[u][0] |= {w}
    # s: 3-sequences -> counter of users visited this 3-sequence
    s = Counter(itertools.chain.from_iterable(d[u][2] for u in d))
    return sorted((-s[k], k) for k in s)[0][1].split('-')

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["u1","u1","u1","u2","u2","u2"], [1,2,3,4,5,6], ["a","b","c","a","b","a"]),
    (["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"]),
  ]
  rslts = [solver.mostVisitedPattern(username, timestamp, website) for username, timestamp, website in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
