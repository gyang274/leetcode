from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
  def dist(self, w1: str, w2: str) -> int:
    return reduce(lambda x, y: x + 1 if y[0] != y[1] else x, zip(w1, w2), 0)
  def backtrack(self, rslt, source, target):
    if source == target:
      self.ans.append(rslt + [source])
    else:
      for w in self.wdict[source]:
        if w not in self.explored:
          self.explored.add(w)
          self.backtrack(rslt + [source], w, target)
          self.explored.remove(w)
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """maintain a word -> setWordsOfDist1, then DFS + backtrack.
    """
    if endWord not in wordList:
      return 0
    # wdict: word -> setWordsOfDist1
    self.wdict = defaultdict(list)
    for i, w in enumerate(wordList):
      if self.dist(beginWord, w) == 1:
        self.wdict[beginWord].append(w)
      for j in range(i + 1, len(wordList)):
        if self.dist(w, wordList[j]) == 1:
          self.wdict[w].append(wordList[j])
          self.wdict[wordList[j]].append(w)
    # maintain a global explored set of words to avoid loop
    self.explored = set([beginWord, ])
    # backtrack
    self.ans = []
    self.backtrack([], beginWord, endWord)
    return min([len(rslt) for rslt in self.ans]) if len(self.ans) > 0 else 0

class Solution:
  def dist(self, w1: str, w2: str) -> int:
    return reduce(lambda x, y: x + 1 if y[0] != y[1] else x, zip(w1, w2), 0)
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """maintain a word -> setWordsOfDist1, then dynamic programming with memorization.
      dist[w, endWord] = 1 + min(dist[v, endWord]), any v in setWordOfDist1
    """
    if endWord not in wordList:
      return 0
    # wdict: word -> setWordsOfDist1
    wdict = defaultdict(set)
    for i, w in enumerate(wordList):
      if self.dist(beginWord, w) == 1:
        wdict[beginWord].add(w)
      for j in range(i + 1, len(wordList)):
        if self.dist(w, wordList[j]) == 1:
          wdict[w].add(wordList[j])
          wdict[wordList[j]].add(w)
    memo = {}
    def dp(w):
      if not w in memo:
        memo[w] = 0
        if endWord in wdict[w]:
          memo[w] = 2
        else:
          for v in wdict[w]:
            if dp(v) > 0:
              if memo[w] == 0:
                memo[w] = memo[v] + 1
              else:
                memo[w] = min(memo[w], memo[v] + 1)
      return memo[w]
    return dp(beginWord)

class Solution:
  def dist(self, w1: str, w2: str) -> int:
    return reduce(lambda x, y: x + 1 if y[0] != y[1] else x, zip(w1, w2), 0)
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """maintain a word -> setWordsOfDist1, then BFS from endWord until beginWord.
    """
    if endWord not in wordList:
      return 0
    # wdict: word -> setWordsOfDist1
    wdict = defaultdict(set)
    for i, w in enumerate(wordList):
      if self.dist(w, endWord) == 1:
        wdict[endWord].add(w)
      for j in range(i + 1, len(wordList)):
        if self.dist(w, wordList[j]) == 1:
          wdict[w].add(wordList[j])
          wdict[wordList[j]].add(w)
        if self.dist(beginWord, w) == 1:
          wdict[w].add(beginWord)
    level, memo, stack, holds = 2, {}, wdict[endWord], set()
    while stack or holds:
      if beginWord in stack:
        return level
      while stack:
        w = stack.pop()
        memo[w] = level
        for v in wdict[w]:
          if v not in memo:
            holds.add(v)
      stack, holds = holds, set()
      level += 1
    return 0

class Solution:
  def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """The creation of a word -> setWordsOfDist1, is O(n^2).
      Often, wordLength <<< numOfWords, so, instead create a wordCandidate -> word which is O(m*n), m = wordLength.
      Then, BFS from endWord until beginWord.
    """
    if endWord not in wordList or not beginWord or not endWord or not wordList:
      return 0
    # wdict: word -> wordCandidate
    # vdict: wordCandidate -> word
    n, wdict, vdict = len(beginWord), defaultdict(set), defaultdict(set)
    for i in range(n):
      # get wordCandidate by replacing i-th position character with '*'
      v = beginWord[:i] + '*' + beginWord[(i + 1):]
      wdict[beginWord].add(v)
      vdict[v].add(beginWord)
    for w in wordList:
      for i in range(n):
        v = w[:i] + '*' + w[(i + 1):]
        wdict[w].add(v)
        vdict[v].add(w)
    # BFS: shortest path on unweighted undirected graph
    level, memo, stack, holds = 2, set(), wdict[endWord], set()
    while stack or holds:
      while stack:
        v = stack.pop()
        if beginWord in vdict[v]:
          return level
        for w in vdict[v]:
          if w not in memo and w not in stack:
            holds.update(wdict[w])
            memo.add(w)
      stack, holds = holds, set()
      level += 1
    return 0

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
    ("hit", "cog", ["hot","dot","dog","lot","log"]),
  ]
  rslts = [solver.ladderLength(beginWord, endWord, wordList) for beginWord, endWord, wordList in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
