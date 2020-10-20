class Solution:
  def checkIfCanBreak(self, s1: str, s2: str) -> bool:
    s1, s2 = sorted(list(s1)), sorted(list(s2))
    return all(x <= y for x, y in zip(s1, s2)) or all(x >= y for x, y in zip(s1, s2))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", "xyz"),
    ("abe", "acd"),
  ]
  rslts = [solver.checkIfCanBreak(s1, s2) for s1, s2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
