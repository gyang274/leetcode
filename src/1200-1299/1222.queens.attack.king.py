from typing import List

class Solution:
  def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
    # a king can be attacked by at most 8 queens, one from each direction
    # bfs, explore from the king until met 1st queen on each direction, instead explore each queen
    (ki, kj), queens, ans = king, set(map(tuple, queens)), []
    for di, dj in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
      m = 1
      while True:
        qi, qj = ki + di * m, kj + dj * m
        if not (0 <= qi < 8 and 0 <= qj < 8):
          break
        if (qi, qj) in queens:
          ans.append((qi, qj))
          break
        m += 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], [0,0]),
    ([[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], [3,3]),
    ([[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], [3,4]),
  ]
  rslts = [solver.queensAttacktheKing(queens, king) for queens, king in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
