class Solution:
  def maxPower(self, s: str) -> int:
    z, n, m = '', 0, 1
    for x in s:
      if x == z:
        n += 1
      else:
        z, n = x, 1
      m = max(m, n)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "leetcode",
    "hooraaaaaaaaaaay"
  ]
  rslts = [solver.maxPower(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
