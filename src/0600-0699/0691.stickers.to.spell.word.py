from typing import List
from collections import Counter

class Solution:
  def recursive(self, t):
    key = tuple(sorted(t.items()))
    if key not in self.memo:
      self.memo[key] = -1
      for s in self.stickers:
        u = s.keys() & t.keys()
        if u:
          tnext = t.copy()
          for k in u:
            tnext[k] -= s[k]
            if tnext[k] <= 0:
              tnext.pop(k)
          if tnext:
            n = 1 + self.recursive(tnext)
            n = n if n > 0 else -1
          else:
            n = 1
          if self.memo[key] == -1 or self.memo[key] > n:
            self.memo[key] = n
    return self.memo[key]
  def minStickers(self, stickers: List[str], target: str) -> int:
    """Q0638.
    """
    self.target = Counter(target)
    self.stickers = [Counter(sticker) & self.target for sticker in stickers]
    for i in range(len(self.stickers) - 1, -1, -1):
      if not self.stickers[i] or any(
        self.stickers[i] == self.stickers[i] & self.stickers[j] for j in range(len(self.stickers)) if not i == j
      ):
        self.stickers.pop(i)
    self.memo = {}
    return self.recursive(self.target)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["with", "example", "science"], "thehat"),
  ]
  rslts = [solver.minStickers(stickers, target) for stickers, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
