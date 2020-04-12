class Solution:
  def checkRecord(self, n: int) -> int:
    # x: count of attendance by A and ends of P/L
    # x[0]: C(A0, P): count without A, ended with P
    # x[1]: C(A0, PL): count without A, ended with PL
    # x[2]: C(A0, LL): count without A, ended with LL
    # x[3]: C(A1, X): count with one A, ended with X = P or A
    # x[4]: C(A1, XL): count with one A, ended with XL = PL or AL
    # x[5]: C(A1, LL): count with one A, ended with LL
    x = [1, 1, 0, 1, 0, 0]
    if n == 1:
      return sum(x)
    for _ in range(2, n + 1):
      # transition from n to n + 1
      y = [None] * 6
      y[0] = x[0] + x[1] + x[2]
      y[1] = x[0]
      y[2] = x[1]
      y[3] = sum(x)
      y[4] = x[3]
      y[5] = x[4]
      x = y
    return sum(x) % (10 ** 9 + 7)

class Solution:
  def calculateXY(self, X, Y):
    """calculate matrix multiplication: Z = X * Y
    """
    Z = [[0] * 6 for _ in range(6)]
    for i in range(6):
      for j in range(6):
        for k in range(6):
          Z[i][j] += X[i][k] * Y[k][j]
    return Z
  def calculateTp(self, T, p):
    """calculate matrix power: T^p
    """
    if p == 1:
      return T
    # recursive the power calculate so O(logK)
    if p // 2 == 1:
      # deep copy of T
      X = [T[i][:] for i in range(6)]
    else:
      X = self.calculateTp(T, p // 2)
    X = self.calculateXY(X, X)
    if p & 1 == 0:
      return X
    else:
      return self.calculateXY(X, T)
  def calculateTx(self, T, x):
    """calculate Tx
    """
    y = [0] * 6
    for i in range(6):
      for k in range(6):
        y[i] += T[i][k] * x[k]
    return y
  def checkRecord(self, n: int) -> int:
    # x: count of attendance by A and ends of P/L
    # x[0]: C(A0, P): count without A, ended with P
    # x[1]: C(A0, PL): count without A, ended with PL
    # x[2]: C(A0, LL): count without A, ended with LL
    # x[3]: C(A1, X): count with one A, ended with X = P or A
    # x[4]: C(A1, XL): count with one A, ended with XL = PL or AL
    # x[5]: C(A1, LL): count with one A, ended with LL
    x = [1, 1, 0, 1, 0, 0]
    if n == 1:
      return sum(x)
    # T: transition matrix from n to n + 1
    T = [
      [1, 1, 1, 0, 0, 0],
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 0, 0, 0],
      [1, 1, 1, 1, 1, 1],
      [0, 0, 0, 1, 0, 0],
      [0, 0, 0, 0, 1, 0],
    ]
    # y = T^(n - 1) x, if n > 1
    T = self.calculateTp(T, n - 1)
    y = self.calculateTx(T, x)
    return sum(y) % (10 ** 9 + 7)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 42, 85,
  ]
  rslts = [solver.checkRecord(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
