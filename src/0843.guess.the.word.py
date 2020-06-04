# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#   def guess(self, word: str) -> int:

import random

class Solution:
  def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
    # O(1): num of matches between words, since len(word) = 6
    match = lambda word1, word2: sum(x == y for x, y in zip(word1, word2))
    # guess
    N = 10
    for _ in range(N):
      word0 = random.choice(wordlist)
      n0 = master.guess(word0)
      wordlist = [word1 for word1 in wordlist if match(word0, word1) == n0]