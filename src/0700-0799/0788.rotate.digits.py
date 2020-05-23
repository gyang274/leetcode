class Solution:
  def rotatedDigits(self, N: int) -> int:
    A = list(map(int, str(N)))
    memo = {}
    def dp(i, equality, involution):
      if i == len(A):
        return +(involution)
      if (i, equality, involution) not in memo:
        memo[(i, equality, involution)] = 0
        for d in range((A[i] + 1) if equality else 10):
          if d not in {3, 4, 7}:
            memo[(i, equality, involution)] += dp(i + 1, equality and d == A[i], involution or d in {2, 5, 6, 9})
      return memo[(i, equality, involution)]
    return dp(0, True, False)

class Solution:
  def rotatedDigits(self, N: int) -> int:
    N = list(map(int, str(N)))
    s0 = set([0, 1, 8, 2, 5, 6, 9])
    s1 = set([0, 1, 8])
    count, s = 0, set([])
    for i, x in enumerate(N):
      for j in range(x):
        if s.issubset(s0) and j in s0:
          count += 7 ** (len(N) - i - 1)
        if s.issubset(s1) and j in s1:
          count -= 3 ** (len(N) - i - 1)
      if x not in s0:
        return count
      s.add(x)
    return count + (s.issubset(s0) and not s.issubset(s1))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    10, 2374,
  ]
  rslts = [solver.rotatedDigits(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
