from typing import List

class Solution:
  def reorderSpaces(self, text: str) -> str:
    n = len(text)
    words = text.split()
    ans = words[0] if len(words) == 1 else (' ' * ((n - sum(map(len, words))) // (len(words) - 1))).join(words)
    return ans + ' ' * (n - len(ans))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    " hello  world   !    ",
  ]
  rslts = [solver.reorderSpaces(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
