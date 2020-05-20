class Solution:
  def numTilings(self, N: int) -> int:
    """dp: [1, 0, 0, 0], num of tiles ende with _|X, X|X,  _|X, X|X,
                                                _|X, _|X , X|X, X|X,
      where | is the cut off index and X on left of | means not tiled properly.
    """
    M = 10 ** 9 + 7
    dp = [1, 0, 0, 0]
    for _ in range(N):
      ndp = [1, 0, 0, 0]
      ndp[0] = (dp[0] + dp[3]) % M
      ndp[1] = (dp[0] + dp[2]) % M
      ndp[2] = (dp[0] + dp[1]) % M
      ndp[3] = (dp[0] + dp[1] + dp[2]) % M
      dp = ndp
    return dp[0]

class Solution:
  def matmul(self, X, Y):
    # https://martin-thoma.com/matrix-multiplication-python-java-cpp/
    n = len(X)
    Z = [[0] * n for _ in range(n)]
    for i in range(n):
      for k in range(n):
        for j in range(n):
          Z[i][j] += X[i][k] * Y[k][j]
    for i in range(n):
      for j in range(n):
        Z[i][j] %= self.M
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
  def numTilings(self, N: int) -> int:
    self.M = 10 ** 9 + 7
    T = [
      [1, 0, 0, 1],
      [1, 0, 1, 0],
      [1, 1, 0, 0],
      [1, 1, 1, 0],
    ]
    return self.power(T, N)[0][0]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 23, 42, 85, 274,
  ]
  rslts = [solver.numTilings(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
