class Solution:
  def minFlips(self, target: str) -> int:
    s, n = '0', 0
    for x in target:
      if x != s:
        s, n = x, n + 1
    return n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "01",
    "101",
    "10111",
    "001011101",
  ]
  rslts = [solver.minFlips(target) for target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
