from typing import List

class Solution:
  def constructKMPReferenceTable(self, p):
    m = len(p)
    # construct the \pi reference table
    u = [-1 for _ in range(m + 1)]
    k = -1
    for i in range(1, m + 1):
      while k >= 0 and p[k] != p[i - 1]:
        k = u[k]
      k += 1
      u[i] = k
    # print(u)
    return u
  def strStr(self, s: str, p: str, u: List[int]) -> int:
    """Knuth-Morris-Pratt (KMP) Algorithm.
    """
    n, m = len(s), len(p)
    # match with push forward w.r.t \pi
    i = 0
    j = 0
    k = 0
    while i < n:
      j = max(0, k)
      # print('outer', i, j, k)
      while i + j < n and j < m and s[i + j] == p[j]:
        j += 1
        # print('inner', i, j, k)
        if j == m:
          return True
      k = u[j]
      i = i + max(1, j - k) 
    return False
  def stringMatching(self, words: List[str]) -> List[str]:
    # Q0028 KMP
    words.sort(key=lambda x: len(x))
    n = len(words)
    ans = []
    for i in range(n):
      # construct KMP reference table once
      u = self.constructKMPReferenceTable(words[i])
      for j in range(i + 1, n):
        if self.strStr(words[j], words[i], u):
          ans.append(words[i])
          break
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["blue","green","bu"],
    ["leetcode","et","code"],
    ["mass","as","hero","superhero"],
  ]
  rslts = [solver.stringMatching(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
