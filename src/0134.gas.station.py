from typing import List

class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    """math: if sum(extra) >= 0 guaranteed to have a travel solution, 
      view the list to be sublists separated by negative extra elemented,
      at least one of such sublist will accumulate enough extra to overcome one negative block, and induction.
      TC: O(n), SC: O(1) - extra can be in-place by using gas or cost.
    """
    extra = [x - y for x, y in zip(gas, cost)]
    if sum(extra) < 0:
      return -1
    index, xsum, ok = -1, 0, False
    for i, e in enumerate(extra):
      if not ok:
        # start with index i
        if e >= 0:
          index, xsum, ok = i, e, True
      else:
        # accumulate gas at each station
        xsum += e
        # meet a block (large negative), cann't start from earlier index
        if xsum < 0:
          index, xsum, ok = -1, 0, False  
    return index

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([2], [2]),
    ([2,3,4], [3,4,3]),
    ([5,8,2,8], [6,5,6,6]),
    ([1,2,3,4,5], [3,4,5,1,2]),
  ]
  rslts = [solver.canCompleteCircuit(gas, cost) for gas, cost in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  