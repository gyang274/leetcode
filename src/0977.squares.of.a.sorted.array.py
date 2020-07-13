from typing import List

class Solution:
  def sortedSquares(self, A: List[int]) -> List[int]:
    stack, ans = [], []
    for x in A:
      if x < 0:
        stack.append(x * x)
      else:
        s = x * x
        while stack and stack[-1] < s:
          ans.append(stack.pop())
        ans.append(s)
    while stack:
      ans.append(stack.pop())
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [-4,-1,0,3,5],
    [-8,-5,2,3,5],
  ]
  rslts = [solver.sortedSquares(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
