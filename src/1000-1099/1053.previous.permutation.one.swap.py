from typing import List

class Solution:
  def prevPermOpt1(self, A: List[int]) -> List[int]:
    n = len(A)
    i, stack = n - 2, [n - 1, ]
    while i >= 0:
      if A[i] <= A[i + 1]:
        stack.append(i)
        i -= 1
      else:
        break
    if i >= 0:
      j = stack.pop()
      while stack and A[j] < A[stack[-1]] and A[i] > A[stack[-1]]:
        j = stack.pop()
      A[i], A[j] = A[j], A[i]
    return A

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [3,2,1],
    [1,1,4],
    [3,1,1,3],
    [3,1,2,4],
    [3,1,1,4],
    [3,1,3,4],
    [1,9,4,6,7],
  ]
  rslts = [solver.prevPermOpt1(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
