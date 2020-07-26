from typing import List

class Solution:
  def maxSumTwoNoOverlapUnit(self, A, L, M):
    N = len(A)
    # L on left
    AL = [0] * N
    AL[L - 1] = sum(A[:L])
    for i in range(L, N):
      AL[i] = AL[i - 1] + A[i] - A[i - L]
    # L max over left
    for i in range(L, N):
      AL[i] = max(AL[i], AL[i - 1])
    # M on right
    AM = [0] * N
    AM[N - M] = sum(A[(N - M):])
    for i in range(N - M - 1, -1, -1):
      AM[i] = AM[i + 1] + A[i] - A[i + M]
    # M max over right
    for i in range(N - 2, -1, -1):
      AM[i] = max(AM[i], AM[i + 1])
    # max of non overlap
    return max(AL[i] + AM[i + 1] for i in range(L - 1, N - M))
  def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
    N = len(A)
    if L + M == N:
      return sum(A)
    return max(self.maxSumTwoNoOverlapUnit(A, L, M), self.maxSumTwoNoOverlapUnit(A, M, L))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # ([2,3,1,1,4], 1, 2),
    ([67,38,92,21,91,24,25,20,100,41,22,56,63,42,95,76,84,79,89,3], 18, 1),
  ]
  rslts = [solver.maxSumTwoNoOverlap(A, L, M) for A, L, M in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
