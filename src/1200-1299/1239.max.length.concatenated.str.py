from typing import List

class Solution:
  def maxLength(self, arr: List[str]) -> int:
    z = [set()]
    for a in arr:
      if len(set(a)) < len(a):
        continue
      a = set(a)
      z += [x | a for x in z if not x & a]
    return max(len(x) for x in z)

class Solution:
  def maxLength(self, arr: List[str]) -> int:
    # hash str to integer
    def hash(s):
      h, k = 0, 0
      for x in s:
        i = 1 << (ord(x) - ord('a'))
        if h & i:
          return 0, 0
        h |= i
        k += 1
      return h, k
    z = set([(0, 0)])
    for h, k in map(hash, arr):
      if h:
        z |= {(x | h, y + k) for x, y in z if h & x == 0}
    return max(k for h, k in z)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["un","iq","ue"],
    ["cha","r","act","ers"],
    ["yy","bkhwmpbiisbldzknpm"],
    ["abcdefghijklmnopqrstuvwxyz"],
  ]
  rslts = [solver.maxLength(arr) for arr in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
