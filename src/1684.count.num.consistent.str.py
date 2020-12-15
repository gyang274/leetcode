class Solution:
  def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
    return sum(1 if len(set(word) - set(allowed)) == 0 else 0 for word in words)