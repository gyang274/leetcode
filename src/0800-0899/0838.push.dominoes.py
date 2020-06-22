class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    d = list(dominoes)
    r, i, n = None, 0, len(d)
    for j in range(n):
      if d[j] == 'R':
        if r is not None:
          d[r:j] = ['R'] * (j - r)
        r = j
      elif d[j] == 'L':
        if r is not None:
          d[r:((r + j + 1) // 2)] = ['R'] * ((j - r + 1) // 2)
          d[((r + j + 2) // 2):(j + 1)] = ['L'] * ((j - r + 1) // 2)
          r = None
        else:
          d[i:(j + 1)] = ['L'] * (j + 1 - i)
        i = j + 1
    if r is not None:
      d[r:] = ['R'] * (n - r)
    return ''.join(d)

class Solution:
  def pushDominoes(self, dominoes: str) -> str:
    # ripple and reset the force
    d, n = list(dominoes), len(dominoes)
    # received force to right
    r, f = [0] * n, 0
    for i in range(n):
      if d[i] == 'R':
        f = n
      elif d[i] == 'L':
        f = 0
      else:
        f = max(f - 1, 0)
      r[i] = f
    # recived force to left
    l, f = [0] * n, 0
    for i in range(n - 1, -1, -1):
      if d[i] == 'L':
        f = -n
      elif d[i] == 'R':
        f = 0
      else:
        f = min(f + 1, 0)
      l[i] = f
    # accumulate the force from both side
    for i in range(n):
      f = r[i] + l[i]
      if f == 0:
        d[i] = '.'
      elif f > 0:
        d[i] = 'R'
      else:
        d[i] = 'L'
    return ''.join(d)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "R.",
    "RL",
    "RR.L",
    "R.R.L"
    ".L.R...LR..L..",
  ]
  rslts = [solver.pushDominoes(dominoes) for dominoes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
