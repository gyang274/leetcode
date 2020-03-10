from collections import deque

class Solution:
  def isValidSerialization(self, preorder: str) -> bool:
    # empty
    if preorder == "":
      return False
    # verify preorder traversal of a tree
    xlist = deque(preorder.split(','))
    stack = deque([xlist.popleft(), ])
    while xlist or stack:
      # node
      if not stack:
        return False
      if not stack.popleft() == "#":  
        # node left child
        if not xlist:
          return False
        stack.append(xlist.popleft())
        # node right child
        if not xlist:
          return False
        stack.append(xlist.popleft())
    return True

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "#",
    "1,#",
    "1,#,#",
    "1,#,2",
    "1,#,#,2",
    "5,1,2,#,#,3,#,#,4,#,6,#,#",
  ]
  rslts = [solver.isValidSerialization(preorder) for preorder in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")