class Solution:
  def distinctEchoSubstrings(self, text: str) -> int:
    # O(N^2) check all substr, O(1) each check with rolling hash
    s, n = list(map(lambda x: ord(x) - ord('a'), text)), len(text)
    e = set()
    for j in range(n - 1, 0, -1):
      h, k, l, kk = s[j], 1, 1, 1
      for i in range(j - 1, -1, -1):
        l += 1
        k *= 26
        h += s[i] * k
        # length is even
        if (l & 1) ^ 1:
          kk *= 26
          if h // kk == h % kk:
            e.add(text[i:(j + 1)])
    return len(e)

class Solution:
  def distinctEchoSubstrings(self, text: str) -> int:
    # O(N^2) check all substr, O(1) each check with rolling count of equality
    # s: text + '#' in case length of text is odd and out of index error
    s, n = text + '#', len(text)
    echo = set()
    for k in range(1, n // 2 + 1):
      # init
      same = sum(x == y for x, y in zip(s[:k], s[k:(k + k)]))
      for i in range(n - 2 * k + 1):
        if same == k:
          echo.add(s[i:(i + 2 * k)])
        # rolling the count of equality
        same += (s[i + k] == s[i + k + k]) - (s[i] == s[i + k])
    return len(echo)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "abcabcabc",
    "tiduxtidux",
    "leetcodeleetcode",
  ]
  rslts = [solver.distinctEchoSubstrings(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
