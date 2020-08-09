from typing import List

class Solution:
  def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
    # bfs
    queue, seen = [[r0, c0]], set([(r0, c0)])
    for x, y in queue:
      for dx, dy in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        r, c = x + dx, y + dy
        if 0 <= r < R and 0 <= c < C and (r, c) not in seen:
          seen.add((r, c))
          queue.append([r, c])
    return queue

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1,2,0,0),
    (2,2,0,1),
  ]
  rslts = [solver.allCellsDistOrder(R, C, r0, c0) for R, C, r0, c0 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
