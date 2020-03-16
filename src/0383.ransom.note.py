from collections import Counter

class Solution:
  def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    """HashMap, O(N).
    """
    if len(ransomNote) > len(magazine):
      return False
    # counter of characters in magazine
    cntr = Counter(magazine)
    # check constructability
    for s in ransomNote:
      cntr[s] -= 1
      if cntr[s] < 0:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("a", "b"),
    ("a", "ab"),
    ("aa", "ab"),
    ("aaa", "aaba"),
    ("aaaa", "aaba"),
  ]
  rslts = [solver.canConstruct(ransomNote, magazine) for ransomNote, magazine in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
        