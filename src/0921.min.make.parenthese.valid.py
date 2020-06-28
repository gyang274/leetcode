class Solution:
  def minAddToMakeValid(self, S: str) -> int:
    ans = bal = 0
    for x in S:
      if x == '(':
        bal += 1
      else:
        bal -= 1
      if bal < 0:
        ans += 1
        bal = 0
    return ans + bal