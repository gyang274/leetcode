from config.treenode import TreeNode, listToTreeNode

class Solution:
  def recursive(self, i):
    if i == self.n:
      return None, self.n
    v = ""
    while i < self.n and not (self.s[i] == "(" or self.s[i] == ")"):
      v += self.s[i]
      i += 1
    node = TreeNode(int(v))
    if i < self.n and self.s[i] == "(":
      node.left, i = self.recursive(i + 1)
      if i < self.n and self.s[i] == "(":
        node.right, i = self.recursive(i + 1)
        if i < self.n and self.s[i] == ")":
          i += 1
      elif i < self.n and self.s[i] == ")":
          i += 1
    elif i < self.n and self.s[i] == ")":
      i += 1
    return node, i
  def str2tree(self, s: str) -> TreeNode:
    self.s, self.n = s, len(s)
    return self.recursive(0)[0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "4(2(3)(1))(6(5))",
    "1(2(3(4(5(6(7(8)))))))(9(10(11(12(13(14(15)))))))",
    "345(846(921(756(641(667)(251)))(83(675(840))(794(983))))(489(545(949(443))(433(962)(515)))(569(420(864)(892)))))",
  ]
  rslts = [solver.str2tree(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution:\n{rs.display() if rs else None}")