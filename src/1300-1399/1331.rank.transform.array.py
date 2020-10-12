from typing import List

class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    n, x = len(arr), sorted([v, i, 1] for i, v in enumerate(arr))
    for k in range(1, n):
      x[k][2] = x[k - 1][2] + (1 if x[k][0] > x[k - 1][0] else 0)
    return [vir[2] for vir in sorted(x, key=lambda vir: vir[1])]

class Solution:
  def arrayRankTransform(self, arr: List[int]) -> List[int]:
    return list(map({x: i + 1 for i, x in enumerate(sorted(set(arr)))}.get, arr))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
    [3,2,1,0,4],
  ]
  rslts = [solver.arrayRankTransform(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
