from typing import List

class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    def camelMatchUnit(query):
      i, j, m, n = 0, 0, len(query), len(pattern)
      while i < m:
        while i < m and j < n and query[i] != pattern[j] and query[i].islower():
          i += 1
        if i < m and j < n and query[i] == pattern[j]:
          i += 1
          j += 1
        else:
          break
      if j == n:
        while i < m and query[i].islower():
          i += 1
      return i == m and j == n
    return list(map(camelMatchUnit, queries))

class Solution:
  def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
    def u(s):
      return [c for c in s if c.isupper()]
    def issup(s, t):
      it = iter(t)
      return all(c in it for c in s)
    p = pattern
    return [u(p) == u(q) and issup(p, q) for q in queries]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB"),
    (["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa"),
    (["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT"),
  ]
  rslts = [solver.camelMatch(queries, pattern) for queries, pattern in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
