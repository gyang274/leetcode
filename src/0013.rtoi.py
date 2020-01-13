class Solution:
  def romanToInt(self, s: str) -> int:
    r2i = {
      "I": 1,
      "V": 5,
      "X": 10,
      "L": 50,
      "C": 100,
      "D": 500,
      "M": 1000,
      "IV": 4,
      "IX": 9,
      "XL": 40,
      "XC": 90,
      "CD": 400,
      "CM": 900, 
    }
    i = 0
    l = len(s)
    x = 0
    while i < l:
      if i + 1 < l and s[i:(i + 2)] in r2i:
        x += r2i[s[i:(i+2)]]
        i += 2
      else:
        x += r2i[s[i]]
        i += 1
    return x


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    "III",
    "IV",
    "IX",
    "LVIII",
  ]
  rslts = [
    solver.romanToInt(s) for s in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")