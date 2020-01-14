from typing import List


class Solution:
  def longestCommonPrefix(self, strs: List[str]) -> str:
    i = 0
    for z in zip(*strs):
      if (len(set(z))) == 1:
        i += 1
      else:
        break
    return strs[0][:i] if i > 0 else ''
     

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ["flower", "flow", "flight"],
    ["flower", "flow"],
    ["dog", "racecar", "car"],
    []
  ]
  rslts = [solver.longestCommonPrefix(x) for x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")