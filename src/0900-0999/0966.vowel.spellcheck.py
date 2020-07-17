from typing import List

import itertools

class Solution:
  def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
    devowels = lambda word: "".join('*' if x in {'a', 'e', 'i', 'o', 'u'} else x for x in word)
    # case in-sensitive
    d, q = {}, {}
    for word in wordlist:
      wc = word.lower()
      d[wc] = d.get(wc, word)
      # spell-check ignore vowels
      wk = devowels(wc)
      q[wk] = q.get(wk, word)
    # case sensitive
    wordlist = set(wordlist)
    # query
    ans = []
    for query in queries:
      if query in wordlist:
        ans.append(query)
      else:
        query = query.lower()
        if query in d:
          ans.append(d[query])
        else:
          query = devowels(query)
          if query in q:
            ans.append(q[query])
          else:
            ans.append("")
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["KiTe","kite","hare","Hare"], ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]),
  ]
  rslts = [solver.spellchecker(wordlist, queries) for wordlist, queries in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
