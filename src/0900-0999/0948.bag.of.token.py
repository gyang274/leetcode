from typing import List

class Solution:
  def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
    # greedy
    # pay min power/token to buy 1 point, buy max power/token by pay 1 point
    tokens.sort()
    n = len(tokens)
    i, j, k, m = 0, n - 1, 0, 0
    while i <= j:
      while i <= j and P >= tokens[i]:
        P -= tokens[i]
        i += 1
      k = max(k, i - (n - 1 - j))
      if k == 0:
        return 0
      if i <= j:
        P += tokens[j]
        j -= 1
    return k

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([100], 50),
    ([100,200], 150),
    ([100,200,300,400], 200),
  ]
  rslts = [solver.bagOfTokensScore(tokens, P) for tokens, P in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
