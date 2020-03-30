from typing import List

class Solution:
  def recursive(self, word):
    # print(self.memo)
    if word not in self.memo:
      node = self.trie
      for i in range(len(word)):
        if word[i] not in node:
          self.memo[word] = ""
          break
        node = node[word[i]]
        if "#" in node:
          winext = self.recursive(word[(i + 1):])
          if not winext == "":
            self.memo[word] = word[:(i + 1)] + "#" + winext
            break
      if word not in self.memo:
        if "#" in node:
          self.memo[word] = word
        else:
          self.memo[word] = ""
    return self.memo[word]
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    """Trie + DFS + memorization.
    """
    # build the trie
    self.trie = {}
    for word in words:
      node = self.trie
      for w in word:
        if w not in node:
          node[w] = {}
        node = node[w]
      node["#"] = 1
    # DFS over Trie + memorization
    ans, self.memo = [], {}
    for word in words:
      concatenate = self.recursive(word)
      if word == "yyifkin":
        print(concatenate)
      if len(concatenate) > len(word):
        ans.append(word)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat","ratcathippopo"],
  ]
  rslts = [solver.findAllConcatenatedWordsInADict(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
