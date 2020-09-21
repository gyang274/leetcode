class Solution:
  def balancedStringSplit(self, s: str) -> int:
    # b: balance, k: count of splits
    b, k = 0, 0
    for x in s:
      if x == 'L':
        b -= 1
      else:
        b += 1
      if b == 0:
        k += 1
    return k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "RLRRLLRLRL",
    "RLLLLRRRLR",
    "LLLLLRRRRR",
    "RLRRRLLRLL",
  ]
  rslts = [solver.balancedStringSplit(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
