from typing import List

class Solution:
  def parseEmail(self, email):
    s, p = "", False
    for i, x in enumerate(email):
      if x == ".":
        continue
      elif x == "+":
        p = True
      elif x == "@":
        s += email[i:]
        break
      else:
        if not p:
          s += x
    return s
  def numUniqueEmails(self, emails: List[str]) -> int:
    return len(set(map(self.parseEmail, emails)))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"],
  ]
  rslts = [solver.numUniqueEmails(emails) for emails in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
