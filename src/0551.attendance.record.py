class Solution:
  def checkRecord(self, s: str) -> bool:
    return s.count("A") < 2 and s.find("LLL") < 0

class Solution:
  def checkRecord(self, s: str) -> bool:
    count = 0
    for i in range(len(s)):
      if s[i] == "A":
        count += 1
        if count > 1:
          return False
      elif s[i] == "L":
        if i + 2 < len(s) and s[i + 1] == s[i + 2] == "L":
          return False
    return True