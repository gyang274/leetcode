class Solution:
  def backspaceCompare(self, S: str, T: str) -> bool:
    """TC: O(N), SC: O(1).
    """
    i, j, sb, tb = len(S) - 1, len(T) - 1, 0, 0
    while i > -1 or j > -1:
      while i > -1 and (S[i] == "#" or sb > 0):
        if S[i] == '#':
          sb += 1
        else:
          sb -= 1
        i -= 1
      while j > -1 and (T[j] == '#' or tb > 0):
        if T[j] == '#':
          tb += 1
        else:
          tb -= 1
        j -= 1
      if i > -1 and j > -1:
        if S[i] == T[j]:
          i -= 1
          j -= 1
        else:
          return False
      else:
        if i > -1 and not S[i] == '#':
          return False
        if j > -1 and not S[j] == '#':
          return False
    return i == j == -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ('a#c', 'a'),
    ('a#c', 'c'),
    ('ab#c', 'ad#c'),
    ('ab##', 'c#d#'),
    ('a##c', '#a#c'),
    ("xywrrmp", "xywrrmu#p"),
  ]
  rslts = [solver.backspaceCompare(S, T) for S, T in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
