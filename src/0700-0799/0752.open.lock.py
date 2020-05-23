from typing import List
from collections import deque

class Solution:
  def openLock(self, deadends: List[str], target: str) -> int:
    dead = set(deadends)
    seen, queue = {'0000'}, deque([('0000', 0)])
    while queue:
      node, dist = queue.popleft()
      if node == target:
        return dist
      if node not in dead:
        for i in range(4):
          for j in (-1, 1):
            nuxt = node[:i] + str((int(node[i]) + j) % 10) + node[(i + 1):]
            if nuxt not in seen:
              seen.add(nuxt)
              queue.append((nuxt, dist + 1))
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["0000"], "8888"),
    (["8888"], "0007"),
    (["8888"], "0009"),
    (["0201","0101","0102","1212","2002"], "0202"),
    (["8887","8889","8878","8898","8788","8988","7888","9888"], "8888"),
  ]
  rslts = [solver.openLock(deadends, target) for deadends, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
