from typing import List

class Solution:
  def removeComments(self, source: List[str]) -> List[str]:
    ans, inblock = [], False
    for line in source:
      i = 0
      if not inblock:
        left = ""
      while i < len(line):
        if not inblock and line[i:(i + 2)] == "/*":
          inblock = True
          i += 1
        elif inblock and line[i:(i + 2)] == "*/":
          inblock = False
          i += 1
        elif not inblock and line[i:(i + 2)] == "//":
          break
        elif not inblock:
          left += line[i]
        i += 1
      if not inblock and left:
        ans.append(left)
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    # ["a/*/b//*c","blank","d//*e/*/f"],
    # ["a//*b//*c","blank","d/*/e*//f"],
    ["a/*/b//*c","blank","d/*/e*//f"],
    # ["a/*comment", "line", "more_comment*/b"],
    # ["struct Node{", "    /*/ declare members;/**/", "    int size;", "    /**/int val;", "};"],
    # ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"],
  ]
  rslts = [solver.removeComments(source) for source in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
