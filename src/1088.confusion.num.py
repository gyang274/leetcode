class Solution:
  def confusingNumberII(self, N: int) -> int:
    d = {
      '0': '0',
      '1': '1',
      '6': '9',
      '8': '8',
      '9': '6',
    }
    self.count = 0
    def dfs(s, r):
      if not s == r:
        self.count += 1
      for x in d:
        if int(s + x) <= N:
          dfs(s + x, d[x] + r)
    dfs('1', '1')
    dfs('6', '9')
    dfs('8', '8')
    dfs('9', '6')
    return self.count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 23, 42, 85,
  ]
  rslts = [solver.confusingNumberII(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
