class Solution:
  def moves(self, node):
    n, node = len(node), list(node)
    ans = []
    for i in range(n):
      if node[i] == 'X':
        if i - 1 >= 0 and node[i - 1] == 'R':
          nuxt = node.copy()
          nuxt[i - 1], nuxt[i] = nuxt[i], nuxt[i - 1]
          ans.append(''.join(nuxt))
        if i + 1 < n and node[i + 1] == 'L':
          nuxt = node.copy()
          nuxt[i], nuxt[i + 1] = nuxt[i + 1], nuxt[i]
          ans.append(''.join(nuxt))
    return ans
  def canTransform(self, start: str, end: str) -> bool:
    if start == end:
      return True
    seen, queue = {start}, [start]
    while queue:
      qnext = []
      for node in queue:
        for nuxt in self.moves(node):
          if nuxt == end:
            return True
          if nuxt not in seen:
            seen.add(nuxt)
            qnext.append(nuxt)
      queue = qnext
    return False

class Solution:
  def canTransform(self, start: str, end: str) -> bool:
    if start == end:
      return True
    l = r = 0
    for p in zip(start, end):
      if r > 0 and 'L' in p:
        return False
      if l > 0 and 'R' in p:
        return False
      if p == ('L', 'R'):
        return False
      if p == ('R', 'L'):
        return False
      # moves
      if p == ('R', 'X'):
        r += 1
      elif p == ('X', 'R'):
        r -= 1
      elif p == ('X', 'L'):
        l += 1
      elif p == ('L', 'X'):
        l -= 1
      # scheduled moves compatible or not
      if l < 0 or r < 0 or (l > 0 and r > 0):
        return False
    return r == l == 0

class Solution:
  def canTransform(self, start: str, end: str) -> bool:
    n = len(start)
    if not start.replace('X', '') == end.replace('X', ''):
      return False
    l = r = 0
    for i, x in enumerate(start):
      if start[i] == 'L':
        while l < n and not end[l] == 'L':
          l += 1
        if i < l:
          return False
        l += 1
      elif start[i] == 'R':
        while r < n and not end[r] == 'R':
          r += 1
        if i > r:
          return False
        r += 1
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ('X', 'L'),
    ("RXXLRXRXL", "XRLXXRRLX"),
    ("XXXXXLXXXLXXXX", "XXLXXXXXXXXLXX"),
    ("XRRXLXLXRLXLRRXXXRXXRRRXXRXLXX", "XXXXRRLLXRLXXXLXRRRRRXRXXXRXLX"),
    ("XXRXXXXRXXXXXXRXXXXLXXXXLXLXXXXXXRXXXXLX", "XXXXXXXXXXXXRRRLLLXXXXXXXXXXXXXXXXXXRLXX"),
  ]
  rslts = [solver.canTransform(start, end) for start, end in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
