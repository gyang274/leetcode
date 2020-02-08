from typing import List
from config.listnode import ListNode, listToListNode
from config.treenode import TreeNode, listToTreeNode


class Solution:
  def getLength(self, head: ListNode) -> int:
    s, node = 0, head
    while node:
      node = node.next
      s += 1
    return s
  def simulateInorderTraversal(self, l, r) -> TreeNode:
    if l == r - 1:
      node = TreeNode(self.head.val)
      self.head = self.head.next
      return node
    m = (l + r) // 2
    if m > l:
      hold = self.simulateInorderTraversal(l, m)
    node = TreeNode(self.head.val)
    self.head = self.head.next
    node.left = hold
    if m < r - 1:
      node.right = self.simulateInorderTraversal(m + 1, r)
    return node
  def sortedListToBST(self, head: ListNode) -> TreeNode:
    """Algorithms:
      1. Convert to sorted array + recursion: Time Complexity O(N), Space Complexity O(N).
      2. Two pointer find middle + recursion: Time Complexity O(NlogN), Space Complexity O(logN).
      3. Direct conversion via simulation of inorder travel: Time Complexity O(N), Space Complexity O(logN).
    """
    if not head:
      return None
    size = self.getLength(head)
    self.head = head
    return self.simulateInorderTraversal(0, size)


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 2, 3, 4],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5, 6, 7, 8],
  ]
  cases = [
    (listToListNode(x)) for x in cases
  ]
  rslts = [
    solver.sortedListToBST(head) for head in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs.display()}, solution:\n{rs.display()}")