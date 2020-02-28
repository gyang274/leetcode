import heapq
# from queue import PriorityQueue
from typing import List
from config.listnode import ListNode, listToListNode, traverseListNode


class Solution:
  def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    k = len(lists)
    h = [l for l in lists if l]
    heapq.heapify(h)
    s = ListNode(0)
    x = s
    while h:
      v = heapq.heappop(h)
      x.next = v
      x = x.next
      if v.next:
        heapq.heappush(h, v.next)
    return s.next

# class Solution:
#   def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#     """Without define `<` in singly-linked list class. 
#     """
#     k = len(lists)
#     h = [(l.val, i) for i, l in enumerate(lists) if l]
#     heapq.heapify(h)
#     s = ListNode(0)
#     x = s
#     while h:
#       v, i = heapq.heappop(h)
#       x.next = ListNode(v)
#       x = x.next
#       if lists[i].next:
#         lists[i] = lists[i].next
#         heapq.heappush(h, (lists[i].val, i))
#     return s.next

# class Solution:
#   def mergeKLists(self, lists: List[ListNode]) -> ListNode:
#     k = len(lists)
#     q = PriorityQueue()
#     for l in lists:
#       if l:
#         q.put((l.val, l))
#     s = ListNode(0)
#     x = s
#     while q:
#       val, v = q.get()
#       if v.next:
#         q.put((v.next.val, v))
#       x.next = v
#       x = x.next
#     return s.next


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [[1,4,5],[1,3,4],[2,6]],
    [[1,4,5],[1,3,4],[2,6],[4]],
    [[1,4,5],[1,3,4],[2,6],[]],
  ]
  cases = [
    [listToListNode(y) for y in x] for x in cases
  ]
  rslts = [
    solver.mergeKLists(lists) for lists in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {traverseListNode(rs)}")