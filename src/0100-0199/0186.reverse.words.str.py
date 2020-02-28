from typing import List

class Solution:
  def reverseWords(self, s: List[str]) -> None:
    """Do not return anything, modify s in-place instead.
      Two pass, reverse the list, reverse each word (separated by space) within list. Similar as 0151.
    """
    # reverse s
    l, r = 0, len(s) - 1
    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
    # reverse each word within s
    l, r = 0, 0
    while r < len(s):
      r += 1
      if r == len(s) or s[r] == ' ':
        i, j = l, r - 1
        while i < j:
          s[i], s[j] = s[j], s[i]
          i += 1
          j -= 1
        l = r + 1
    return None

class Solution:
  def reverse(self, s: List[str], l: int, r: int) -> None:
    """reverse s in-between l and r.
    """
    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1
  def reverseWords(self, s: List[str]) -> None:
    """Do not return anything, modify s in-place instead.
      Two pass, reverse the list, reverse each word (separated by space) within list. Similar as 0151.
    """
    # reverse s
    self.reverse(s, 0, len(s) - 1)
    # reverse each word within s
    l, r = 0, 0
    while r < len(s):
      r += 1
      if r == len(s) or s[r] == ' ':
        self.reverse(s, l, r - 1)
        l = r + 1
    return None

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [],
    [" "],
    list("the sky is blue"),
  ]
  rslts = [solver.reverseWords(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")