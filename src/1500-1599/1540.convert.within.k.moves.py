class Solution:
  def canConvertString(self, s: str, t: str, k: int) -> bool:
    if len(s) != len(t):
      return False
    # num of times this difference seen
    seen = [0] * 26
    for x, y in zip(s, t):
      d = (ord(y) - ord(x)) % 26
      # num of moves required after previous seen
      if d > 0 and seen[d] * 26 + d > k:
        return False
      seen[d] += 1
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", "bcd", 27),
    ("input", "ouput", 9),
  ]
  rslts = [solver.canConvertString(s, t, k) for s, t, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
