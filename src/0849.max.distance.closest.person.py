from typing import List

class Solution:
  def maxDistToClosest(self, seats: List[int]) -> int:
    n = len(seats)
    l = [0] * n
    s = 0
    while seats[s] == 0:
      l[s] = n
      s += 1
    for i in range(s, n):
      if seats[i] == 0:
        l[i] = l[i - 1] + 1
    r = [0] * n
    s = n - 1
    while seats[s] == 0:
      r[s] = n
      s -= 1
    for i in range(s, -1, -1):
      if seats[i] == 0:
        r[i] = r[i + 1] + 1
    return max(min(l[i], r[i]) for i in range(n))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [1,0,0,0,1,0,1],
    [1,0,0,0],
  ]
  rslts = [solver.maxDistToClosest(seats) for seats in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
