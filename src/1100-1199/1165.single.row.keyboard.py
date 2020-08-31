class Solution:
  def calculateTime(self, keyboard: str, word: str) -> int:
    d, n = {x: i for i, x in enumerate(keyboard)}, len(word)
    return d[word[0]] + sum(abs(d[word[i]] - d[word[i - 1]]) for i in range(1, n))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcdefghijklmnopqrstuvwxyz", "cba"),
    ("pqrstuvwxyzabcdefghijklmno", "leetcode"),
  ]
  rslts = [solver.calculateTime(keyboard, word) for keyboard, word in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
