from typing import List

class Solution:
  def minDeletionSize(self, A: List[str]) -> int:
    if len(A) == 1:
      return 0
    rows, count = list(range(len(A))), 0
    rows = list(zip(rows[:-1], rows[1:]))
    for col in zip(*A):
      pars, ok = [], True
      for i, j in rows:
        if col[i] > col[j]:
          count += 1
          ok = False
          break
        elif col[i] == col[j]:
          pars.append((i, j))
      if ok:
        if not pars:
          break
        else:
          rows = pars
    return count

class Solution:
  def minDeletionSize(self, A: List[str]) -> int:
    if len(A) == 1:
      return 0
    rows, count = [False] * len(A), 0
    for col in zip(*A):
      if all(rows[i] or col[i] <= col[i + 1] for i in range(len(col) - 1)):
        for i in range(len(col) - 1):
          if col[i] < col[i + 1]:
            rows[i] = True
      else:
        count += 1
      if all(rows):
        break
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["ca","bb","ac"],
    ["xc","yb","za"],
    ["xbb","xac","yab"],
    ["zyx","wvu","tsr"],
  ]
  rslts = [solver.minDeletionSize(A) for A in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
