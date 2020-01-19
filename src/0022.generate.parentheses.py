from typing import List


# class Solution(object):
#   def generateParenthesis(self, n: int) -> List[str]:
#     if n == 0: return ['']
#     x = []
#     for k in range(n):
#       for xl in self.generateParenthesis(k):
#         for xr in self.generateParenthesis(n - 1 - k):
#           x.append('({}){}'.format(xl, xr))
#     return x


class Solution:
  def addParenthesis(self, x: List[str], s: str, nl: int, nr: int) -> List[str]:
    if nl == 0 and nr == 0:
      x.append(s)
      return None
    if nl > 0:
      self.addParenthesis(x, s + "(", nl - 1, nr + 1)
    if nr > 0:
      self.addParenthesis(x, s + ")", nl, nr - 1)
  def generateParenthesis(self, n: int) -> List[str]:
    x = []
    self.addParenthesis(x, "", n, 0)
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    3, 4, 5
  ]
  rslts = [solver.generateParenthesis(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")