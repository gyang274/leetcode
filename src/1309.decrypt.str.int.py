import string

class Solution:
  def freqAlphabets(self, s: str) -> str:
    n, i, r = len(s), 0, ''
    while i < n:
      if i + 2 < n and s[i + 2] == '#':
        r += string.ascii_lowercase[int(s[i:(i + 2)]) - 1]
        i += 3
      else:
        r += string.ascii_lowercase[int(s[i]) - 1]
        i += 1
    return r

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "2326",
    "2326#",
    "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#",
  ]
  rslts = [solver.freqAlphabets(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
