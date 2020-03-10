from typing import List
from collections import defaultdict

class Solution:
  def kmp(self, p):
    # Knuth-Morris-Pratt (KMP) Algorithm
    m = len(p)
    # construct the \pi reference table
    u = [-1 for _ in range(m + 1)]
    k = -1
    for i in range(1, m + 1):
      while k >= 0 and p[k] != p[i - 1]:
        k = u[k]
      k += 1
      u[i] = k
    return u
  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    # prefix or suffix that can complete a word into a palindrome
    prefix, suffix = defaultdict(set), defaultdict(set)
    # must have both prefix and suffix in case one is shorter to cover all cases, e.g.,
    # 'lls' + 'sssll' is ok, but from 'lls' can figure out all suffix possible.
    for idx, word in enumerate(words):
      drow = word[::-1]
      # construct patthern p1
      p1 = word + '#' + drow
      u1 = self.kmp(p1)
      # print(f"{p1=}, {u1=}")
      # construct patthern p2
      p2 = drow + '#' + word
      u2 = self.kmp(p2)
      # print(f"{p2=}, {u2=}")
      # prefix form KMP u1 table
      n = len(word)
      k1 = -1
      while u1[k1] > -1:
        prefix[drow[:(n - u1[k1])]].add(idx)
        k1 = u1[k1]
      # suffix from KMP u2 table
      k2 = -1
      while u2[k2] > -1:
        suffix[drow[u2[k2]:]].add(idx)
        k2 = u2[k2]
    # print(f"{prefix=}")
    # print(f"{suffix=}")
    # use prefix and suffix dict to get palindrome pairs
    ans = set([])
    for idx, word in enumerate(words):
      # this word (say, 'lls') is the prefix of word at prefix[word] (say, 'sssll', 'xxsll')
      for jdx in prefix[word]:
        if not idx == jdx:
          ans.add((idx, jdx))
      # this word (say, 'sll') is the suffix of word at suffix[word] (say, 'llsss', 'llsxx')
      for jdx in suffix[word]:
        if not idx == jdx:
          ans.add((jdx, idx))
    return ans

class Solution:
  def _prefix(self, word):
    # prefix, say word: 'lls', l is palindrome, so ls -> ls is a preifx, ll is palindrome, so s -> s a is prefix
    prefix = set([])
    for i in range(len(word)):
      if word[:(i+1)] == word[:(i+1)][::-1]:
        prefix.add(word[(i+1):][::-1])
    return prefix
  def _suffix(self, word):
    # suffix, say word: 'lls', s is palindrome, so ll -> ll is a suffix
    suffix = set([])
    for i in range(len(word)):
      if word[i:] == word[i:][::-1]:
        suffix.add(word[:i][::-1])
    return suffix
  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    """simplify prefix and suffix w.o. KMP.
    """
    wdict = {word: idx for idx, word in enumerate(words)}
    # self._prefix and self._suffix only finds possible str 
    # s.t. word + str or str + word is palindrome, len(str) < len(word)
    # note the strict less of length, need to check the word pair with same length separately
    ans = set([])
    for idx, word in enumerate(words):
      drow = word[::-1]
      # word + drow
      if drow in wdict and not idx == wdict[drow]:
        # only need to add (idx, wdict[drow]), the reverse one will be added when processing drow
        ans.add((idx, wdict[drow]))
      # dro + word, any prefix like dro in words?
      for wp in self._prefix(word):
        if wp in wdict:
          ans.add((wdict[wp], idx))
      # word + row, any suffix like row in words?
      for ws in self._suffix(word):
        if ws in wdict:
          ans.add((idx, wdict[ws]))
    return ans

class TrieNode:
  def __init__(self):
    self.next = defaultdict(TrieNode)
    self.ending_word = -1
    self.palindrome_suffixes = []

class Solution:
  def palindromePairs(self, words: List[str]) -> List[List[int]]:
    # Create the Trie and add the reverses of all the words.
    trie = TrieNode()
    for i, word in enumerate(words):
      word = word[::-1] # We want to insert the reverse.
      current_level = trie
      for j, c in enumerate(word):
        # Check if remainder of word is a palindrome.
        # Is the word the same as its reverse?
        if word[j:] == word[j:][::-1]:
          current_level.palindrome_suffixes.append(i)
        # Move down the trie.
        current_level = current_level.next[c]
      current_level.ending_word = i
    # Look up each word in the Trie and find palindrome pairs.
    solutions = []
    for i, word in enumerate(words):
      current_level = trie
      for j, c in enumerate(word):
        # Check for case 3.
        if current_level.ending_word != -1:
          # Is the word the same as its reverse?
          if word[j:] == word[j:][::-1]:
            solutions.append([i, current_level.ending_word])
        if c not in current_level.next:
          break
        current_level = current_level.next[c]
      # Case 1 and 2 only come up if whole word was iterated.
      else:
        # Check for case 1.
        if current_level.ending_word != -1 and current_level.ending_word != i:
          solutions.append([i, current_level.ending_word])
        # Check for case 2.
        for j in current_level.palindrome_suffixes:
          solutions.append([i, j])
    return solutions

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["bat","tab","cat"],
    ["a","abc","aba",""],
    ["abcd","dcba","lls","s","sssll"],
  ]
  rslts = [solver.palindromePairs(words) for words in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")