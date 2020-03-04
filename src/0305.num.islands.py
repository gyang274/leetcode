from typing import List

class Solution:
  def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    """maintain a list or dict of all existing islands boundaries, when a new land added:
      1) +1 islands, if not in any boundaries
      2) -(i - 1) islands, if in k boundaries, i >= 1
      TC: O(k^2), k is the number of positions
    """
    return None

class Solution:
  def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
    """Disjoint-Set: https://en.wikipedia.org/wiki/disjoint-set_data_structure
    """
    matrix = [[-1] * n for _ in range(m)]
    # disjoint set, init each operation/island root to itself, height 0
    # when two islands connected, pointing both to the smaller one
    root = [[i, 1] for i in range(len(positions))]
    # k: number of islands, islands: num of islands after each operations
    k, islands = 0, []
    # dxdy: surrounded positions
    dxdy = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for idx, (x, y) in enumerate(positions):
      # in case of duplicate operation on the same position
      if matrix[x][y] == -1:
        matrix[x][y] = idx
        # each operation can connect to up to 4 adjacent positions
        connected = set([])
        for dx, dy in dxdy:
          i, j = x + dx, y + dy
          # new island (x, y) is connected to some existing island
          if 0<= i < m and 0 <= j < n and matrix[i][j] > -1:
            # add the root of existing island (index, disjoint-set height)
            r = matrix[i][j]
            while not root[r][0] == r:
              r = root[r][0]
            connected.add(root[r])
        # if more than one, connect them by pointing to the same root (root with highest height)
        if connected:
          # connected is at most 4, sort by larger height and smaller idx
          connected = sorted(list(connected), key=lambda r: (r[1], -r[0]), reverse=True)
          r, h = connected.pop()
          # point this operation to the root
          root[idx] = (r, 1)
          # update other island by pointing to the same root, and update height correspondingly.
          while connected:
            s, hs = connected.pop()
            root[s] = (r, hs)
            root[r] = (r, max(h, hs + 1))
            k -= 1
        else:
          # point this operation to the root as itself
          root[idx] = (idx, 1)
          k += 1
      else:
        # point this operation to the root as previous operation
        root[idx] = (matrix[x][y], 1)
      # update
      islands.append(k)
    return islands

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 3, [[0,0], [1,1], [2,2]]),
    (3, 3, [[0,0], [0,1], [1,1], [1,2], [2,2]]),
    (3, 3, [[0,0], [0,1], [1,2], [2,1], [2,2]]),
    (5, 5, [[0,0], [2,2], [4,4], [0,1], [1,2], [1,1], [4,2], [3,3], [3,4], [3,2]])
  ]
  rslts = [solver.numIslands2(m, n, positions) for m, n, positions in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")