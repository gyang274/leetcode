class Solution:
  def isPalindrome(self, s: str) -> bool:
    alphanumeric = set('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    i, j = 0, len(s) - 1
    while i < j:
      while i < j and s[i].lower() not in alphanumeric:
        i += 1
      while j > i and s[j].lower() not in alphanumeric:
        j -= 1
      if s[i].lower() == s[j].lower():
        i += 1
        j -= 1
      else:
        return False
    return True

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "aba",
    "aabba",
    "aababa",
    "aabbaa",
    "0P",
    "race a car",
    "A man, a plan, a canal: Panama",
  ]
  rslts = [solver.isPalindrome(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")