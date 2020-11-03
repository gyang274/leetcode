class Solution:
  def reformat(self, s: str) -> str:
    # split
    alpha, numeric = [], []
    for x in s:
      if x.isalpha():
        alpha.append(x)
      else:
        numeric.append(x)
    # build
    if len(alpha) == len(numeric):
      return ''.join(''.join([x, y]) for x, y in zip(alpha, numeric))
    elif len(alpha) == len(numeric) - 1:
      alpha += ['']
      return ''.join(''.join([x, y]) for x, y in zip(numeric, alpha))
    elif len(alpha) == len(numeric) + 1:
      numeric += ['']
      return ''.join(''.join([x, y]) for x, y in zip(alpha, numeric))
    else:
      return ""

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "ab123",
    "a0b1c2",
    "alpha2019",
  ]
  rslts = [solver.reformat(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
