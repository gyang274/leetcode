from typing import List

class Solution:
  def movesToStamp(self, stamp: str, target: str) -> List[int]:
    m, n, s, t, ans = len(stamp), len(target), list(stamp), list(target), []
    # work backward
    # let d[i] = (j1, j2, ..), i <= j < i + n, where stamp[j - i] == target[j], i is ok to stamp when len(d[i]) == n
    # stamp[j - i] == target[j] if same character in the beginning or k stamped, j - n < k <= j
    def check(i):
      changed = False
      for j in range(m):
        if t[i + j] == '?':
          continue
        elif t[i + j] != s[j]:
          return False
        else:
          changed = True
      if changed:
        t[i:(i + m)] = ['?'] * m
        ans.append(i)
      return changed
    changed = True
    while changed:
      changed = False
      for i in range(n - m + 1):
        changed |= check(i)
    return ans[::-1] if t == ['?'] * n else []

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", "ababc"),
    ("abca", "aabcaca"),
    ("de", "ddeddeddee"),
    ("zbs", "zbzbsbszbssbzbszbsss"),
  ]
  rslts = [solver.movesToStamp(stamp, target) for stamp, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
