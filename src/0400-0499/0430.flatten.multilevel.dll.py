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

class Solution:
  def flatten(self, head: 'Node') -> 'Node':
    if head:
      stack = [head, ]
      while stack:
        node = stack.pop()
        if node.next:
          stack.append(node.next)
        if node.child:
          stack.append(node.child)
          node.child = None
        if stack:
          node.next = stack[-1]
          stack[-1].prev = node
    return head

# []
# [1]
# [1,2,3]
# [1,2,null,3]
# [1,2,null,null,3]
# [1,2,null,null,3,null,4]