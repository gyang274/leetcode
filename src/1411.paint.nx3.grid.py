class Solution:
  def matmul(self, X, Y):
    # https://martin-thoma.com/matrix-multiplication-python-java-cpp/
    n = len(X)
    Z = [[0] * n for _ in range(n)]
    for i in range(n):
      for k in range(n):
        for j in range(n):
          Z[i][j] += X[i][k] * Y[k][j]
    return Z
  def power(self, X, p):
    if p == 0:
      return [[(i == j) & 1 for i in len(X)] for j in len(X)]
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
  def numOfWays(self, n: int) -> int:
    """Q0552
      Let x(n) = [k2, k3] count the num of paints with n-grids and last grid using 2-colors or 3-colors.
      T: transition matrix from x(n) to x(n + 1), X is not compatible, V is compatible
      (1 2 1) -> (1 2 1) X, (1 3 1) X, (2 1 2) V, (2 3 2) V, (3 1 3) V, (3 2 3) X => T[0][0] = 3
      (1 2 1) -> (1 2 3) X, (1 3 2) X, (2 1 3) V, (2 3 1) X, (3 1 2) V, (3 2 1) X => T[0][1] = 2
      (1 2 3) -> (1 2 1) X, (1 3 1) X, (2 1 2) V, (2 3 2) V, (3 1 3) X, (3 2 3) X => T[0][0] = 2
      (1 2 3) -> (1 2 3) X, (1 3 2) X, (2 1 3) X, (2 3 1) V, (3 1 2) V, (3 2 1) X => T[1][1] = 2
      T = [
        [3, 2],
        [2, 2],
      ]
    """
    x = [6, 6]
    if n == 1:
      return sum(x)
    T = [
      [3, 2],
      [2, 2],
    ]
    T = self.power(T, n - 1)
    # x = self.multiplyTx(T, x)
    # return sum(x) % (10 ** 9 + 7)
    return ((sum(T[0]) + sum(T[1])) * 6) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 42, 85,
  ]
  rslts = [solver.numOfWays(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")