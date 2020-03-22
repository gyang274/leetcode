class Solution:
  def flatten(self, head: 'Node') -> 'Node':
    node = head
    while node:
      s = node.next
      if node.child:
        h = self.flatten(node.child)
        node.child = None
        node.next = h
        h.prev = node
        while h.next:
          h = h.next
        h.next = s
        if s:
          s.prev = h
      node = s
    return head

# []
# [1]
# [1,2,3]
# [1,2,null,3]
# [1,2,null,null,3]
# [1,2,null,null,3,null,4]