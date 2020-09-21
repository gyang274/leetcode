from typing import List
from collections import deque

class Solution:
  def countSteppingNumbers(self, low: int, high: int) -> List[int]:
    q, ans = deque([x for x in range(10)]), set()
    while q:
      x = q.popleft()
      if low <= x <= high:
        ans.add(x)
      if x < high:
        d = x % 10
        if d == 0:
          q.append(x * 10 + 1)
        elif d == 9:
          q.append(x * 10 + 8)
        else:
          q.append(x * 10 + (d - 1))
          q.append(x * 10 + (d + 1))
    return sorted(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (0, 23), (23, 42), (42, 85),
  ]
  rslts = [solver.countSteppingNumbers(low, high) for low, high in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
