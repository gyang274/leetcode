class Solution:
  def toLowerCase(self, str: str) -> str:
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower = "abcdefghijklmnopqrstuvwxyz"
    h = dict(zip(upper, lower))
    return ''.join([h[x] if x in upper else x for x in str])