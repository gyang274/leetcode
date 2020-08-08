import heapq

class Solution:
  def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    # a-star search
    # distance d(i1, i2) = shortest-length-cover str1[:i1] and str2[:i2]
    # a-star with heuristic h(i1, i2) = max(n1 - i1, n2 - i2)
    n1, n2 = len(str1), len(str2)
    # s: determined shortest supersequence length cover str1[:i1] and str2[:i2]
    # s: (i1, i2) -> l
    # c: candidate with (estimate = heuristic-lower-bound + determined, i1, i2, superstr)
    s, c = set(), [(max(n1, n2), max(n1, n2), 0, 0, 0, '')]
    while c:
      _, h, d, i1, i2, x = heapq.heappop(c)
      if (i1, i2) == (n1, n2):
        return x
      if (i1, i2) not in s:
        s.add((i1, i2))
        if i1 < n1 and i2 < n2 and str1[i1] == str2[i2]:
          heapq.heappush(c, (max(n1 - i1, n2 - i2) + d, max(n1 - i1 - 1, n2 - i2 - 1), d + 1, i1 + 1, i2 + 1, x + str1[i1]))
        else:
          if i1 < n1:
            heapq.heappush(c, (max(n1 - i1 - 1, n2 - i2) + d + 1, max(n1 - i1 - 1, n2 - i2), d + 1, i1 + 1, i2, x + str1[i1]))
          if i2 < n2:
            heapq.heappush(c, (max(n1 - i1, n2 - i2 - 1) + d + 1, max(n1 - i1, n2 - i2 - 1), d + 1, i1, i2 + 1, x + str2[i2]))
    return ''

class Solution:
  def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    # longest common subsequence, O(MN)
    def lcs(str1, str2):
      n, m = len(str1), len(str2)
      dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
      for i in range(n):
        for j in range(m):
          if str1[i] == str2[j]:
            dp[i + 1][j + 1] = dp[i][j] + str1[i]
          else:
            dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
      return dp[-1][-1]
     # recover shortest common supersequence from longest common subsequence    
    ans, i, j = "", 0, 0
    for c in lcs(str1, str2):
      while str1[i] != c:
        ans += str1[i]
        i += 1
      while str2[j] != c:
        ans += str2[j]
        j += 1
      ans += c
      i, j = i + 1, j + 1
    return ans + str1[i:] + str2[j:]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abac", "cab"),
  ]
  rslts = [solver.shortestCommonSupersequence(str1, str2) for str1, str2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")