class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    codes = [
      ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
      "...","-","..-","...-",".--","-..-","-.--","--.."
    ]
    d = lambda x: codes[ord(x) - ord("a")]
    return len(set(["".join(map(d, word)) for word in words]))

class Solution:
  def uniqueMorseRepresentations(self, words: List[str]) -> int:
    codes = [
      ".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.",
      "...","-","..-","...-",".--","-..-","-.--","--.."
    ]
    return len({"".join(codes[ord(c) - ord('a')] for c in word) for word in words})