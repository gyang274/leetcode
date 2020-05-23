from typing import List
from config.listnode import ListNode, listToListNode

class Solution:
  def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
    i, d, node = 0, {}, root
    while node:
      d[i] = node
      node = node.next
      i += 1
    ans = []
    if i <= k:
      for j in range(i):
        ans.append(d[j])
        d[j].next = None
      for j in range(i, k):
        ans.append(None)
    else:
      q, r = i // k, i % k
      for j in range(k):
        if j < r:
          ans.append(d[q * j + j])
          d[q * (j + 1) + (j + 1) - 1].next = None
        else:
          ans.append(d[q * j + r])
          d[min(q * (j + 1) + r - 1, i - 1)].next = None
    return ans

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    ([1, 2, 3], 2),
    ([1, 2, 3], 3),
    ([1, 2, 3], 5),
  ]
  cases = [
    (listToListNode(l), k) for l, k in cases
  ]
  rslts = [
    solver.splitListToParts(l, k) for (l, k) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs[0].display()} + {cs[1:]} | solution: {[rsi.display() if rsi else None for rsi in rs]}")
