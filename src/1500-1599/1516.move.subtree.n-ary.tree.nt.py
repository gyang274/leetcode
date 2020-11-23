"""
# Definition for a Node.
class Node:
  def __init__(self, val=None, children=None):
    self.val = val
    self.children = children if children is not None else []
"""

from collections import deque

class Solution:
  def moveSubTree(self, root: 'Node', p: 'Node', q: 'Node') -> 'Node':
    def scanTree():
      r_queue, p_queue = deque(), deque() 
      if root == p: 
        p_queue.append(root) 
      else: 
        r_queue.append(root)
      p_index, q_index, p_parent, q_parent, isQInP = -1, -1, None, None, False
      notFound = (p != root) + (q != root)
      while notFound:
        if p_queue:
          node = p_queue.popleft()
          for i, child in enumerate(node.children):
            if child == q:
              notFound -= 1
              q_parent, q_index = node, i
              isQInP = True
            p_queue.append(child)
        if r_queue:
          node = r_queue.popleft()
          for i, child in enumerate(node.children):
            if child == p:
              notFound -= 1
              p_parent, p_index = node, i
            if child == q:
              notFound -= 1
              q_parent, q_index = node, i
            if child == p:
              p_queue.append(child)
            else:
              r_queue.append(child)
      return (p_parent, p_index, q_parent, q_index, isQInP)                
    p_parent, p_index, q_parent, q_index, isQInP = scanTree()
    if p_parent == q: return root
    if (p_parent): p_parent.children.pop(p_index) 
    if isQInP:
      q_parent.children.pop(q_index) 
      if (p_parent): p_parent.children.insert(p_index, q) 
    q.children.append(p)        
    return root if root != p else q
