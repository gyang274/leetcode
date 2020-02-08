from typing import List


class Solution:
  def findSubstringAtKRecursive(self, ans, s, k, w, words):
    if len(s) == 0 and len(words) == 0:
      ans.append(k)
    elif s[:w] in words:
      words.remove(s[:w])
      self.findSubstringAtKRecursive(ans, s[w:], k, w, words)
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    ans = []
    n = len(words)
    if n == 0:
      return []
    w = len(words[0])
    for k in range(len(s) - n * w + 1):
      wordsCopy = words.copy()
      self.findSubstringAtKRecursive(ans, s[k:(k + n * w)], k, w, wordsCopy)
    return ans


class Solution:
  def findSubstring(self, s: str, words: List[str]) -> List[int]:
    """Hash List.
    """
    ans = []
    n = len(words)
    if n == 0:
      return []
    w = len(words[0])
    if len(s) < n * w:
      return []
    # world list to hash table (wdict)
    wdict = {}
    for word in words:
      wdict[word] = wdict.get(word, 0) + 1  
    # go through s, in fact only possible pattern are s[0], s[1], .., s[w - 1]
    for i in range(w):
      lft, cnt, sdict = i, 0, {}
      for j in range(i, len(s), w):
        word = s[j:(j + w)]
        if word in wdict:
          sdict[word] = sdict.get(word, 0) + 1
          cnt += 1
          if sdict[word] > wdict[word]:
            # move left one world by another until move out conflict
            while sdict[word] > wdict[word]:
              sdict[s[lft:(lft+w)]] -= 1
              lft += w
              cnt -= 1
          if cnt == n:
            ans.append(lft)
            sdict[s[lft:(lft+w)]] -= 1
            lft += w
            cnt -= 1
        else:
          lft, cnt, sdict = j + w, 0, {}
    return ans


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ("barfoothefoobarman", ["foo", "bar"]),
    ("barfoofoobarthefoobarman", ["bar","foo","the"]),
    ("wordgoodgoodgoodbestword", ["word","good","best","word"]),
    # ("a" * 5000, ["a"] * 5001),
  ]
  rslts = [solver.findSubstring(s, words) for s, words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
