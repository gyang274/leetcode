from collections import deque

class Solution:
  def numberOfSubstrings(self, s: str) -> int:
    n, count = len(s), 0
    z = [deque([]), deque([]), deque([])]
    for j, x in enumerate(s):
      z[ord(x) - ord('a')].append(j)
      if all(z):
        h = min(map(min, z))
        i = min(map(max, z))
        # s[i:(j+1)] as the core of "a..b..c" all once, extends on both side, h <-- i, .., j --> n
        count += (i - h + 1) * (n - j)
        for k in range(3):
          while z[k] and z[k][0] <= i:
            z[k].popleft()
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abc",
    "abcabc",
    "aabbcc",
    "acbbca",
  ]
  rslts = [solver.numberOfSubstrings(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
