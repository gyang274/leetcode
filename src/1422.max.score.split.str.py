from collections import Counter

class Solution:
  def maxScore(self, s: str) -> int:
    m, l, r = 0, 0, Counter(s)["1"]
    for x in s[:-1]:
      if x == '0':
        l += 1
      else:
        r -= 1
      m = max(m, l + r)
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0110111",
  ]
  rslts = [solver.maxScore(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
