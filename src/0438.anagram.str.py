from typing import List

class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    """two pointers
    """
    ans = []
    ns, np = len(s), len(p)
    if ns >= np:
      # pattern as list of counts a-z
      q = [0] * 26
      for x in p:
        q[ord(x) - ord("a")] += 1
      # init s
      i, t = 0, [0] * 26
      while i < np - 1:
        t[ord(s[i]) - ord("a")] += 1
        i += 1
      while i < ns:
        t[ord(s[i]) - ord("a")] += 1
        i += 1
        if t == q:
          ans.append(i - np)
        t[ord(s[i - np]) - ord("a")] -= 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcabc", "abc"),
  ]
  rslts = [solver.findAnagrams(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")