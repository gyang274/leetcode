from typing import List
from collections import Counter

class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    banned = set(banned)
    paragraph = paragraph.translate(str.maketrans({
      '!': ' ', '?': ' ', "'": ' ', ',': ' ', ';': ' ', '.': ' '
    })).lower()
    return Counter(filter(lambda x: x not in banned, paragraph.split())).most_common(1)[0][0]
