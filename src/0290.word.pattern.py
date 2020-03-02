class Solution:
  def wordPattern(self, pattern: str, str: str) -> bool:
    # zip will shorten the longer one
    wlist = str.split(' ')
    if not len(pattern) == len(wlist):
      return False
    # check mapping: bi-directional one to one
    cw, wc = {}, {}
    for c, w in zip(list(pattern), wlist):
      if c in cw or w in wc:
        if not (c in cw and w in wc and cw[c] == w and wc[w] == c):
          return False
      else:
        cw[c] = w
        wc[w] = c
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aaaa", "aa aa aa"),
    ("aaaa", "aa aa aa aa"),
    ("abba", "dog cat cat dog"),
    ("abba", "dog cat cat fish"),
    ("aaaa", "dog cat cat dog"),
    ("abba", "dog dog dog dog"),
  ]
  rslts = [solver.wordPattern(pattern, str) for pattern, str in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
