class Solution:
  def shortestWay(self, source: str, target: str) -> int:
    m, n, count = len(source), len(target), 0
    i = 0
    while i < n:
      j, k = i, 0
      while j < n and k < m:
        if target[j] == source[k]:
          j += 1
        k += 1
      if j == i:
        return -1
      count += 1
      i = j
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", "abcbc"),
    ("abc", "abcdc"),
    ("xyz", "xzyxz"),
  ]
  rslts = [solver.shortestWay(source, target) for source, target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
