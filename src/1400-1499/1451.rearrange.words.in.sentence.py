class Solution:
  def arrangeWords(self, text: str) -> str:
    return (' '.join([x for _, _, x in sorted((len(x), i, x) for i, x in enumerate(list(map(lambda x: x.lower(), text.split()))))])).capitalize()
