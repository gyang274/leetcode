class Solution:
  def compareVersion(self, version1: str, version2: str) -> int:
    v1, v2 = version1.split('.'), version2.split('.')
    n1, n2 = len(v1), len(v2)
    if not n1 == n2:
      if n1 < n2:
        v1 += [0 for _ in range(n2 - n1)]
      else:
        v2 += [0 for _ in range(n1 - n2)]
    n = max(n1, n2)
    for i in range(n):
      if int(v1[i]) < int(v2[i]):
        return -1
      if int(v1[i]) > int(v2[i]):
        return 1
    return 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("0.1", "1.1"),
    ("1.0.1", "1"),
    ("7.5.2.4", "7.5.3"),
    ("1.01", "1.001"),
    ("1.0", "1.0.0"),
  ]
  rslts = [solver.compareVersion(version1, version2) for version1, version2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  