from typing import List

class Solution:
  def restoreString(self, s: str, indices: List[int]) -> str:
    r = [''] * len(s)
    for i, k in enumerate(indices):
      r[k] = s[i]
    return ''.join(r)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("codeleet", [4,5,6,7,0,2,1,3]),
  ]
  rslts = [solver.restoreString(s, indices) for s, indices in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
