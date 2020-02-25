from typing import List

class Solution:
  def __init__(self):
    # strobo
    self.strobo = {
      "0": "0",
      "1": "1",
      "8": "8",
      "6": "9",
      "9": "6",
    }
    # strobo as init, without 0
    self.stroboInit = {
      "1": "1",
      "8": "8",
      "6": "9",
      "9": "6",      
    }
    # memo on strobogrammic
    self.memo = {
      0: [""],
      1: ["0", "1", "8"],
    }
    # memo on recursive calls
    # n = 2: '00' is valid for recusive
    self.memoRecursive = {
      0: [""],
      1: ["0", "1", "8"]
    }
  def recursive(self, n):
    if n not in self.memoRecursive:
      self.memoRecursive[n] = [] 
      for x in self.strobo:
        for v in self.recursive(n - 2):
          self.memoRecursive[n].append(x + v + self.strobo[x])
    return self.memoRecursive[n]
  def findStrobogrammatic(self, n: int) -> List[str]:
    if n not in self.memo:
      self.memo[n] = []
      for x in self.stroboInit:
        for v in self.recursive(n - 2):
          self.memo[n].append(x + v + self.strobo[x])
    return self.memo[n]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 4, 5, 8
  ]
  rslts = [solver.findStrobogrammatic(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")