from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
  def minimumLengthEncoding(self, words: List[str]) -> int:
    # remove duplicates
    words = list(set(words))
    # trie
    trie = {}
    for word in words:
      node = trie
      for w in word[::-1]:
        if w not in node:
          node[w] = {}
        node = node[w]
    # reduce(dict.__getitem__, S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
    nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
    return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)

class Solution:
  def minimumLengthEncoding(self, words: List[str]) -> int:
    # remove duplicates
    words = list(set(words)) 
    # Trie is a nested dictionary with nodes created when fetched entries are missing
    Trie = lambda: defaultdict(Trie)
    # trie
    trie = Trie()
    # reduce(dict.__getitem__, S, trie) is trie[S[0]][S[1]][S[2]][...][S[S.length - 1]]
    nodes = [reduce(dict.__getitem__, word[::-1], trie) for word in words]
    #Add word to the answer if it's node has no neighbors
    return sum(len(word) + 1 for i, word in enumerate(words) if len(nodes[i]) == 0)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["time", "me", "bell"],
  ]
  rslts = [solver.minimumLengthEncoding(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")

