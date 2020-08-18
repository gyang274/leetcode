class Solution:
  def alphabetBoardPath(self, target: str) -> str:
    # board
    board = [
      "abcde",
      "fghij",
      "klmno",
      "pqrst",
      "uvwxy",
      "z"    ,
    ]
    # hash the board
    d = {}
    for i in range(5):
      for j in range(5):
        d[board[i][j]] = (i, j)
    d['z'] = (5, 0)
    # define path
    def path(s1, s2):
      x1, y1 = d[s1]
      x2, y2 = d[s2]
      xs = ('U' if x1 > x2 else 'D') * abs(x1 - x2)
      ys = ('L' if y1 > y2 else 'R') * abs(y1 - y2)
      return ys + xs + '!' if s2 == 'z' else xs + ys + '!'
    # create path
    ans, target = '', 'a' + target
    for i in range(len(target) - 1):
      ans += path(target[i], target[i + 1])
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    'leetcode', 'zinedinezidane'
  ]
  rslts = [solver.alphabetBoardPath(target) for target in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
