from config.listnode import ListNode, listToListNode

class Solution:
  def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    """Travel through listA and add an extra reverse link to its previous node, then travel through listB, 
      1st one has reverse link will be the intersection node.
    """
    node = ListNode('')
    node.next = headA
    while node is not None:
      hold = node.next
      if hold is not None:
        hold.prev = node
      node = hold
    node = ListNode('')
    node.next = headB
    while node is not None:
      # alternative: try-except,
      # or 'prev' in node.__dict__
      if hasattr(node, 'prev'):
        return node
      node = node.next
    return None