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
  def countVowelPermutation(self, n: int) -> int:
    # TC: O(logN), SC: O(1), transition matrix
    # T[i][j] = 1 if (a, e, i, o, u) -> (a, e, i, o, u) is ok
    T = [
      [0, 1, 0, 0, 0],
      [1, 0, 1, 0, 0],
      [1, 1, 0, 1, 1],
      [0, 0, 1, 0, 1],
      [1, 0, 0, 0, 0],
    ]
    # y = T^(n - 1)x
    return sum(self.matvec(self.power(T, n - 1), [1, 1, 1, 1, 1])) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.countVowelPermutation(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
