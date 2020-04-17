class Solution:
  def expand(self, s, ns):
    for i in range(2):
      if isinstance(s[i], int):
        s[i] = [s[i], ns + 1 - s[i]]
      else:
        self.expand(s[i], ns)
    return None
  def write(self, s):
    if isinstance(s[0], int):
      return "(" + ",".join(map(str, s)) + ")"
    else:
      return "(" + ",".join(map(self.write, s)) + ")"
  def findContestMatch(self, n: int) -> str:
    s, ns = [1,2], 2
    while ns < n:
      ns *= 2
      self.expand(s, ns)
    return self.write(s)

class Solution:
  def findContestMatch(self, n):
    s = list(map(str, range(1, n + 1)))
    while n > 1:
      for i in range(n // 2):
        s[i] = "({},{})".format(s[i], s.pop())
      n //= 2
    return s[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    8, 
  ]
  rslts = [solver.findContestMatch(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")