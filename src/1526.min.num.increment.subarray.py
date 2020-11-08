from typing import List

class Solution:
  def minNumberOperations(self, target: List[int]) -> int:
    # TC: O(N), SC: O(1), stack
    #  keep a stack of increasing nums, settle whenever see a decrease
    stack, count = [], 0
    for x in target:
      m = 0
      while stack and stack[-1] >= x:
        m = max(m, stack.pop() - x)
      count += m
      stack.append(x)
    count += stack[-1]
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,1,5,4,2],
    [1,9,4,5,6,3,8,7,2],
  ]
  rslts = [solver.minNumberOperations(target) for target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
