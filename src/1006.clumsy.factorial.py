class Solution:
  def clumsy(self, N: int) -> int:
    if N < 3:
      return N
    X, N = N * (N - 1) // (N - 2), N - 3
    while N > 0:
      if N > 3:
        X += N - (N - 1) * (N - 2) // (N - 3)
        N -= 4
      else:
        X += 1
        N -= N
    return X

class Solution:
  def clumsy(self, N: int) -> int:
    # observe: N * (N - 1) // (N - 2) = (N + 1), ...
    magic = [1, 2, 2, -1, 0, 0, 3, 3]
    return N + (magic[N % 4] if N > 4 else magic[N + 3])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.clumsy(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
