from typing import List
from collections import defaultdict

import heapq

class Solution:
  def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
    # constructor
    Trie = lambda: defaultdict(Trie)
    # construct the trie of words, and store search suggestions in node['#']
    trie = Trie()
    for product in products:
      node = trie
      for x in product:
        node = node[x]
        if '#' not in node:
          node['#'] = []
        node['#'].append(product)
        if len(node['#']) > 3:
          heapq._heapify_max(node['#'])
          heapq._heappop_max(node['#'])
    # use the trie and prefix
    ans, node = [], trie
    for x in searchWord:
      node = node[x]
      ans.append(sorted(node['#']))
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["mobile","mouse","moneypot","monitor","mousepad"], "mouse"),
  ]
  rslts = [solver.suggestedProducts(products, searchWord) for products, searchWord in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
