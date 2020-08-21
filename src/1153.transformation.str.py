class Solution:
  def canConvert(self, str1: str, str2: str) -> bool:
    d = {}
    for x, y in zip(str1, str2):
      if x in d and d[x] != y:
        return False
      d[x] = y
    # no cycle when fully occupied..
    if len(d) == 26 and len(set(d.values())) == 26:
      return all(d[x] == x for x in d)
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("aabbc", "ccdde"),
    ("leetcode", "codeleet"),
    ("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyza"),
    ("abcdefghijklmnopqrstuvwxyz", "bcdefghijklmnopqrstuvwxyzq"),
  ]
  rslts = [solver.canConvert(str1, str2) for str1, str2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
