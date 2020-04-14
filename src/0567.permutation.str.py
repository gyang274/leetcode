from collections import Counter, defaultdict

class Solution:
  def checkInclusion(self, s1: str, s2: str) -> bool:
    """permutation <=> counter() equality.
    """
    n1, n2 = len(s1), len(s2)
    if n1 > n2:
      return False
    s1counter = Counter(s1)
    s2counter = Counter(s2[:n1])
    if s2counter == s1counter:
      return True
    j, i = 0, n1
    while i < n2:
      s2counter[s2[i]] += 1
      s2counter[s2[j]] -= 1
      if s2counter[s2[j]] == 0:
        s2counter.pop(s2[j])
      if s2counter == s1counter:
        return True
      i += 1
      j += 1
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("oc", "leetcode"),
  ]
  rslts = [solver.checkInclusion(s1, s2) for s1, s2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
