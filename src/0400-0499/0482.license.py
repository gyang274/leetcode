class Solution:
  def licenseKeyFormatting(self, S: str, K: int) -> str:
    s, i = "", 0
    for x in S[::-1]:
      if not x == "-":
        s += x.upper()
        i += 1
        if (i + 1) % (K + 1) == 0:
          s += "-"
          i += 1
    return s[(-1 + (-1 if s[-1] == "-" else 0))::-1] if s else ""

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", 2),
    ("--", 2),
    ("2-5g-3-J", 2),
    ("2-5g-3-J", 3),
    ("5F3Z-2e-9-w", 4),
  ]
  rslts = [solver.licenseKeyFormatting(S, K) for S, K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
