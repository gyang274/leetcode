class Solution:
  def longestMountain(self, A: List[int]) -> int:
    n = len(A)
    l = [0] * n
    for i in range(1, n):
      if A[i] > A[i - 1]:
        l[i] = l[i - 1] + 1
    r = [0] * n
    for i in range(n - 2, -1, -1):
      if A[i] > A[i + 1]:
        r[i] = r[i + 1] + 1
    m = [l[i] + r[i] + 1 for i in range(n) if l[i] * r[i] > 0]
    return max(m) if m else 0