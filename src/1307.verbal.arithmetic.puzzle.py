from typing import List
from functools import reduce

import operator

class Solution:
  def recursive(self, i, nums):
    if i == self.n:
      d = {x: str(m) for x, m in zip(self.x, self.m)}
      z = lambda word: int(reduce(operator.__add__, map(lambda x: d[x], word), ''))
      return sum(map(z, self.words)) == z(self.result)
    for k in range(len(nums)):
      if nums[k] == 0 and self.x[i] in self.y:
        continue
      self.m[i] = nums[k]
      if self.recursive(i + 1, nums[:k] + nums[(k + 1):]):
        return True
    return False
  def isSolvable(self, words: List[str], result: str) -> bool:
    # backtrack
    self.words, self.result = words, result
    # y: all leading characters
    self.y = set(map(lambda word: word[0], words)) | set(result[0])
    # x: all unique characters
    self.x = list(reduce(operator.__or__, map(set, words)) | set(result))
    # m: characters mapping to nums by index
    if len(self.x) > 10 or len(self.y) > 9:
      return False
    self.n = len(self.x)
    self.m = [None] * self.n
    # backtrack
    return self.recursive(0, [0,1,2,3,4,5,6,7,8,9])

class Solution:
  def recursive(self, i, nums):
    if isinstance(self.x[i], str):
      for k in range(len(nums)):
        if nums[k] == 0 and self.x[i] in self.y:
          continue
        self.d[self.x[i]] = str(nums[k])
        if self.recursive(i + 1, nums[:k] + nums[(k + 1):]):
          return True
      return False
    else:
      z = lambda word: int(reduce(operator.__add__, map(lambda x: self.d[x], word[(-self.x[i]):]), ''))
      l, r = str(sum(map(z, self.words[:-1]))), str(z(self.words[-1]))
      if int(l[-len(r):]) == int(r):
        if i + 1 == len(self.x):
          return True
        else:
          return self.recursive(i + 1, nums)
      else:
        return False
  def isSolvable(self, words: List[str], result: str) -> bool:
    # backtrack + efficient prunning
    self.words = words
    self.words.append(result)
    # y: all leading characters
    self.y = set(map(lambda word: word[0], self.words))
    # x: all unique characters from least-significant to most-siginificant digit position + check point for prunning
    self.x, seen, n = [], set(), max(*map(len, self.words))
    for i in range(n):
      # seem: new character from all ith-least-significant digit position
      seem = set()
      for word in self.words:
        if len(word) > i and word[-(i + 1)] not in seen:
          seem.add(word[-(i + 1)])
          seen.add(word[-(i + 1)])
          self.x.append(word[-(i + 1)])
      # put a number to indicate early check point for all i-least-significant digits for prunnning
      if seem:
        self.x.append(i + 1)
      else:
        self.x[-1] = i + 1
    self.d = {z: -1 for z in self.x if isinstance(z, str)}
    # backtrack + efficient prunning
    return self.recursive(0, [0,1,2,3,4,5,6,7,8,9])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["SEND","MORE"], "MONEY"),
    (["LEET","CODE"], "POINT"),
    (["THIS","IS","TOO"], "FUNNY"),
    (["SIX","SEVEN","SEVEN"], "TWENTY"),
  ]
  rslts = [solver.isSolvable(words, result) for words, result in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
