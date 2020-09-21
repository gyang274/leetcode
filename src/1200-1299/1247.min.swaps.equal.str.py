from collections import defaultdict

class Solution:
  def minimumSwap(self, s1: str, s2: str) -> int:
    # s1: xx |
    # s2: yy | -> one swap to make equal
    #
    # s1: xy |
    # s2: yx | -> two swap to make equal, use at most once
    #
    # d: count of num of not match, w.r.t x, y in s1
    d = defaultdict(lambda: 0)
    for c1, c2 in zip(s1, s2):
      d[c1] += (c1 != c2)
    if sum(d.values()) & 1:
      return -1
    return d['x'] // 2 + d['y'] // 2 + ((d['x'] & 1) + (d['y'] & 1))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("xx", "yy"),
    ("xx", "xy"),
    ("xy", "yx"),
    ("xxyyxyxyxx", "xyyxyxxxyx"),
  ]
  rslts = [solver.minimumSwap(s1, s2) for s1, s2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
