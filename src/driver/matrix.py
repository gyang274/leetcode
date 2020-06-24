class Solution:
  def matmul(self, X, Y):
    # https://martin-thoma.com/matrix-multiplication-python-java-cpp/
    m, n, o = len(X), len(Y), len(Y[0])
    Z = [[0] * n for _ in range(n)]
    for i in range(m):
      for k in range(n):
        for j in range(o):
          Z[i][j] += X[i][k] * Y[k][j]
    return Z
  def power(self, X, p):
    if p == 0:
      return [[(i == j) & 1 for i in range(len(X))] for j in range(len(X))]
    elif p == 1:
      return X
    elif p == 2:
      return self.matmul(X, X)
    elif p == 3:
      return self.matmul(self.matmul(X, X), X)
    else:
      Y = self.power(X, p // 2)
      if p & 1 == 0:
        return self.matmul(Y, Y)
      else:
        return self.matmul(self.matmul(Y, Y), X)
  def matvec(self, X, y):
    # v = Xy
    return list(map(lambda x: sum(map(lambda xy: xy[0] * xy[1], zip(x, y))), X))
