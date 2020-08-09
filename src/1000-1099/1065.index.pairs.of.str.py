from typing import List
from collections import defaultdict
from functools import reduce

class Solution:
  def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
    # approx O(N + W), n = len(text), w = sum(map(len, words))
    # O(W): trie on words
    # constructor
    Trie = lambda: defaultdict(Trie)
    # construct the trie of words
    trie = Trie()
    for word in words:
      reduce(dict.__getitem__, word, trie)['#'] = True
    # O(N+), pasring on text
    ans, nodes = [], []
    for j, x in enumerate(text):
      nuxts = [] 
      nodes.append((j, trie))
      for i, node in nodes:
        if x in node:
          nuxts.append((i, node[x]))
          if '#' in node[x]:
            ans.append((i, j))
      nodes = nuxts
    return sorted(ans)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("thestoryofleetcodeandme", ["story","fleet","leetcode"]),
  ]
  rslts = [solver.indexPairs(text, words) for text, words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
