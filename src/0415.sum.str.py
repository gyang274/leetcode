class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    n1, n2 = len(num1), len(num2)
    if n1 < n2:
      n1, num1, n2, num2 = n2, num2, n1, num1
    i, k, x = -1, 0, ""
    while i > -(n1 + 1):
      if i > -(n2 + 1):
        s = int(num1[i]) + int(num2[i]) + k
      else:
        s = int(num1[i]) + k
      x = str(s % 10) + x
      k = s // 10
      i -= 1
    if k > 0:
      x = str(k) + x
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0", "0"),
    ("9", "1"),
    ("1123", "429785"),
  ]
  rslts = [solver.addStrings(num1, num2) for num1, num2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")