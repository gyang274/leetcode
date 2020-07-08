from typing import List

class Solution:
  def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
    d, q = {}, {}
    d[tuple(cells)] = 0
    q[0] = tuple(cells)
    for i in range(1, N + 1):
      cells = [0] + [(cells[i - 1] ^ cells[i + 1]) ^ 1 for i in range(1, len(cells) - 1)] + [0]
      k = tuple(cells)
      if k in d:
        return q[d[k] + (N - d[k]) % (i - d[k])]
      d[k] = i
      q[i] = k
    return cells

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0,1,0,1,1,0,0,1], 7),
    ([1,0,0,1,0,0,1,0], 1000000000),
  ]
  rslts = [solver.prisonAfterNDays(cells, N) for cells, N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
