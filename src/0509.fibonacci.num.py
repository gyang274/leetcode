class Solution:
  def __init__(self):
    self.memo = {}
    self.memo[0] = 0
    self.memo[1] = 1
    
  def fib(self, N: int) -> int:
    if N > 1 and N not in self.memo:
      self.memo[N] = self.fib(N - 1) + self.fib(N - 2)
    return self.memo[N]

class Solution:
  def fib(self, N: int) -> int:
    if N == 0:
      return 0
    if N == 1:
      return 1
    x = [None] * (N + 1)
    x[0] = 0
    x[1] = 1
    for i in range(2, N + 1):
      x[i] = x[i - 1] + x[i - 2]
    return x[N]

class Solution:
  """TC: O(logN), SC: O(logN), [[F_{N+1}, F_N], [F_N, F_{N-1}]] = [[1 1], [1, 0]] ^ N
  """
  def fib(self, N: int) -> int:
    if (N <= 1):
      return N
    A = [[1, 1], [1, 0]]
    self.matrix_power(A, N-1)
    return A[0][0]

  def matrix_power(self, A: list, N: int):
    if (N <= 1):
      return A
    self.matrix_power(A, N//2)
    self.multiply(A, A)
    B = [[1, 1], [1, 0]]
    if (N%2 != 0):
      self.multiply(A, B)

  def multiply(self, A: list, B: list):
    x = A[0][0] * B[0][0] + A[0][1] * B[1][0]
    y = A[0][0] * B[0][1] + A[0][1] * B[1][1]
    z = A[1][0] * B[0][0] + A[1][1] * B[1][0]
    w = A[1][0] * B[0][1] + A[1][1] * B[1][1]
    A[0][0] = x
    A[0][1] = y
    A[1][0] = z
    A[1][1] = w

class Solution:
  """TC: O(1), SC: O(1), math.
  """
  def fib(self, N: int) -> int:
  	return int(((((1 + 5 ** 0.5) / 2) ** N - ((1 - 5 ** 0.5) / 2) ** N)) / (5 ** 0.5))