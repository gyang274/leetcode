from typing import List

class Solution:
  def minKBitFlips(self, A: List[int], K: int) -> int:
    """TC: O(N), SC: O(N), Greedy.
    """
    N = len(A)
    if K == 1:
      return N - sum(A)
    count, X, k = 0, [0] * N, 1
    for i in range(N - K + 1):
      if i >= K:
        k ^= X[i - K]
      X[i] = A[i] ^ k
      k ^= X[i]
    for i in range(N - K + 1, N):
      if i >= K:
        k ^= X[i - K]
      if A[i] ^ k:
        return -1
    return sum(X)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([0,1,0], 1),
    ([0,1,0], 2),
    ([0,1,1], 2),
    ([0,0,0,1,0,1,1,0], 3),
    ([1,1,1,1,1,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,0,1,1,1,0,0,0,0,1,1,1], 8),
  ]
  rslts = [solver.minKBitFlips(A, K) for A, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
