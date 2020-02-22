class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    """Track replacement with HashMap on both directions.
    """
    p, q = {}, {}
    for x, y in zip(s, t):
      if (x in p) and (y in q):
        if not (p[x] == y and q[y] == x):
          return False
      elif (x in p) ^ (y in q):
        return False
      else:
        p[x] = y
        q[y] = x
    return True

class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return [s.find(i) for i in s] == [t.find(j) for j in t]
    
class Solution:
  def isIsomorphic(self, s: str, t: str) -> bool:
    return list(map(s.find, s)) == list(map(t.find, t))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", ""),
    ("a", "a"),
    ("a", "b"),
    ("bar", "foo"),
    ("foo", "bar"),
    ("add", "egg"),
    ("paper", "title"),
  ]
  rslts = [solver.isIsomorphic(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  