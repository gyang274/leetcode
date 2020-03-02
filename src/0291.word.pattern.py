from collections import defaultdict

class Solution:
  def backtrack(self, cidx, pinit, sinit, nsleft) -> bool:
    """Args
      cidx: index of next characters (unique, ordered) from pattern for find recursive mapping.
      pinit: index of characters in pattern itself wait for the mapping from cidx, self.cw and self.wc.
      sinit: index of characters in str itself wait for the mapping from cidx, self.cw and self.wc.
      nsleft: num of characters in str available for make any mapping, fast fail.
    """
    # print(f"in: {cidx=}, {pinit=}, {sinit=}, {nsleft=}")
    if cidx == len(self.cs):
      return pinit == self.np and sinit == self.ns
    # next unseen character
    c = self.cs[cidx]
    # this character from pattern can map to i0, .., i1 characters in str
    i0 = 1
    i1 = (nsleft - (len(self.cs) - 1 - cidx)) // self.cc[c] + 1
    # c is the last one? if so, mapping is uniquely defined.
    if cidx == len(self.cs) - 1:
      # c -> num of charaters from str
      if (nsleft == 0) or (nsleft % self.cc[c]):
        return False
      i0 = nsleft // self.cc[c]
    # iterative on each mapping, is this match ok?
    for i in range(i0, i1):
      w = self.str[sinit:(sinit + i)]
      if w not in self.wc:
        self.cw[c] = w
        self.wc[w] = c
        jpinit, jsinit, jnsleft = pinit, sinit, nsleft - i * self.cc[c]
        ok = None
        while jpinit < self.np:
          jc = self.pattern[jpinit]
          if jc in self.cw:
            jw = self.str[jsinit:(jsinit+len(self.cw[jc]))]
            if jw == self.cw[jc]:
              jpinit += 1
              jsinit += len(self.cw[jc])
            else:
              break
          else:
            break
        if jpinit == self.np or self.pattern[jpinit] not in self.cw:
          if self.backtrack(cidx + 1, jpinit, jsinit, jnsleft):
            return True
        self.cw.pop(c)
        self.wc.pop(w)
    return False
  def wordPatternMatch(self, pattern: str, str: str) -> bool:
    # global refr
    self.pattern, self.str = pattern, str
    self.np, self.ns = len(pattern), len(str)
    if self.np == 0:
      return self.ns == 0
    # cw: pattern character to word in str
    # wc: word in str to pattern character
    self.cw, self.wc = {}, {}
    # cs: list of character in pattern
    # cc: count of each character in pattern
    self.cs, self.cc = [], defaultdict(lambda: 0)
    for c in pattern:
      if c not in self.cc:
        self.cs.append(c)
      self.cc[c] += 1
    # backtrack
    # a bidirectional 1-to-1 mapping such that each character c_i in pattern mapping to n_i characters (word w_i) in str
    return self.backtrack(0, 0, 0, self.ns)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # ("", ""),
    ("ab", "cd"),
    ("aaaa", "asdasdasdasd"),
    ("aabb", "xyzabcxzyabc"),
    ("abab", "redblueredblue"),
    ("abba", "xyzabcxzyabc"),
  ]
  rslts = [solver.wordPatternMatch(pattern, str) for pattern, str in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
