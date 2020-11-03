class TreeAncestor:

  def __init__(self, n: int, parent: List[int]):
    # keep a list of 1st, 2nd, 4th, 8th, .., (2^15)-th ancestor + binary search
    self.K = K = 16
    self.s = [[-1] * n for _ in range(K)]
    for j in range(n):
      self.s[0][j] = parent[j]
    for i in range(1, K):
      for j in range(0, n):
        if self.s[i - 1][j] > -1:
          self.s[i][j] = self.s[i - 1][self.s[i - 1][j]]
    
  def getKthAncestor(self, node: int, k: int) -> int:
    for i in range(self.K - 1, -1, -1):
      if k >= 1 << i:
        node = self.s[i][node]
        if node == -1:
          return -1
        k -= 1 << i
    return node
