from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
  def recursive(self, x, y):
    for z, q in self.nodes[x]:
      self.path.append(q)
      if z not in self.visited:
        self.visited.add(z)
        if z == y or self.recursive(z, y):
          return True
      self.path.pop()
    return False
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """graph + DFS.
    """
    # construct undirected graph
    self.nodes = defaultdict(set)
    for (x, y), v in zip(equations, values):
      self.nodes[x].add((y,  v ))
      self.nodes[y].add((x, 1/v))
    # DFS for each query
    r = []
    for x, y in queries:
      if x in self.nodes and y in self.nodes:
        if x == y:
          r.append(1.0)
        else:
          self.path, self.visited = [], set([x])
          self.recursive(x, y)
          if self.path:
            r.append(reduce((lambda x, y: x * y), self.path))
          else:
            r.append(-1.0)
      else:
        r.append(-1.0)
    return r

class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """precompute all using Floyd–Warshall, advantage when queries repeatedly.
    """
    # construct undirected graph
    quot = defaultdict(dict)
    for (num, den), val in zip(equations, values):
      quot[num][num] = quot[den][den] = 1.0
      quot[num][den] = val
      quot[den][num] = 1 / val
    # Floyd–Warshall Algorithm
    for k, i, j in itertools.permutations(quot, 3):
      if k in quot[i] and j in quot[k]:
        quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]

class Solution:
  def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
    """precompute all using Floyd–Warshall, advantage when queries repeatedly.
    """
    # construct undirected graph
    quot = defaultdict(dict)
    for (num, den), val in zip(equations, values):
      quot[num][num] = quot[den][den] = 1.0
      quot[num][den] = val
      quot[den][num] = 1 / val
    # Floyd–Warshall Algorithm
    for k in quot:
      for i in quot[k]:
        for j in quot[k]:
          quot[i][j] = quot[i][k] * quot[k][j]
    return [quot[num].get(den, -1.0) for num, den in queries]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([["a","b"],["b","c"]], [2.0,3.0], [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]),
  ]
  rslts = [solver.calcEquation(equations, values, queries) for equations, values, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
