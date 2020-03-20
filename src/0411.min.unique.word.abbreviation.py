from typing import List

import itertools

class Solution:
  def abbrLen(self, mask):
    """length of abbreviation given a bit mask str.
    """
    return mask.count('1') + sum([len(str(len(n0))) for n0 in mask.split('1') if not n0 == ""])
  def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
    """Q0320 + Q0408
    """
    # mask of characters in target should keep to distinguish with source in dictionary.
    # e.g., target: apple, sourcee appds, then mask = 00011, means must contain one of le to distinguish
    masks = []
    for source in dictionary:
      if len(source) == len(target):
        ms = "".join(["0" if x == y else "1" for x, y in zip(source, target)])
        masks.append((ms, int(ms, 2)))
    if masks == []:
      return str(len(target))
    # dfs/backtrack?
    minNt, minMt = len(target), target
    # n1minNt: min abbreviation length given n1 num of character
    n1 = 1
    n1minNt = self.abbrLen("".join(["1"] * n1 + ["0"] * len(target)))
    while n1minNt < minNt:
      mts = ["".join(mt) for mt in set(itertools.permutations(["1"] * n1 + ["0"] * (len(target) - n1)))]
      for mt in mts:
        mt2 = int(mt, 2)
        for ms, ms2 in masks:
          if mt2 & ms2 == 0:
            break
        else:
          nt = self.abbrLen(mt)
          if nt < minNt:
            minNt, minMt = nt, mt
      n1 += 1
      n1minNt = self.abbrLen("".join(["1"] * n1 + ["0"] * len(target)))
    # construct abbreviation given mask
    abbr, i = "", 0
    while i < len(target):
      if minMt[i] == "1":
        abbr += target[i]
        i += 1
      else:
        k = 1
        while i + k < len(target) and minMt[i + k] == "0":
          k += 1
        abbr += str(k)
        i += k
    return abbr

class Solution:
  def abbrLen(self, mask):
    """length of abbreviation given a bit mask str.
    """
    # Each number or letter in the abbreviation is considered length = 1. 
    # For example, the abbreviation "a32bc" has length = 4.
    return mask.count('1') + sum([1 for n0 in mask.split('1') if not n0 == ""])
  def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
    """Q0320 + Q0408
    """
    # mask of characters in target should keep to distinguish with source in dictionary.
    # e.g., target: apple, sourcee appds, then mask = 00011, means must contain one of le to distinguish
    masks = []
    for source in dictionary:
      if len(source) == len(target):
        ms = "".join(["0" if x == y else "1" for x, y in zip(source, target)])
        masks.append((ms, int(ms, 2)))
    if masks == []:
      return str(len(target))
    # dfs/backtrack?
    minNt, minMt = len(target), "1" * len(target)
    # n1minNt: min abbreviation length given n1 num of character
    n1 = 1
    n1minNt = self.abbrLen("1" * n1 + "0" * (len(target) - n1))
    while n1minNt < minNt:
      mts = ["".join(mt) for mt in set(itertools.permutations("1" * n1 + "0" * (len(target) - n1)))]
      for mt in mts:
        mt2 = int(mt, 2)
        for ms, ms2 in masks:
          if mt2 & ms2 == 0:
            break
        else:
          nt = self.abbrLen(mt)
          if nt < minNt:
            minNt, minMt = nt, mt
      n1 += 1
      n1minNt = self.abbrLen("1" * n1 + "0" * (len(target) - n1))
    # print(f"{minNt=}, {minMt=}")
    # construct abbreviation given mask
    abbr, i = "", 0
    while i < len(target):
      if minMt[i] == "1":
        abbr += target[i]
        i += 1
      else:
        k = 1
        while i + k < len(target) and minMt[i + k] == "0":
          k += 1
        abbr += str(k)
        i += k
    return abbr

class Solution:
  def abbrLen(self, mask):
    """length of abbreviation given bit sequence
    """
    b, count = 3, self.n
    while b < self.bn:
      if mask & b == 0:
        count -= 1
      b <<= 1
    return count
  def backtrack(self, bs, mt):
    """DFS backtrack.
      Args:
        bs: start bs for DFS, left of leftmost bit of mt.
        mt: abbreviation mask of target.
    """
    l = self.abbrLen(mt)
    if l >= self.minLen:
      return None
    ok = True
    for ms in self.masks:
      if mt & ms == 0:
        ok = False
        break
    if ok:

      self.minLen, self.minMt = l, mt
    else:
      b = bs
      while b < self.bn:
        if self.maskd & b:
          self.backtrack(b << 1, mt | b)
        b <<= 1
  def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
    self.n = len(target)
    self.bn = 1 << self.n
    self.minLen = self.n
    self.minMt = (1 << self.n) - 1
    # masks
    # self.masks: mask to each individual word in dictionary
    # self.maskd: an "or" of individual mask to show all possible characters considered for keep in abbreviation
    self.masks = []
    self.maskd = 0
    for source in dictionary:
      if len(source) == len(target):
        ms = 0
        for i in range(1, self.n + 1):
          if not source[-i] == target[-i]:
            ms |= 1 << (i - 1)
        self.masks.append(ms)
        self.maskd |= ms
    # print(f"{self.maskd=}, {self.masks=}")
    # print(f"{bin(self.maskd)=}, {[bin(ms) for ms in self.masks]=}")
    # dfs/backtrack
    self.backtrack(1, 0)
    # construct abbreviation from a bit sequence
    # print(f"{self.minLen=}, {self.minMt=}")
    abbr, i = "", 1
    while self.minMt:
      if self.minMt & 1 == 0:
        k = 0
        while self.minMt & 1 == 0:
          self.minMt >>= 1
          k += 1
        abbr = str(k) + abbr
        i += k
      else:
        abbr = target[-i] + abbr
        self.minMt >>= 1
        i += 1
    if i < self.n + 1:
      abbr = str(self.n + 1 - i) + abbr
    return abbr

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("apple", ["amber"]),
    ("apple", ["amber", "blade"]),
    ("apple", ["amber", "blade", "plain"]),
    ("apple", ["amber", "apply", "blade", "plain"]),
    ("abc", ["abd","acd","acc"]),
    ("aaaaaxaaaaa", ["bbbbbxbbbbb"]),
  ]
  rslts = [solver.minAbbreviation(target, dictionary) for target, dictionary in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
