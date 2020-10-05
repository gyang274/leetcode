from collections import defaultdict

class Solution:
  def sortString(self, s: str) -> str:
    d = defaultdict(lambda: 0)
    for x in s:
      d[x] += 1
    z = ''
    while d:
      k = sorted(d.keys())
      for x in k + k[::-1]:
        if d[x] > 0:
          z += x
          d[x] -= 1
        if d[x] == 0:
          d.pop(x)
    return z

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "leetcode",
  ]
  rslts = [solver.sortString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
