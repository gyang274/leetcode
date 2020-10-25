from collections import deque

class Solution:
  def maxVowels(self, s: str, k: int) -> int:
    vowels, q, m = set('aeiou'), deque([]), 0
    for i, x in enumerate(s):
      while q and i - q[0] >= k:
        q.popleft()
      if x in vowels:
        q.append(i)
      m = max(m, len(q))
    return m

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("leetcode", 2),
    ("leetcode", 3),
    ("leetcode", 5),
  ]
  rslts = [solver.maxVowels(s, k) for s, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
