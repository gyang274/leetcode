from typing import List

class Solution:
  def recursive(self, s, i, j, p):
    """recursive remove anyone of closing ende parathesis, e.g., ')' in original order, and '(' in reverse order,
      whenever the number of closing ende parathesis is greater than the opening init parathesis.
    Args
      s: current str
      i: index of prev ende
      j: index of next init, when found invalid start from ende after i to make it valid and recursive
      p: parathesis pair "()" when parsing origin order to remove invalid ")" or ")(" when parsing reverse to remove "("
    """
    counter = 0
    while j < len(s):
      if s[j] == p[0]:
        counter += 1
      elif s[j] == p[1]:
        counter -= 1
      if counter < 0:
        # found an invalid, remove any p[1] before, remove the first one of a consecutive sequence.
        for k in range(i, j + 1):
          if s[k] == p[1] and (k == i or not s[k - 1] == p[1]):
            self.recursive(s[:k] + s[(k + 1):], k, j, p)
        return None
      j += 1
    # this order is valid
    r = s[::-1]
    if p[0] == "(":
      # need also make reverse order valid
      self.recursive(r, 0, 0, p[::-1])
    else:
      # both original and reverse order are valid
      self.ans.append(r)
  def removeInvalidParentheses(self, s: str) -> List[str]:
    self.ans = []
    self.recursive(s, 0, 0, "()")
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "(",
    ")",
    "()",
    "(()",
    "())",
    "()())()",
    "(a)())()",
    "())()))((",
  ]
  rslts = [solver.removeInvalidParentheses(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")