from typing import List


class Solution:
  def letterCombinations(self, digits: str) -> List[str]:
    if digits == "":
      return []
    d2s = {
      '0': '',
      '1': '',
      '2': 'abc',
      '3': 'def',
      '4': 'ghi',
      '5': 'jkl',
      '6': 'mno',
      '7': 'pqrs',
      '8': 'tuv',
      '9': 'wxyz',
    }
    slist = ['']
    for d in digits:
      xlist = []
      for s in slist:
        for t in d2s[d]:
          xlist.append(s + t)
      slist = xlist
    return slist



if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "", "0", "1", "14", "71", "23", "456"
  ]
  rslts = [solver.letterCombinations(digits) for digits in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")