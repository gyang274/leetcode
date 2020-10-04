from typing import List

class Solution:
  def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    # root
    l, r = leftChild, rightChild
    s = set(range(n)) - set(l + r)
    if len(s) != 1:
      return False
    # bfs
    q = list(s)
    while q:
      x = q.pop()
      for y in [l[x], r[x]]:
        if y > -1:
          if y in s:
            return False
          s.add(y)
          q.append(y)
    return len(s) == n

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (2, [1,0], [-1,-1]),
    (4, [1,-1,3,-1], [2,-1,-1,-1]),
    (4, [1,-1,3,-1], [2, 3,-1,-1]),
    (4, [1,0,3,-1], [-1,-1,-1,-1]),
  ]
  rslts = [solver.validateBinaryTreeNodes(n, leftChild, rightChild) for n, leftChild, rightChild in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
