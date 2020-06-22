from typing import List

class Solution:
  def shortestToChar(self, S: str, C: str) -> List[int]:
    c = [i for i, x in enumerate(S) if x == C]
    ans, prev, nuxt, j = [0] * len(S), float('-inf'), c[0], 0
    for i, x in enumerate(S):
      if x == C:
        prev = nuxt
        j += 1
        if j < len(c):
          nuxt = c[j]
        else:
          nuxt = float('inf')
      else:
        ans[i] = min(i - prev, nuxt - i)
    return ans

class Solution:
  def shortestToChar(self, S: str, C: str) -> List[int]:
    ans = [0] * len(S)
    # dist from left
    prev = float('-inf')
    for i, x in enumerate(S):
      if x == C:
        prev = i
      else:
        ans[i] = i - prev
    # dist from right
    nuxt = float('inf')
    for i, x in reversed(list(enumerate(S))):
      if x == C:
        nuxt = i
      else:
        ans[i] = min(ans[i], nuxt - i)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("loveleetcode", "e"),
  ]
  rslts = [solver.shortestToChar(S, C) for S, C in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
