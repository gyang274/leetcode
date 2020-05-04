from typing import List
from collections import defaultdict

class DSU:
  def __init__(self, size):
    # representer
    self.reps = {i: i for i in range(size)}
  def find(self, x):
    while not x == self.reps[x]:
      x = self.reps[x]
    return x
  def union(self, x, y):
    self.reps[self.find(y)] = self.find(x)

class Solution:
  def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
    n = len(accounts)
    for i in range(n):
      accounts[i] = [accounts[i][0], set(accounts[i][1:])]
    dsu = DSU(n)
    for j in range(n):
      for i in range(j):
        if accounts[i][1] & accounts[j][1]:
          dsu.union(i, j)
    unified = defaultdict(lambda: [None, set([])])
    for k, v in dsu.reps.items():
      kk = dsu.find(v)
      unified[kk][0] = accounts[k][0]
      unified[kk][1] |= accounts[k][1]
    return [[account[0]] + sorted(account[1]) for k, account in unified.items()]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]],
    [["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]]
  ]
  rslts = [solver.accountsMerge(accounts) for accounts in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
