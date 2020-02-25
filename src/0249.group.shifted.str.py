from typing import List
from collections import defaultdict

class Solution:
  def groupStrings(self, strings: List[str]) -> List[List[str]]:
    """HashTable key by adjacent character difference.
    """
    group = defaultdict(list)
    for s in strings:
      if len(s) == 0:
        group[0].append(s)
      elif len(s) == 1:
        group[()].append(s)
      else:
        x, k = s[0], []
        for y in s[1:]:
          k.append((ord(y) - ord(x)) % 26)
          x = y
        group[tuple(k)].append(s)
    return group.values()

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z", ""],
  ]
  rslts = [solver.groupStrings(strings) for strings in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")