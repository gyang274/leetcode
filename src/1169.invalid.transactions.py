from typing import List
from collections import defaultdict, deque

class Solution:
  def invalidTransactions(self, transactions: List[str]) -> List[str]:
    # ts: transactions: (time, name, city, amount, index), sorted by time
    ts = sorted(
      map(
        lambda ix: (int(ix[1][1]), ix[1][0], ix[1][3], int(ix[1][2]), ix[0]),
        map(
          lambda ix: (ix[0], ix[1].split(',')), enumerate(transactions)
        )
      )
    )
    # us: user -> lastest transactions (time, name, city, amount, index)
    us, ans = defaultdict(deque), set()
    for t in ts:
      while us[t[1]] and t[0] - us[t[1]][0][0] > 60:
        us[t[1]].popleft()
      for s in us[t[1]]:
        if s[2] != t[2]:
          ans.add(transactions[s[4]])
          ans.add(transactions[t[4]])
      if t[3] > 1000:
        ans.add(transactions[t[4]])
      us[t[1]].append(t)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["alice,20,800,mtv","alice,40,1200,mtv","alice,50,100,beijing","alice,90,100,shanghai"],
  ]
  rslts = [solver.invalidTransactions(transactions) for transactions in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
