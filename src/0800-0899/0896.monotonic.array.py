class Solution:
  def isMonotonic(self, A: List[int]) -> bool:
    return all(x <= y for x, y in zip(A[:-1], A[1:])) or all(x >= y for x, y in zip(A[:-1], A[1:]))

class Solution:
  def isMonotonic(self, A: List[int]) -> bool:
    increasing = decreasing = True
    for i in range(len(A) - 1):
      if A[i] < A[i + 1]:
        decreasing = False
      if A[i] > A[i + 1]:
        increasing = False
    return increasing or decreasing
