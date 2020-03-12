from typing import List

class Solution:
  def reverseString(self, s: List[str]) -> None:
    """Do not return anything, modify s in-place instead.
    """
    # say, built-in: s[::-1], s.reverse().
    n = len(s)
    for i in range(n // 2):
      s[i], s[n - 1 - i] = s[n - 1 - i], s[i]
    return None

if __name__ == '__main__':
  solver = Solution()
  cases = [
    list("leetcode"),
    list("hello world!"),
  ]
  rslts = [solver.reverseString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")