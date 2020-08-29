from collections import Counter

class Solution:
  def maxNumberOfBalloons(self, text: str) -> int:
    count = Counter(text)
    return min(count['a'], count['b'], count['l'] // 2, count['n'], count['o'] // 2)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "nlaebolko",
    "loonbalxballpoon",
  ]
  rslts = [solver.maxNumberOfBalloons(text) for text in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
