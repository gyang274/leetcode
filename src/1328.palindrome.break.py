class Solution:
  def breakPalindrome(self, palindrome: str) -> str:
    n = len(palindrome)
    if n == 1:
      return ''
    for i in range(n // 2):
      if not palindrome[i] == 'a':
        return palindrome[:i] + 'a' + palindrome[(i + 1):]
    return palindrome[:-1] + 'b'

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "a",
    "b",
    "aaa",
    "aba",
    "aaaa",
    "aabaa",
    "abccba",
  ]
  rslts = [solver.breakPalindrome(palindrome) for palindrome in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
