from typing import List

class Solution:
  def findMinMoves(self, machines: List[int]) -> int:
    mn = len(machines)
    if mn < 2:
      return 0
    ms = sum(machines)
    if ms % mn:
      return -1
    ma = ms // mn
    mr, ops = 0, 0
    for mx in machines:
      md = mx - ma
      if md > 0:
        ops = max(ops, md)
      mr += md
      ops = max(ops, abs(mr))
    return ops

class Solution:
  def findMinMoves(self, machines: List[int]) -> int:
    mn = len(machines)
    if mn < 2:
      return 0
    ms = sum(machines)
    if ms % mn:
      return -1
    ma = ms // mn
    mr, ops = 0, 0
    for mx in machines:
      mr += mx - ma
      ops = max(ops, abs(mr), mx - ma)
    return ops

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0,3,0],
    [3,0,3],
    [2,3,1,0,4],
    [3,2,1,1,4],
    [20,6,16,2,10,18,9,7,13,4,10,16,18,2,13,16,14,19,17,10],
  ]
  rslts = [solver.findMinMoves(machines) for machines in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")    