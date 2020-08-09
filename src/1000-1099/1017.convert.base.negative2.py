class Solution:
  def baseNeg2(self, N: int) -> str:
    if N < 2:
      return str(N)
    x = ''
    while N:
      # 0, 1, 2, 3 => 00, 01, 10, 11
      x = ['00', '01', '10', '11'][N % 4] + x
      if N % 4 > 1:
        N += N % 4
      N >>= 2
    return str(int(x))

class Solution:
  def baseNeg2(self, N: int) -> str:
    if N < 2:
      return str(N)
    x = ''
    while N:
      x += str(N & 1)
      N = -(N >> 1)
    return x[::-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 4, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.baseNeg2(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
