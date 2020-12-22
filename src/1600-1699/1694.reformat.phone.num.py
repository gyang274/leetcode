class Solution:
  def reformatNumber(self, number: str) -> str:
    r, s = '', ''
    for x in number:
      if x.isdigit():
        s += x
        if len(s) == 3:
          r += '-' + s
          s = ''
    if s:
      if len(s) == 1:
        r = r[:-1] + '-' + r[-1] + s
      else:
        r += '-' + s
    return r[1:]