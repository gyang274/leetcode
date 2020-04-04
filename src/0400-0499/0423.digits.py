from collections import Counter, OrderedDict

class Solution:
  def __init__(self):
    self.xs = OrderedDict({
      0: ("z", "zero"),
      2: ("w", "two"),
      4: ("u", "four"),
      5: ("f", "five"),
      6: ("x", "six"),
      7: ("s", "seven"),
      8: ("g", "eight"),
      9: ("i", "nine"),
      1: ("o", "one"),
      3: ("t", "three"),
    })
    
  def originalDigits(self, s: str) -> str:
    x, cntr = [0] * 10, Counter(s)
    for dx, (ix, ds) in self.xs.items():
      if ix in cntr:
        nx = cntr[ix]
        for k in list(ds):
          cntr[k] -= nx
          if cntr[k] == 0:
            cntr.pop(k)
        x[dx] = nx
    return "".join([str(dx) * nx for dx, nx in enumerate(x)])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "zeroonetwothreefourfivesixseveneightnine",
  ]
  rslts = [solver.originalDigits(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
