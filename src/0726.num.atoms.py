from collections import defaultdict

class Solution:
  def recursive(self, formula, n, i):
    atoms = defaultdict(lambda: 0)
    while i < n and not formula[i] == ")":
      if formula[i] == "(":
        d, i = self.recursive(formula, n, i + 1)
        x = ""
        while i < n and formula[i].isdigit():
          x += formula[i]
          i += 1
        if x:
          x = int(x)
          for k in d:
            atoms[k] += d[k] * x
      elif formula[i].isupper():
        s = formula[i]
        i += 1
        while i < n and formula[i].islower():
          s += formula[i]
          i += 1
        x = ""
        if i < n and formula[i].isdigit():
          while i < n and formula[i].isdigit():
            x += formula[i]
            i += 1
        x = x or 1
        atoms[s] += int(x)
    return atoms, i + 1
  def countOfAtoms(self, formula: str) -> str:
    atoms, _ = self.recursive(formula, len(formula), 0)
    return "".join([atom + (str(count) if count > 1 else "") for atom, count in sorted(atoms.items())]) 

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "H2O",
    "H2O2",
    "Mg(OH)2",
    "K4(ON(SO3)2)2",
  ]
  rslts = [solver.countOfAtoms(formula) for formula in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
