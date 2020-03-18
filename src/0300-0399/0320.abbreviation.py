from typing import List

class Solution:
  def generateAbbreviations(self, word: str) -> List[str]:
    if len(word) == 0:
      return [""]
    elif len(word) == 1:
      return ["1", word]
    else:
      l = len(word)
      m = l // 2
      ans = []
      for x in self.generateAbbreviations(word[:m]):
        for y in self.generateAbbreviations(word[m:]):
          if x[-1].isdigit() and y[0].isdigit():
            ans.append(x[:-1] + str(int(x[-1]) + int(y[0])) + y[1:])
          else:
            ans.append(x + y)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "word",
    "leetcode",
  ]
  rslts = [solver.generateAbbreviations(word) for word in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")