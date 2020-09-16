class Solution:
  def subtractProductAndSum(self, n: int) -> int:
    p, s = 1, 0
    while n:
      p *= n % 10
      s += n % 10
      n //= 10
    return p - s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2714,
  ]
  rslts = [solver.subtractProductAndSum(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
