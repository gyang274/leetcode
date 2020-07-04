from typing import List
from collections import deque

class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    i, j, n, stack = 0, 0, len(pushed), []
    while i < n:
      stack.append(pushed[i])
      i += 1
      while stack and stack[-1] == popped[j]:
        stack.pop()
        j += 1 
    return j == n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5], [4,5,3,2,1]),
    ([1,2,3,4,5], [4,3,5,1,2]),
  ]
  rslts = [solver.validateStackSequences(pushed, popped) for pushed, popped in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
