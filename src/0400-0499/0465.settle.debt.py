from typing import List
from collections import defaultdict

class Solution:
  def recursive(self, debt, numT):
    x, amount = debt.popitem()
    while debt and amount == 0:
      x, amount = debt.popitem()
    if not debt:
      self.minNumT = min(numT, self.minNumT)
    else:
      # use sign to protect overflow
      sign = 1 if amount > 0 else -1
      for y in debt:
        if debt[y] * sign < 0:
          debt[y] += amount
          self.recursive(debt.copy(), numT + 1)
          debt[y] -= amount
  def minTransfers(self, transactions: List[List[int]]) -> int:
    # Equivalent to 3-partition problem, which is NP-Complete.
    # Settling Multiple Debts Efficiently: An Invitation to Computing Science by T. Verhoeff, June 2003.
    # Reference: http://www.mathmeth.com/tom/files/settling-debts.pdf
    debt = defaultdict(lambda: 0)
    for creditor, borrower, amount in transactions:
      debt[creditor] -= amount
      debt[borrower] += amount
    # simplified with if one creditor amount == another borrower amount, annihilation.
    numT, self.minNumT = 0, float('inf')
    parties, cleared = list(debt.keys()), set([])
    for i in range(len(parties)):
      if debt[parties[i]] == 0:
        cleared.add(parties[i])
      else:
        for j in range(i + 1, len(parties)):
          if debt[parties[i]] + debt[parties[j]] == 0:
            debt[parties[i]] = 0
            debt[parties[j]] = 0
            cleared.add(parties[i])
            cleared.add(parties[j])
            numT += 1
            break
    for party in cleared:
      debt.pop(party)
    # recursive over all pay methods, as NP-complete.
    if debt:
      self.recursive(debt, numT)
    else:
      self.minNumT = numT
    return self.minNumT

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [[0,1,10], [2,0,5]],
    [[0,1,10], [1,0,1], [1,2,5], [2,0,5]],
    [[0,1,10], [2,3,4], [3,4,5], [4,5,6], [5,6,3]],
  ]
  rslts = [solver.minTransfers(transactions) for transactions in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")