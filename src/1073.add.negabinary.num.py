from typing import List
from itertools import zip_longest

class Solution:
  def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
    # negabinary
    #  1: 0, 0, 1
    #  2: 1, 1, 0
    #  3: 1, 0, 1
    #  4: 1, 0, 0
    # =>
    # a   b   c   d
    #     e   f   g
    # ---------------
    #     k1  k2  x
    # k1' k2' x'
    ans = [(x or 0) + (y or 0) for x, y in zip_longest(reversed(arr1), reversed(arr2))]
    ans.append(0)
    ans.append(0)
    for i in range(len(ans) - 2):
      if ans[i] == 2:
        if ans[i + 1] > 0:
          ans[i + 1] -= 1
        else:
          ans[i + 1] += 1
          ans[i + 2] += 1
        ans[i] = 0
      elif ans[i] == 3:
        if ans[i + 1] > 0:
          ans[i + 1] -= 1
        else:
          ans[i + 1] += 1
          ans[i + 2] += 1
        ans[i] = 1
      elif ans[i] == 4:
        if ans[i + 1] > 1:
          ans[i + 1] -= 2
        else:
          ans[i + 2] += 1
        ans[i] = 0
    while ans and not ans[-1]:
      ans.pop()
    if not ans:
      return [0]
    return list(reversed(ans))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1], [1]),
    ([1], [1,1]),
    ([1], [1,1,1,1]),
    ([1,1], [1,1]),
    ([1,1,1,1,1], [1,0,1]),
  ]
  rslts = [solver.addNegabinary(arr1, arr2) for arr1, arr2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
