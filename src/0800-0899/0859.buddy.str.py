class Solution:
  def buddyStrings(self, A: str, B: str) -> bool:
    if len(A) != len(B):
      return False
    d, hold = 0, None
    if len(A) > 26:
      for x, y in zip(A, B):
        if x != y:
          d += 1
          if d == 1:
            hold = (x, y)
          elif d == 2:
            if not hold == (y, x):
              return False
          else:
            return False
      return d == 0 or d == 2
    else:
      seen, s = set(), False
      for x, y in zip(A, B):
        if x != y:
          d += 1
          if d == 1:
            hold = (x, y)
          elif d == 2:
            if not hold == (y, x):
              return False
          else:
            return False
        else:
          if x in seen:
            s = True
          else:
            seen.add(x)
      return (s and d == 0) or d == 2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aa", "aa"),
    ("ab", "ba"),
    ("ab", "ca"),
    ("abcaa", "abcbb"),
  ]
  rslts = [solver.buddyStrings(A, B) for A, B in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
