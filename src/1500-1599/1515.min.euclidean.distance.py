from typing import List

class Solution:
  def dist(self, p0, p1):
    return ((p0[0] - p1[0]) ** 2 + (p0[1] - p1[1]) ** 2) ** 0.5
  def getMinDistSum(self, positions: List[List[int]]) -> float:
    # Geometric Median, Weiszfeld's algorithm, iteratively re-weighted least squares.
    # init
    P = positions
    q = list(map(lambda x: sum(x) / len(x), zip(*P)))
    D = list(map(lambda p: self.dist(p, q), P))
    qs = sum(D)
    t, T = float('inf'), 10 ** -10
    while t >= T:
      # iterative
      W = [(1 / d if d else 10 ** 10) for d in D]
      r = (sum(p[0] * w for p, w in zip(P, W)) / sum(W), sum(p[1] * w for p, w in zip(P, W)) / sum(W))
      D = list(map(lambda p: self.dist(p, r), P))
      rs = sum(D)
      t = qs - rs
      q, qs = r, rs
    return qs

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[1,1]],
    [[1,1],[0,0],[2,0]],
    [[0,1],[1,0],[1,2],[2,1],[1,1]],
    [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]],
  ]
  rslts = [solver.getMinDistSum(positions) for positions in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
