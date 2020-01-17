class Solution:
  def multiply(self, num1: str, num2: str) -> str:
    n1 = len(num1)
    n2 = len(num2)
    x = [0 for i in range(n1 + n2)]
    for i in range(n1 - 1, -1, -1):
      for j in range(n2 - 1, -1, -1):
        z = x[i + j + 1] + int(num1[i]) * int(num2[j])
        x[i + j + 1] = z % 10
        x[i + j] += z // 10
    while len(x) > 1 and x[0] == 0:
      x.pop(0)
    return "".join(map(str, x))


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("2", "3"),
    ("123", "456"),
    ("0", "0"),
    ("2", "3"),
    ("1", "1"),
    ("0", "1"),
    ("6752716719037375654442652725945722915786612669126862029212", "2840271321219335147"),
  ]
  rslts = [solver.multiply(num1, num2) for num1, num2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")