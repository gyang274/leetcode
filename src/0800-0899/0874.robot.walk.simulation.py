from typing import List
from collections import defaultdict

class Solution:
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    # obstacles 
    rb, cb = defaultdict(set), defaultdict(set)
    for r, c in obstacles:
      rb[r].add(c)
      cb[c].add(r)
    # d: 0, 1, 2, 3, north, west, south, east
    d, i, j, s = 0, 0, 0, 0
    for x in commands:
      if x == -2:
        d = (d + 1) % 4
      elif x == -1:
        d = (d - 1) % 4
      else:
        if d == 0:
          if i in rb:
            for m in range(1, x + 1):
              if j + m in rb[i]:
                x = m - 1
                break
          j += x
        elif d == 1:
          if j in cb:
            for m in range(1, x + 1):
              if i - m in cb[j]:
                x = m - 1
                break
          i -= x
        elif d == 2:
          if i in rb:
            for m in range(1, x + 1):
              if j - m in rb[i]:
                x = m - 1
                break
          j -= x
        else:
          if j in cb:
            for m in range(1, x + 1):
              if i + m in cb[j]:
                x = m - 1
                break
          i += x
        s = max(s, i ** 2 + j ** 2)
    return s

class Solution:
  def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
    obstacleSet = set(map(tuple, obstacles))
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    x = y = d = 0
    ans = 0
    for cmd in commands:
      if cmd == -2:
        # left
        d = (d - 1) % 4
      elif cmd == -1:
        # right
        d = (d + 1) % 4
      else:
        for k in range(cmd):
          if (x + dx[d], y + dy[d]) not in obstacleSet:
            x += dx[d]
            y += dy[d]
        ans = max(ans, x * x + y * y)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([4,-1,3], []),
    ([4,-1,4,-2,4], [[2,4]]),
    ([-2,-1,8,9,6], [[-1,3],[0,1],[-1,5],[-2,-4],[5,4],[-2,-3],[5,-1],[1,-1],[5,5],[5,2]]),
  ]
  rslts = [solver.robotSim(commands, obstacles) for commands, obstacles in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
