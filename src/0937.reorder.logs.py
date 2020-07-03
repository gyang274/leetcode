from typing import List

class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    alpha, digit = [], []
    for log in logs:
      x, *y = log.split()
      if y[0][0].isalpha():
        alpha.append((y, x, log))
      else:
        digit.append(log)
    return [log for _, _, log in sorted(alpha)] + digit

class Solution:
  def reorderLogFiles(self, logs: List[str]) -> List[str]:
    def f(log):
      _id, rest = log.split(" ", 1)
      return (0, rest, _id) if rest[0].isalpha() else (1, )
    return sorted(logs, key = f)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"],
  ]
  rslts = [solver.reorderLogFiles(logs) for logs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
