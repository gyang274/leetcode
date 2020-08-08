from typing import List

class Solution:
  def braceExpansionII(self, expression: str) -> List[str]:
    stack, union, prods = [], [], ['']
    for x in expression:
      if x.isalpha():
        prods = [z + x for z in prods]
      elif x == '{':
        stack.append((union, prods))
        union, prods = [], ['']
      elif x == '}':
        prevUnion, prevProds = stack.pop()
        prods = [z + y for y in union + prods for z in prevProds]
        union = prevUnion
      else:
        union += prods
        prods = ['']
    return sorted(set(union + prods))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "{a,b}{c,{d,e}}",
    "{{a,z},a{b,c},{ab,z}}",
    "{{a,z},a{b,c},{a,b}{c,{d,e}},{ab,z}}",
  ]
  rslts = [solver.braceExpansionII(expression) for expression in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
