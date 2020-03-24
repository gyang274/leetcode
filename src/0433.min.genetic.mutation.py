from typing import List
from collections import defaultdict

class Solution:
  def _distance(self, str1, str2):
    # TODO: use bit operation for distance, say view ATGC as 00, 01, 10, 11, so 8 character -> 16 bit 
    dist = 0
    for x, y in zip(str1, str2):
      if not x == y:
        dist += 1
    return dist
  def minMutation(self, start: str, end: str, bank: List[str]) -> int:
    """BFS
    """
    # base cases
    if end not in bank:
      return -1
    if start not in bank:
      bank.append(start)
    # mutations
    n = len(bank)
    mutation = defaultdict(set)
    for i in range(n):
      for j in range(i, n):
        if self._distance(bank[i], bank[j]) == 1:
          mutation[bank[i]].add(bank[j])
          mutation[bank[j]].add(bank[i])
    # BFS
    dist, stack, bound, visit = 0, set([start]), set([]), set([start])
    while stack:
      dist += 1
      while stack:
        s = stack.pop()
        for e in mutation[s]:
          if e == end:
            return dist
          if e not in visit:
            bound.add(e)
            visit.add(e)
      stack, bound = bound, set([])
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("AACCGGTT", "AACCGGTA", ["AACCGGTA"]),
    ("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]),
    ("AAAAACCC", "AACCCCCC", ["AAAACCCC", "AAACCCCC", "AACCCCCC"]),

  ]
  rslts = [solver.minMutation(start, end, bank) for start, end, bank in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
