from typing import List
import collections

class Poly(collections.Counter):
  def __add__(self, other):
    self.update(other)
    return self
  def __sub__(self, other):
    self.update({k: -v for k, v in other.items()})
    return self
  def __mul__(self, other):
    ans = Poly()
    for k1, v1 in self.items():
      for k2, v2 in other.items():
        ans.update({tuple(sorted(k1 + k2)): v1 * v2})
    return ans
  def evaluate(self, evalmap):
    ans = Poly()
    for k, c in self.items():
      free = []
      for token in k:
        if token in evalmap:
          c *= evalmap[token]
        else:
          free.append(token)
      ans[tuple(free)] += c
    return ans
  def to_list(self):
    return [ "*".join((str(v),) + k) for k, v in sorted(
      self.items(), key = lambda x: (-len(x[0]), x[0], x[1])
    ) if v]

class Solution(object):
  def basicCalculatorIV(self, expression, evalvars, evalints):
    evalmap = dict(zip(evalvars, evalints))
    def combine(left, right, symbol):
      if symbol == '+': return left + right
      if symbol == '-': return left - right
      if symbol == '*': return left * right
      raise
    def make(expr):
      ans = Poly()
      if expr.isdigit():
        ans.update({(): int(expr)})
      else:
        ans[(expr,)] += 1
      return ans
    def parse(expr):
      bucket = []
      symbols = []
      i = 0
      while i < len(expr):
        if expr[i] == '(':
          bal = 0
          for j in range(i, len(expr)):
            if expr[j] == '(': bal += 1
            if expr[j] == ')': bal -= 1
            if bal == 0: break
          bucket.append(parse(expr[i+1:j]))
          i = j
        elif expr[i].isalnum():
          for j in range(i, len(expr)):
            if expr[j] == ' ':
              bucket.append(make(expr[i:j]))
              break
          else:
            bucket.append(make(expr[i:]))
          i = j
        elif expr[i] in '+-*':
          symbols.append(expr[i])
        i += 1
      for i in range(len(symbols) - 1, -1, -1):
        if symbols[i] == '*':
          bucket[i] = combine(bucket[i], bucket.pop(i + 1), symbols.pop(i))
      if not bucket: return Poly()
      ans = bucket[0]
      for i, symbol in enumerate(symbols, 1):
        ans = combine(ans, bucket[i], symbol)
      return ans
    parsed = parse(expression).evaluate(evalmap)
    return parsed.to_list()

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("e + 8 - a + 5", ["e"], [1]),
    ("(e + 8) * (e - 8)", [], []),
    ("a * b * c + b * a * c * 4", ["a"], [2]),
    ("((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", [], []),
    ("((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c - a))", ["c"], [4]),
  ]
  rslts = [solver.basicCalculatorIV(expression, evalvars, evalints) for expression, evalvars, evalints in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}") 
