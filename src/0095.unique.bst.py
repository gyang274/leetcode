from config.treenode import TreeNode


class Solution:
  def generateTrees(self, n: int) -> List[TreeNode]:
    memo = {}
    memo[1] = TreeNode(1)
    return memo[0]


if __name__ == '__main__':  
  solver = Solution()
  cases = [
    0,
    1,
    2,
    3,
  ]
  rslts = [
    solver.generateTrees(n) for (n) in cases
  ]
  for cs, rs in zip(cases, rslts):
    print(f"case: {traverseListNode(cs[0])} + {traverseListNode(cs[1])} | solution: {traverseListNode(rs)}")