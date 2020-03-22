from typing import List

class Solution:
  def validWordSquare(self, words: List[str]) -> bool:
    for i in range(len(words)):
      for j in range(len(words[i])):
        if not (j < len(words) and i < len(words[j]) and words[i][j] == words[j][i]):
          return False
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [
      "abcd",
      "bnrt",
      "crmy",
      "dtye",
    ],
    [
      "abcd",
      "bnrt",
      "crm",
      "dt",
    ],
    [
      "ball",
      "area",
      "read",
      "lady",
    ],
  ]
  rslts = [solver.validWordSquare(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")