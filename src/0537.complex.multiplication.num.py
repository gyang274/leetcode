class Solution:
  def complexNumberMultiply(self, a: str, b: str) -> str:
    ar, ai = a.split("+")
    ar, ai = int(ar), int(ai[:-1])
    br, bi = b.split("+")
    br, bi = int(br), int(bi[:-1])
    return str(ar * br - ai * bi) + "+" + str(ar * bi + ai * br) + "i"

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("1+1i", "1+1i"),
    ("1+1i", "1+-1i"),
    ("1+-1i", "1+-1i"),
  ]
  rslts = [solver.complexNumberMultiply(a, b) for a, b in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
