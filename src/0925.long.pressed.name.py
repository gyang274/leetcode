class Solution:
  def isLongPressedName(self, name: str, typed: str) -> bool:
    m, n = len(name), len(typed)
    A = [[name[0], 1]]
    for i in range(1, m):
      if name[i] == name[i - 1]:
        A[-1][1] += 1
      else:
        A.append([name[i], 1])
    B = [[typed[0], 1]]
    for j in range(1, n):
      if typed[j] == typed[j - 1]:
        B[-1][1] += 1
      else:
        B.append([typed[j], 1])
    return len(A) == len(B) and all(a[0] == b[0] and a[1] <= b[1] for a, b in zip(A, B))

from itertools import groupby

class Solution:
  def isLongPressedName(self, name: str, typed: str) -> bool:
    g1 = [(k, len(list(grp))) for k, grp in groupby(name)]
    g2 = [(k, len(list(grp))) for k, grp in groupby(typed)]
    return len(g1) == len(g2) and all(k1 == k2 and v1 <= v2 for (k1,v1), (k2,v2) in zip(g1, g2))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("alex", "alex"),
    ("alex", "aaleex"),
    ("alex", "aeeeex"),
    ("laidez", "laideccc")
  ]
  rslts = [solver.isLongPressedName(name, typed) for name, typed in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")