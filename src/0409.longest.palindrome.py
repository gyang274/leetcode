from collections import Counter

class Solution:
  def longestPalindrome(self, s: str) -> int:
    n, sc = 0, Counter(s)
    for _, ns in sc.items():
      n += ns
      if not n & 1 and ns & 1:
        n -= 1
    return n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "", "a", "aaAAA"
  ]
  rslts = [solver.longestPalindrome(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")