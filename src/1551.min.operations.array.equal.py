class Solution:
  def minOperations(self, n: int) -> int:
    return (n - 1) * (n + 1) // 4 if n & 1 else n * n // 4