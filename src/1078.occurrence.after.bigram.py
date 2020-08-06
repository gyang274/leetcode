from typing import List

class Solution:
  def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
    ans, text = [], text.split()
    for i in range(2, len(text)):
      if text[i - 2] == first and text[i - 1] == second:
        ans.append(text[i])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("we will we will rock you", "we", "will"),
  ]
  rslts = [solver.findOcurrences(text, first, second) for text, first, second in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
