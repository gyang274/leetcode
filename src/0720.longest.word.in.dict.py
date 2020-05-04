class Solution:
  def dfs(self, path, node):
    if "#" in node:
      if len(path) > len(self.ans) or (len(path) == len(self.ans) and path < self.ans):
        self.ans = path
      for w in node:
        if not w == "#":
          self.dfs(path + w, node[w])
    return None
  def longestWord(self, words: List[str]) -> str:
    # trie + dfs
    # built trie
    trie = {}
    for word in words:
      node = trie
      for w in word:
        if w not in node:
          node[w] = {}
        node = node[w]
      node["#"] = 1
    trie["#"] = 1
    # dfs
    self.ans = ""
    self.dfs("", trie)
    return self.ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["w", "wo", "wor", "worl", "world"],
    ["a", "banana", "app", "appl", "ap", "apply", "apple"],
  ]
  rslts = [solver.longestWord(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
