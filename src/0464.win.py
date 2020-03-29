class Solution:
  def recursive(self, t, k):
    if (t, k) not in self.memo:
      for i in range(self.m):
        # can win iff any next state can't win
        if (k >> i) & 1 == 0:
          if (t - (i + 1)) <= 0 or not self.recursive(t - (i + 1), k | (1 << i)):
            self.memo[(t, k)] = True
            break
      else:
        # can't win iff all next state can win
        self.memo[(t, k)] = False
    return self.memo[(t, k)]
  def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
    if desiredTotal <= maxChoosableInteger:
      return True
    upper = maxChoosableInteger * (maxChoosableInteger + 1) // 2
    if desiredTotal > upper:
      return False
    # DFS + memorization
    # 1. can win iff any next state can't win
    # 2. can't win iff all next state can win
    # 3. state if defined by (t: total, k: availableInt), 
    #   availableInt can be represented by bit of m: maxChoosableInteger, where 1 at position i as i + 1 is picked
    self.m, self.memo = maxChoosableInteger, {}
    return self.recursive(desiredTotal, 0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (10, 0),
    (10, 1),
    (10, 11),
    (10, 40),
  ]
  rslts = [solver.canIWin(maxChoosableInteger, desiredTotal) for maxChoosableInteger, desiredTotal in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")