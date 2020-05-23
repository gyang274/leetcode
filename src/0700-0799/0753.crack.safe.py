class Solution:
  def crackSafe(self, n: int, k: int) -> str:
    # Hierholzer's Algorithm
    ans, seen = [], set([])
    def dfs(node):
      for x in map(str, range(k)):
        nuxt = node + x
        if nuxt not in seen:
          seen.add(nuxt)
          dfs(nuxt[1:])
          ans.append(x)
    dfs("0" * (n - 1))
    return "".join(ans) + "0" * (n - 1)

class Solution:
  def crackSafe(self, n: int, k: int) -> str:
    # Inverse Burrows-Wheeler Transform
    m = k ** (n - 1)
    p = [q * k + i for i in range(k) for q in range(m)]
    ans = []
    for i in range(k ** n):
      j = i
      while p[j] >= 0:
        ans.append(str(j // m))
        p[j], j = -1, p[j]
    return "".join(ans) + "0" * (n - 1)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 2),
    (2, 2),
    (2, 3),
  ]
  rslts = [solver.crackSafe(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
