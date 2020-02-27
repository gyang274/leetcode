from typing import List

class Codec:
  """Encode and decode with dynamic delimiter since all kinds of characters combination are possible.
    All letters before 1st null chr(0) is delimiter identified by finding shortest k letters that has no appearance in strs.
  """
  def _delimiter(self, strs):
    d, n = [""], max([len(s) for s in strs])
    for k in range(1, n + 1):
      # generate 256^k delimiter candidates
      dnext = []
      for dx in d:
        # python2 range(1, 128)
        # python3 range(1, 256)
        # python2's ascii set is 0-128?
        for i in range(1, 256):
          dnext.append(dx + chr(i))
      d, dnext = dnext, set(dnext)
      # any of candidates no shown in strs..
      for s in strs:
        for i in range(len(s) - k + 1):
          # discard() instead of remove() to eliminate keyerror
          dnext.discard(s[i:(i + k)])
      if dnext:
        return dnext.pop()
    # strs have all combinations of 1, .., n characters..
    return chr(1) * (n + 1)
    
  def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    if not strs:
      return ""
    d = self._delimiter(strs)
    return d + chr(0) + d.join(strs)

  def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    if s == "":
      return []
    i, d = 0, ''
    while not s[i] == chr(0):
      d += s[i]
      i += 1
    return s[(i + 1):].split(d)
    
class Codec:
  """Encode and decode with dynamic delimiter since all kinds of characters combination are possible.
    All letters before 1st null chr(0) is delimiter identified by finding shortest k letters that has no appearance.
    Improvement: simply using k chr(1) instead of checking over all characters combination, since chr(1) rare anyway.
  """
  def _delimiter(self, strs):
    d, n = "", max([len(s) for s in strs])
    for k in range(1, n + 1):
      # simply using k chr(1) instead of checking over all characters combination, since chr(1) rare anyway
      d += chr(1)
      # any of candidates no shown in strs..
      for s in strs:
        if d in s:
          break
      else:
        return d
    # strs have all combinations of 1, .., n characters..
    return chr(1) * (n + 1)
    
  def encode(self, strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    if not strs:
      return ""
    d = self._delimiter(strs)
    return d + chr(0) + d.join(strs)

  def decode(self, s: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    if s == "":
      return []
    i, d = 0, ''
    while not s[i] == chr(0):
      d += s[i]
      i += 1
    return s[(i + 1):].split(d)
