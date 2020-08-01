class Solution:
  def confusingNumber(self, N: int) -> bool:
    d = {
      '0': '0',
      '1': '1',
      '6': '9',
      '8': '8',
      '9': '6',
    }
    s = str(N)
    return not (set(s) - {'0', '1', '6', '8', '9'} or ''.join(map(lambda x: d[x], reversed(s))) == s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 6, 8, 11, 23, 69, 89, 99,
  ]
  rslts = [solver.confusingNumber(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
