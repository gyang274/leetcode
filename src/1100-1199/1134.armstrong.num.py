class Solution:
  def isArmstrong(self, N: int) -> bool:
    x, k, n = 0, len(str(N)), N
    while n > 0:
      x += (n % 10) ** k
      n //= 10
    return x == N

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 5, 8, 153, 370, 371, 407,
  ]
  rslts = [solver.isArmstrong(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
