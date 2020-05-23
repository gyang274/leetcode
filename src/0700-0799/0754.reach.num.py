class Solution:
  def reachNumber(self, target: int) -> int:
    #  argmin_n s.t. T = sum(1:n) = t + k, k & 1 == 0
    x, T, t  = 1, 0, abs(target)
    while T < t or (T - t) & 1:
      T += x
      x += 1
    return x - 1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.reachNumber(target) for target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
