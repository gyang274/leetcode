class Solution:
  def maximum69Number (self, num: int) -> int:
    s = list(str(num))
    for i, x in enumerate(s):
      if x == '6':
        s[i] = '9'
        break
    return int(''.join(s))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "996",
  ]
  rslts = [solver.maximum69Number(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
