class Solution:
  def toGoatLatin(self, S: str) -> str:
    vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return ' '.join([(x if x[0] in vowel else x[1:] + x[:1]) + 'ma' + 'a' * (i + 1) for i, x in enumerate(S.split())])