class Solution:
  def numSub(self, s: str) -> int:
    r, u = 0, 0
    for x in s + '0':
      if x == '1':
        r += 1
      else:
        u += r * (r + 1) // 2
        r = 0
    return u % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "011011101011",
  ]
  rslts = [solver.numSub(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
