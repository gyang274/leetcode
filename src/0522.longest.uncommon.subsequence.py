class Solution:
  def isSubsequence(self, a, b):
    na, nb = len(a), len(b)
    i, j = 0, 0
    while i < na:
      while j < nb and not a[i] == b[j]:
        j += 1
      if j == nb:
        return False
      i += 1
      j += 1
    return True
  def findLUSlength(self, strs: List[str]) -> int:
    n = len(strs)
    if n == 0:
      return -1
    # sort
    strs.sort(key=lambda x: (len(x), x), reverse=True)
    for i in range(n):
      for u in range(i):
        if self.isSubsequence(strs[i], strs[u]):
          break
      else:
        if i == n - 1 or len(strs[i]) > len(strs[i + 1]) or not strs[i] == strs[i + 1]:
          return len(strs[i])
    return -1
