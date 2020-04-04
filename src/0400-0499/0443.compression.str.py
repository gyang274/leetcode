from typing import List

class Solution:
  def compress(self, chars: List[str]) -> int:
    i, j, k, n = 0, 0, 0, len(chars)
    while j <= n:
      if j == n or not chars[j] == chars[i]:
        if k < n:
          chars[k] = chars[i]
          k += 1
        if j - i > 1:
          for ij in str(j - i):
            chars[k] = ij
            k += 1
        i = j
      j += 1
    return k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [],
    ["a"],
    ["a","a","a","a","b","b","c","c","c"],
  ]
  rslts = [solver.compress(chars) for chars in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
