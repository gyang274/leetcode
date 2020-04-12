def matmul(X, Y):
  # https://martin-thoma.com/matrix-multiplication-python-java-cpp/
  n = len(X)
  Z = [[0] * n for _ in range(n)]
  for i in range(n):
    for k in range(n):
      for j in range(n):
        Z[i][j] += X[i][k] * Y[k][j]
  return Z

def power(X, p):
  if p == 0:
    return [[(i == j) & 1 for i in len(X)] for j in len(X)]
  elif p == 1:
    return X
  elif p == 2:
    return matmul(X, X)
  elif p == 3:
    return matmul(matmul(X, X), X)
  else:
    Y = power(X, p // 2)
    if p & 1 == 0:
      return matmul(Y, Y)
    else:
      return matmul(matmul(Y, Y), X)
