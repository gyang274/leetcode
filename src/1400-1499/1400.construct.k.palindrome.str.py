from collections import Counter

class Solution:
  def canConstruct(self, s: str, k: int) -> bool:
    return len(list(filter(lambda x: x & 1, Counter(s).values()))) <= k <= len(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("annabelle", 2),
    ("leetcoded", 3),
  ]
  rslts = [solver.canConstruct(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
