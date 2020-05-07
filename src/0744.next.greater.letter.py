class Solution:
  def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    for x in letters:
      if x > target:
        return x
    return letters[0]

class Solution(object):
  def nextGreatestLetter(self, letters, target):
    seen = set(letters)
    for i in range(1, 26):
      cand = chr((ord(target) - ord('a') + i) % 26 + ord('a'))
      if cand in seen:
        return cand

import bisect

class Solution(object):
  def nextGreatestLetter(self, letters, target):
    return letters[bisect.bisect(letters, target) % len(letters)]
