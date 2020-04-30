from typing import List

class Node:
  def __init__(self):
    self.isEnde = False
    self.children = {}

class Solution:
  def addBoldTag(self, s: str, dict: List[str]) -> str:
    trie = Node()
    for p in dict:
      node = trie
      for x in p:
        if x not in node.children:
          node.children[x] = Node()
        node = node.children[x]
      node.isEnde = True
    bold = []
    for i in range(len(s)):
      node = trie
      j = k = i
      while j < len(s) and s[j] in node.children:
        node = node.children[s[j]]
        j += 1
        if node.isEnde:
          k = j
      if k > i:
        if bold and i <= bold[-1][1]:
          bold[-1][1] = max(bold[-1][1], k)
        else:
          bold.append([i, k])
    s = list(s)
    for i, k in bold[::-1]:
      s.insert(k, "</b>")
      s.insert(i, "<b>")
    return "".join(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abcxyz123", ["abc","123"]),
    ("aaabbcc", ["aaa","aab","bc"]),
    ("aaabbcc", ["aaa","aab","bc","aaabbcc"]),
  ]
  rslts = [solver.addBoldTag(s, dict) for s, dict in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
