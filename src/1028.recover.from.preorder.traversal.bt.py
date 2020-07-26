from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recoverFromPreorder(self, S: str) -> TreeNode:
    stack, i, n, d, x = [], 0, len(S), 0, ''
    while i < n:
      while S[i] == '-':
        d += 1
        i += 1
      while i < n and S[i].isdigit():
        x += S[i]
        i += 1
      node = TreeNode(int(x))
      if d == 0:
        root = node
        stack.append((d, node))
      else:
        while stack and stack[-1][0] >= d:
          stack.pop()
        if not stack[-1][1].left:
          stack[-1][1].left = node
        else:
          stack[-1][1].right = node
          stack.pop()
        stack.append((d, node))
      d, x = 0, ''
    return root

class Solution:
  def recoverFromPreorder(self, S: str) -> TreeNode:
    stack, i = [], 0
    while i < len(S):
      d, x = 0, ''
      while i < len(S) and S[i] == '-':
        d += 1
        i += 1
      while i < len(S) and S[i] != '-':
        x += S[i]
        i += 1
      while len(stack) > d:
        stack.pop()
      node = TreeNode(x)
      if stack and stack[-1].left is None:
        stack[-1].left = node
      elif stack:
        stack[-1].right = node
      stack.append(node)
    return stack[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "1-2--3--4-5--6--7",
    "1-2--3---4-5--6---7",
    "1-401--349---90--88",
  ]
  rslts = [solver.recoverFromPreorder(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution:\n{rs.display() if rs else None}")
