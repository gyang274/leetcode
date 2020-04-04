from collections import Counter

class Solution:
  def frequencySort(self, s: str) -> str:
    return ''.join([k * v for k, v in sorted([(k, v) for k, v in Counter(s).items()], key=lambda x: (-x[1], x[0]))])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "a",
    "ab",
    "aba",
  ]
  rslts = [solver.frequencySort(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
