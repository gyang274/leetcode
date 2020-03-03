from collections import Counter

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("", ""),
    ("rad", "car"),
    ("anagram", "nagaram"),
  ]
  rslts = [solver.isAnagram(s, t) for s, t in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")