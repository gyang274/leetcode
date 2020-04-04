from typing import List
from collections import defaultdict

class Solution:
  def recursive(self, queue, words):
    k = len(queue)
    if k == self.n:
      self.ans.append(queue)
    else:
      for word in words:
        ok = True
        for i in range(len(queue)):
          if not word[i] == queue[i][k]:
            ok = False
            break
        if ok:
          self.recursive(queue + [word], words)
  def wordSquares(self, words: List[str]) -> List[List[str]]:
    """dfs backtrack.
    """
    self.n = len(words[0])
    self.ans = []
    self.recursive([], set(words))
    return self.ans

class Solution:
  def recursive(self, queue):
    k = len(queue)
    if k == self.n:
      self.ans.append(queue)
    else:
      # make a copy..
      ws = set(self.wsnext[(queue[0], 0)][k])
      for i in range(1, k):
        ws &= self.wsnext[(queue[i], i)][k]
      for w in ws:
        self.recursive(queue + [w])
  def wordSquares(self, words: List[str]) -> List[List[str]]:
    """Key: word square ws, ws[i][j] == ws[j][i], so if wordX[j] == wordY[i] then (X, Y) is candidate at i and j in ws.
    """
    self.n = len(words[0])
    # ws next
    self.wsnext = defaultdict(lambda: defaultdict(set))
    for wi in range(len(words)):
      for wj in range(wi, len(words)):
        for j in range(len(words[wi])):
          for i in range(len(words[wj])):
            if (not i == j) and words[wi][j] == words[wj][i]:
              if i < j:
                # words[wi] as i-th words in ws, words[wj] can be the j-th words in ws, i < j
                self.wsnext[(words[wi], i)][j].add(words[wj])
              else:
                # words[wj] as j-th words in ws, words[wi] can be the i-th words in ws, j < i
                self.wsnext[(words[wj], j)][i].add(words[wi])
    # ans
    self.ans = []
    for word in words:
      self.recursive([word])
    return self.ans

class Solution:
  def recursive(self, queue):
    k = len(queue)
    if k == self.n:
      self.ans.append(queue)
    else:
      prefix = ""
      for i in range(k):
        prefix += queue[i][k]
      for word in self.prefixWords[prefix]:
        self.recursive(queue + [word])
  def wordSquares(self, words: List[str]) -> List[List[str]]:
    """backtrack with hashtable
    """
    self.n = len(words[0])
    # hash words with prefix
    self.prefixWords = defaultdict(set)
    for word in words:
      for i in range(self.n):
        self.prefixWords[word[:(i + 1)]].add(word)
    # ans
    self.ans = []
    for word in words:
      self.recursive([word])
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["abat","baba","atan","atal"],
    # ["area","lead","wall","lady","ball"],
  ]
  rslts = [solver.wordSquares(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")