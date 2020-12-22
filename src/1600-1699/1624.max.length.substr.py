class Solution:
  def maxLengthBetweenEqualCharacters(self, s: str) -> int:
    d = {}
    for i, x in enumerate(s):
      if x in d:
        d[x][1] = i
      else:
        d[x] = [i, i]
    return max(d[x][1] - d[x][0] - 1 for x in d)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "aa", "abcabc", "abcxyz", "cabbac",
  ]
  rslts = [solver.maxLengthBetweenEqualCharacters(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
