from typing import List
from collections import defaultdict

class Solution:
  def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    """From 0127, wordCandidate <-> word which is O(m*n), m = wordLength, n = len(wordList).
      Then, BFS from beginWord until endWord.
    """
    if endWord not in wordList or not beginWord or not endWord or not wordList:
      return []
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
    ans, visited, boundary, stack, holds = [], set([beginWord]), set(), [[beginWord, ] ], []
    while stack or holds:
      while stack:
        wpath = stack.pop()
        w = wpath[-1]
        if w == endWord:
          ans.append(wpath)
        else:
          for v in wdict[w]:
            for wnext in vdict[v]:
              if wnext not in visited:
                holds.append(wpath + [wnext])
                boundary.add(wnext)
      if not ans:
        stack, holds = holds, []
        visited.update(boundary)
        boundary = set()
      else:
        break
    return ans

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("hit", "cog", ["hot","dot","dog","lot","log","cog"]),
    ("hit", "cog", ["hot","dot","dog","lot","log"]),
  ]
  rslts = [solver.findLadders(beginWord, endWord, wordList) for beginWord, endWord, wordList in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
