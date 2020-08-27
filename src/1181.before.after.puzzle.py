from typing import List
from collections import defaultdict
from itertools import product

class Solution:
  def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
    phrases = list(map(lambda x: x.split(), phrases))
    # d: word -> (phase-word-as-last, phase-word-as-first)
    d = defaultdict(lambda: [set(), set()])
    for i, x in enumerate(phrases):
      d[x[-1]][0].add(i)
      d[x[0]][-1].add(i)
    # construct the before and after puzzles
    ans = set()
    for word in d:
      for i, j in product(*d[word]):
        if not i == j:
          ans.add(' '.join(phrases[i] + phrases[j][1:]))
    return sorted(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["a","b","a"],
    ["writing code","code rocks"],
    ["mission statement","a quick bite to eat","a chip off the old block","chocolate bar","mission impossible","a man on a mission","block party","eat my words","bar of soap"],
  ]
  rslts = [solver.beforeAndAfterPuzzles(phrases) for phrases in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
