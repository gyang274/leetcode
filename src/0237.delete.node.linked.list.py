from config.listnode import ListNode, listToListNode

class Solution:
  def deleteNode(self, node: ListNode) -> None:
    """Do not return anything, modify node in-place instead.
      Key: O(N), move the value one by one while traverse from node to tail.
    """
    while node.next.next:
      node.val = node.next.val
      node = node.next
    node.val = node.next.val
    node.next = None

class Solution:
  def deleteNode(self, node: ListNode) -> None:
    """Do not return anything, modify node in-place instead.
      Key: O(1), move the value of node.next, and link from node to node.next.next.
      The key is since we don't have prev, we modify this node as prev and instead delete node.next as node.
    """
    node.val = node.next.val
    node.next = node.next.next