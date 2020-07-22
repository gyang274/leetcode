class Solution:
  def smallestRepunitDivByK(self, K: int) -> int:
    if K == 1:
      return 1
    if (K & 1) ^ 1:
      return -1
    s, r, i = 1, 1, 1
    seen = set()
    while s and (s, r) not in seen:
      seen.add((s, r))
      r = (r * 10) % K
      s = (s + r) % K
      i += 1
      if not s:
        return i
    return -1

class Solution:
  def smallestRepunitDivByK(self, K: int) -> int:
    # pigeon hole
    if K % 2 == 0 or K % 5 == 0:
      return -1
    r = 0
    for x in range(1, K + 1):
      r = (r * 10 + 1) % K
      if not r:
        return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 7, 11, 13, 17,
  ]
  rslts = [solver.smallestRepunitDivByK(K) for K in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
