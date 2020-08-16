from typing import List

class Solution:
  def mctFromLeafValues(self, arr: List[int]) -> int:
    # stack, TC: O(N), SC: O(N).
    # note: this is a stack question, not binary tree.
    # construct the min cost tree is equivalent as removing elements of array A until one,
    # where the cost of removing an element A[i] is A[i] * min(A[i - 1], A[i + 1])
    # stack: keep a stack of descreasing elements seen
    stack, cost = [float('inf')], 0
    for x in arr:
      while stack and stack[-1] <= x:
        m = stack.pop()
        cost += m * min(stack[-1], x)
      stack.append(x)
    while len(stack) > 2:
      cost += stack.pop() * stack[-1]
    return cost

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [2,3,1,1,4],
  ]
  rslts = [solver.mctFromLeafValues(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
