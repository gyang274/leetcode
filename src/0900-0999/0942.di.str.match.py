from typing import List
from collections import deque

class Solution:
  def diStringMatch(self, S: str) -> List[int]:
    x = deque(range(len(S) + 1))
    return [x.popleft() if s == "I" else x.pop() for s in S + "D"]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "III", "DDD", "IDID", "DIDI",
  ]
  rslts = [solver.diStringMatch(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
