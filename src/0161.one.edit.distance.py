class Solution:
  def isOneEditDistance(self, s: str, t: str) -> bool:
    if abs(len(s) - len(t)) > 1:
      return False
    if len(s) - len(t) == 1:
      # deletion
      i, j = 0, -1
      while i < len(t):
        if s[i] == t[i]:
          i += 1
        elif j == -1:
          j = i
          s = s[:j] + s[(j + 1):]
        else:
          return False
      return True
    elif len(s) - len(t) == -1:
      # insertion
      i, j = 0, -1
      while i < len(s):
        if s[i] == t[i]:
          i += 1
        elif j == -1:
          j = i
          t = t[:j] + t[(j + 1):]
        else:
          return False
      return True
    else:
      # replacement
      i, j = 0, -1
      while i < len(s):
        if s[i] == t[i]:
          i += 1
        elif j == -1:
          j = i
          i += 1
        else:
          return False
      if j == -1:
        return False
      return True

class Solution:
  def isOneEditDistance(self, s: str, t: str) -> bool:
    ns, nt = len(s), len(t)
    if ns > nt:
      s, t, ns, nt = t, s, nt, ns
    if nt - ns > 1:
      return False
    if nt - ns == 0 and s == t:
      return False
    for i in range(ns):
      if not s[i] == t[i]:
        if ns == nt:
          return s[(i + 1):] == t[(i + 1):]
        else:
          return s[i:] == t[(i + 1):]
    return True
    
if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ("", ""),
    ("ab", "ab"),
    ("ab", "acb"),
    ("ad", "cab"),
    ("1024", "1324")
  ]
  rslts = [
    solver.isOneEditDistance(s, t) for s, t in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs}, solution: {rs}")

