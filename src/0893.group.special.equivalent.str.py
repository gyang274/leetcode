from typing import List
from collections import Counter

class Solution:
  def numSpecialEquivGroups(self, A: List[str]) -> int:
    d, s = {}, set()
    for x in A:
      d[x] = (Counter(x[::2]), Counter(x[1::2]))
      for z in s:
        if d[x] == d[z]:
          break
      else:    
        s.add(x)
    return len(s)

class Solution:
  def numSpecialEquivGroups(self, A: List[str]) -> int:
    def count(A):
      ans = [0] * 52
      for i, letter in enumerate(A):
        ans[ord(letter) - ord('a') + 26 * (i % 2)] += 1
      return tuple(ans)
    return len({count(word) for word in A})

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["abc","acb","bac","bca","cab","cba"],
    ["abcd","cdab","cbad","xyzz","zzxy","zzyx"],
  ]
  rslts = [solver.numSpecialEquivGroups(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
