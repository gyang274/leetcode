class Solution:
  def generateTheString(self, n: int) -> str:
    return 'x' * n if n & 1 else 'x' * (n - 1) + 'y'

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.generateTheString(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
