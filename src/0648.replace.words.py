from typing import List

class Solution:
  def replaceWords(self, dict: List[str], sentence: str) -> str:
    trie = {}
    for word in dict:
      node = trie
      for w in word:
        if w not in node:
          node[w] = {}
        node = node[w]
      node["#"] = 1
    sent = sentence.split()
    for i, word in enumerate(sent):
      node = trie
      for k, w in enumerate(word):
        if "#" in node:
          sent[i] = word[:k]
          break
        elif w in node:
          node = node[w]
        else:
          break
    return " ".join(sent)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (["cat","bat","rat"], "the cattle was rattled by the battery"),
  ]
  rslts = [solver.replaceWords(dict, sentence) for dict, sentence in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
