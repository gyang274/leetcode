class Solution:
  def __init__(self):
    self.n1 = {
      0: "Zero",
      1: "One",
      2: "Two",
      3: "Three",
      4: "Four",
      5: "Five",
      6: "Six",
      7: "Seven",
      8: "Eight",
      9: "Nine",
      10: "Ten",
      11: "Eleven",
      12: "Twelve",
      13: "Thirteen",
      14: "Fourteen",
      15: "Fifteen",
      16: "Sixteen",
      17: "Seventeen",
      18: "Eighteen",
      19: "Nineteen",
    }
    self.n2 = {
      20: "Twenty",
      30: "Thirty",
      40: "Forty",
      50: "Fifty",
      60: "Sixty",
      70: "Seventy",
      80: "Eighty",
      90: "Ninety",
    }
    self.nn = [
      "", "Thousand", "Million", "Billion"
    ]
  def _numberToWordsWithinComma(self, num):
    s = ""
    # _x_ xx
    if num > 99:
      s += str(self.n1[num // 100]) + " " + "Hundred" + " "
      num %= 100
    # x _xx_
    if num > 19:
      s += self.n2[num // 10 * 10] + " "
      num %= 10
    # xx _x_
    if num > 0:
      s += self.n1[num]
      return s
    elif s:
      return s[:-1]
    else:
      # `zero million, or zero thousand`
      return s
  def numberToWords(self, num: int) -> str:
    if num == 0:
      return self.n1[num]
    i, s = 0, ""
    while num:
      # si: one part of xxx between commas
      si = self._numberToWordsWithinComma(num % 1000)
      if not si == "":
        if i > 0:
          si += " " + self.nn[i]
        s = si if s == "" else (si + " " + s)
      num //= 1000
      i += 1
    return s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 4, 5, 8, 12, 17, 48, 85, 520, 1000, 5374, 6922, 857142, 3000150, 1234567890,
  ]
  rslts = [solver.numberToWords(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: '{rs}'")