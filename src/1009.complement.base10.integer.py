class Solution:
  def bitwiseComplement(self, N: int) -> int:
    if N == 0:
      return 1
    x, i = 0, 0
    while N:
      if (N & 1) ^ 1:
        x |= 1 << i
      N >>= 1
      i += 1
    return x

class Solution:
  def bitwiseComplement(self, N: int) -> int:
    # Q0476
    if N == 0:
      return 1
    mask, runs = 0, N
    while runs:
      mask = (mask << 1) | 1
      runs >>= 1
    return mask ^ N

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.bitwiseComplement(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
