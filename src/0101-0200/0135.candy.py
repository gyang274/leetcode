from typing import List

class Solution:
  def candy(self, ratings: List[int]) -> int:
    n = len(ratings)
    # view from left to right
    vl = [1 for _ in range(n)]
    for i in range(1, n):
      if ratings[i] > ratings[i - 1]:
        vl[i] += vl[i - 1]
    # view from right to left
    vr = [1 for _ in range(n)]
    for i in range(n - 2, -1, -1):
      if ratings[i] > ratings[i + 1]:
        vr[i] += vr[i + 1]
    # max(vl, vr) at each index
    vx = [max(il, ir) for il, ir in zip(vl, vr)]
    return sum(vx)

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [1],
    [1,0],
    [1,1],
    [1,2],
    [1,0,2],
    [1,2,2],
  ]
  rslts = [solver.candy(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  
