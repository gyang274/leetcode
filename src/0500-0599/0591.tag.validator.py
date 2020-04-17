class Solution:
  def parseContent(self, code):
    # A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, 
    # unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
    n = len(code)
    i, stack = 0, []
    while i < n:
      if code[i] == "<":
        if i == n - 1:
          return False
        if not (code[i + 1] == "!" or code[i + 1] == "/"):
          # opening tag
          j = i + 1
          while j < n and not code[j] == ">":
            j += 1
          if j == i + 1 or j > i + 10:
            return False
          To = code[(i + 1):j]
          if not (To.isalpha() and To.isupper()):
            return False
          stack.append(To)
          i = j + 1
        elif code[i + 1] == "/":
          # closing tag
          j = i + 2
          while j < n and not code[j] == ">":
            j += 1
          if not stack:
            return False
          To, Tc = stack.pop(), code[(i + 2):j]
          if not To == Tc:
            return False
          i = j + 1
        else:
          # <![CDATA[CDATA_CONTENT]]>
          if code[i:(i + 9)] == "<![CDATA[":
            j = i + 9
            while j < n and not code[j:(j + 3)] == "]]>":
              j += 1
            if j == n:
              return False
            i = j + 3
          else:
            return False
      else:
        i += 1
    return not bool(stack)
  def isValid(self, code: str) -> bool:
    n = len(code)
    if n < 7 or not (code[0] == "<" and code[-1] == ">") or code[:2] == "</" or code[:2] == "<!":
      return False
    # <TAG_NAME>TAG_CONTENT</TAG_NAME>
    i = 0
    while i < n and not code[i] == ">":
      i += 1
    if i == n or i > 10:
      return False
    To = code[1:i]
    if not (To.isalpha() and To.isupper()):
      return False
    j = n - 1
    while j >= 0 and not code[j] == "<":
      j -= 1
    if j == 0 or j < i:
      return False
    # i < j
    Tc = code[(j + 1):(n - 1)]
    if not "/" + To == Tc:
      return False
    return self.parseContent(code[(i + 1):j])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "<DIV>This is the 1st line <![CDATA[<div>]]></DIV>",
    "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>",
    "<DIV>  div tag is not closed  <DIV>",
    "<DIV>  unmatched <  </DIV>",
    "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>",
    "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>",
    "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>",
    "<![CDATA[wahaha]]]>",
    "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>",
    "<A><A>456</A>  <A> 123  !!  <![CDATA[]]>  123 </A>   <A>123</A></A>",
    "<A></A><A></A>",
    "<A></A><B></B>",
    "<A>  <B> </A>   </B>",
    "<A><![CDATA[</A>]]123></A>",
    "<A A></A A>",
    "<A><!A></A>",
    "<AAAAAAAAAA></AAAAAAAAAA>",
    "<A><AAAAAAAAAA></AAAAAAAAAA></A>",
  ]
  rslts = [solver.isValid(code) for code in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")