class Solution:
  def backtrack(self, s1, s2, s3, i, j, k):
    if k == len(s3):
      return True
    elif (i < len(s1) and s1[i] == s3[k]) and (j < len(s2) and s2[j] == s3[k]):
      return self.backtrack(s1, s2, s3, i + 1, j, k + 1) or self.backtrack(s1, s2, s3, i, j + 1, k + 1)
    elif i < len(s1) and s1[i] == s3[k]:
      return self.backtrack(s1, s2, s3, i + 1, j, k + 1)
    elif j < len(s2) and s2[j] == s3[k]:
      return self.backtrack(s1, s2, s3, i, j + 1, k + 1)
    else:
      return False
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    """backtrack
    """
    if not len(s1) + len(s2) == len(s3):
      return False
    return self.backtrack(s1, s2, s3, 0, 0, 0)


class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    """dynamic programming
      dp[k][i][j] represent s3[-k:] can be interleaved by s1[-i:] and s2[-j:]
    """
    if not len(s1) + len(s2) == len(s3):
      return False
    dp = [ [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)] for _ in range(len(s3) + 1)]
    dp[0][0][0] = True
    for k in range(1, len(s3) + 1):
      for i in range(0, k + 1):
        j = k - i
        if i >= 0 and i <= len(s1) and j >= 0 and j <= len(s2):
          # print(f"{k=}, {i=}, {j=}, {s3[-k]=}, {s1[-i]=}, {s2[-j]}, {dp[k - 1][i - 1][j]=}, {dp[k - 1][i][j - 1]=}")
          dp[k][i][j] = (dp[k - 1][i - 1][j] and s3[-k] == s1[-i]) or (dp[k - 1][i][j - 1] and s3[-k] == s2[-j])
    return dp[len(s3)][len(s1)][len(s2)]


class Solution:
  def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    """dynamic programming
      dp[k][i][j] represent s3[-k:] can be interleaved by s1[-i:] and s2[-j:]
    """
    if not len(s1) + len(s2) == len(s3):
      return False
    memo = {}
    memo[(0, 0)] = True
    def dp(i, j):
      if (i, j) not in memo:
        memo[(i, j)] = False
        if i >= 0 and i <= len(s1) and j >= 0 and j <= len(s2):
          if i > 0:
            memo[(i, j)] |= (s3[-(i + j)] == s1[-i] and dp(i - 1, j)) 
          if j > 0:
            memo[(i, j)] |= (s3[-(i + j)] == s2[-j] and dp(i, j - 1))
      return memo[(i, j)]
    return dp(len(s1), len(s2))


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("aa", "bbb", "ababa"),
    ("aabcc", "dbbca", "aadbbcbcac"),
    ("ab", "bc", "babc"),
    ("aabcc", "dbbca", "aadbbbaccc"),
    (
      "bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa",
      "babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab",
      "babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
    ),
  ]
  rslts = [solver.isInterleave(s1, s2, s3) for s1, s2, s3 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")