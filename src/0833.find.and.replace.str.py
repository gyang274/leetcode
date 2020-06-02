from typing import List

class Solution:
  def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
    s = list(S)
    for i, x, y in reversed(sorted(list(zip(indexes, sources, targets)))):
      if S[i:(i + len(x))] == x:
        s[i:(i + len(x))] = list(y)
    return ''.join(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcd", [0, 2], ["a", "cd"], ["eee", "ffff"]),
    ("abcd", [0, 2], ["ab", "ec"], ["eee", "ffff"]),
    ("vmokgggqzp", [3,5,1], ["kg","ggq","mo"], ["s","so","bfr"]),
  ]
  rslts = [solver.findReplaceString(S, indexes, sources, targets) for S, indexes, sources, targets in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
