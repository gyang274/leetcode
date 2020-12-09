class Solution:
  def interpret(self, command: str) -> str:
    s, i, n = '', 0, len(command)
    while i < n:
      if command[i] == 'G':
        s += 'G'
        i += 1
      else:
        # command[i] == '('
        if command[i + 1] == ')':
          s += 'o'
          i += 2
        else:
          s += 'al'
          i += 4
    return s
