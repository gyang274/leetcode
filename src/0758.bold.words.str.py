from typing import List

class Solution:
  def boldWords(self, words: List[str], S: str) -> str:
    """Q0616, trie + merge intervals O(N sum(W)).
    """
    # trie
    trie = {}
    for word in words:
      node = trie
      for w in word:
        if w not in node:
          node[w] = {}
        node = node[w]
      node["#"] = 1
    # parsing S
    i, n, b = 0, len(S), []
    while i < n:
      node, j, k = trie, i, i
      while j < n and S[j] in node:
        node = node[S[j]]
        if "#" in node:
          k = j + 1
        j += 1
      if k > i:
        if b and i <= b[-1]:
          b[-1] = max(b[-1], k)
        else:
          b.extend([i, k])
      i += 1
    # tag S with <b></b>
    s = list(S)
    for i, j in enumerate(b[::-1]):
      if i & 1:
        s.insert(j, '<b>')
      else:
        s.insert(j, '</b>')
    return ''.join(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["ab","bc"], "aabcd"),
  ]
  rslts = [solver.boldWords(words, S) for words, S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
