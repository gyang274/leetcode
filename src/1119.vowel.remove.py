class Solution:
  def removeVowels(self, S: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return ''.join(x for x in S if x not in vowels)