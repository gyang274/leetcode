from functools import lru_cache

class Solution:
  @lru_cache(None)
  def generateArray(self):
    M = 100
    A = [0] * (M + 1)
    A[1] = 1
    for i in range(2, M + 1):
      A[i] = A[i // 2]
      if i & 1:
        A[i] += A[i // 2 + 1]
    for i in range(2, M + 1):
      A[i] = max(A[i], A[i - 1])
    return A    
  def getMaximumGenerated(self, n: int) -> int:
    return self.generateArray()[n]
