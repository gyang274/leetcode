import string

class Solution:
  def prefix(self, s):
    # KMP
    p = [0] * len(s)
    # contruct \pi table
    for i in range(1, len(s)):
      k = p[i - 1]
      while k > 0 and s[k] != s[i]: 
        k = p[k - 1]
      if s[k] == s[i]:
        k += 1
      p[i] = k
    return p[-1]

  def CreateConnections(self, evil, T):
    k = len(evil)
    connections = [[-1] * T for _ in range(k)]
    conn = [[] for _ in range(k)]
    for i in range(k):
      for letter in self.alphabet:
        curr_max = self.prefix(evil + "#" + evil[0:i] + letter)
        # process case when we reached the end of evil string
        if curr_max != k:
          connections[i][ord(letter) - ord("a")] = curr_max
          if curr_max != 0:
            conn[i].append([ord(letter) - ord("a"), curr_max])
    connections_num_zeros = [[0] for _ in range(k)]
    for i in range(k):
      for j in range(1, T + 1):
        connections_num_zeros[i] += [connections_num_zeros[i][-1] + (connections[i][j - 1] == 0)]
    return connections_num_zeros, conn

  def findLesserGood(self, n, k, string, M, evil):
    dp_bord = [[0] * k for _ in range(n)]
    dp_notb = [[0] * k for _ in range(n)]
    dp_bord[0][0] = 1
    for it_n in range(n - 1):
      for it_k in range(k):
        ord_num = ord(string[it_n + 1]) - ord("a")
        for letter, s in self.conn[it_k]:
          dp_notb[it_n + 1][s] += dp_notb[it_n][it_k]
          if letter < ord_num:
            dp_notb[it_n + 1][s] += dp_bord[it_n][it_k]
        dp_notb[it_n + 1][0] += self.conn_num_zero[it_k][-1] * dp_notb[it_n][it_k]     
        dp_notb[it_n + 1][0] += self.conn_num_zero[it_k][ord_num] * dp_bord[it_n][it_k]
        dp_notb[it_n + 1][it_k] %= M
      index = self.prefix(evil + "#" + string[0:it_n+2])
      if index != k and sum(dp_bord[it_n]) != 0:
        dp_bord[it_n + 1][index] = 1
    return sum(dp_bord[-1]) + sum(dp_notb[-1])

  def findGoodStrings(self, n: int, s1: str, s2: str, evil: str) -> int:
    # dp: O(nk), k = len(evil)
    self.alphabet = string.ascii_lowercase
    M, k = 10**9 + 7, len(evil)
    self.conn_num_zero, self.conn = self.CreateConnections(evil, len(self.alphabet))
    res1 = self.findLesserGood(n + 1, k, "#" + s2, M, evil)
    res2 = self.findLesserGood(n + 1, k, "#" + s1, M, evil)
    return (res1 - res2 + 1 - (evil in s1)) % M

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (8, "edocteel", "leetcode", "echo")
  ]
  rslts = [solver.findGoodStrings(n, s1, s2, evil) for n, s1, s2, evil in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
