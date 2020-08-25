from config.listnode import ListNode, listToListNode
from collections import defaultdict, OrderedDict
from itertools import accumulate

class Solution:
  def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    # linked list -> array
    node, nums = head, []
    while node:
      nums.append(node.val)
      node = node.next
    # consecutive sum 0 <=> prefix sum seen
    prefix, seen, remove = list(accumulate(nums)), {}, set()
    for i, x in enumerate(prefix):
      if x == 0:
        for k in range(i + 1):
          remove.add(k)
      elif x in seen and seen[x] not in remove:
        for k in range(seen[x] + 1, i + 1):
          remove.add(k)
      else:
        seen[x] = i
    ans = [nums[i] for i in range(len(nums)) if i not in remove]
    # array -> linked list
    s = prev = ListNode('')
    for x in ans:
      curr = ListNode(x)
      prev.next = curr
      prev = curr
    return s.next

class Solution:
  def removeZeroSumSublists(self, head: ListNode) -> ListNode:
    # O(N), one pass, in-place
    # s: sentinel node
    s = node = ListNode(0)
    s.next = head
    # consecutive sum 0 <=> prefix sum seen
    prefix, seen = 0, OrderedDict()
    while node:
      prefix += node.val
      prev = seen.get(prefix, node)
      while prefix in seen:
        seen.popitem()
      seen[prefix] = prev
      prev.next = node.next
      node = node.next
    return s.next

if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [1,-1],
    [1,2,-3,3,1],
    [1,2,3,-3,4],
    [1,2,3,-3,-2],
    [2,3,-3,2,2,-2],
    [2,2,3,-2,-3,5,2,-2],
  ]
  cases = [
    listToListNode(l) for l in cases
  ]
  rslts = [
    solver.removeZeroSumSublists(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()} | solution: {rs.display() if rs else None}")
        