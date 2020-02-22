class Solution:
  def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    """at each position, keep track length of 1 distinct and length of 2 distinct.
      dynamic programming with memoryless so kind of status machine.
    """
    char1, char2, ln1, ln2, lnX = '', '', 0, 0, 0
    for x in s:
      if x == char2:
        ln1 += 1
        ln2 += 1
        lnX = max(lnX, ln2)
      elif x == char1:
        ln1 = 1
        ln2 += 1
        lnX = max(lnX, ln2)
        char1, char2 = char2, x
      else:
        ln2 = ln1 + 1
        ln1 = 1
        lnX = max(lnX, ln2)
        char1, char2 = char2, x
    return lnX

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    "",
    "a",
    "ab",
    "aab",
    "abac",
    "abcdc",
    "aabcbccc",
  ]
  rslts = [solver.lengthOfLongestSubstringTwoDistinct(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")