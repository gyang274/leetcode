from typing import List
from itertools import zip_longest

class Solution:
  def printVertically(self, s: str) -> List[str]:
    s = s.split()
    n = max(map(len, s))
    s = list(map(lambda x: x + ' ' * (n - len(x)), s))
    return list(map(lambda x: ''.join(x).rstrip(), zip_longest(*s)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "ABC D EFGH I JKLMN",
  ]
  rslts = [solver.printVertically(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
