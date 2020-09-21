class Solution:
  def __init__(self):
    self.d = {
      'a': 'A',
      'b': 'B',
      'c': 'C',
      'd': 'D',
      'e': 'E',
      'f': 'F',
      '0': 'O',
      '1': 'I',
    }
  def toHexspeak(self, num: str) -> str:
    s, h = hex(int(num))[2:], ''
    for x in s:
      if x in self.d:
        h += self.d[x]
      else:
        return 'ERROR'
    return h

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, 2, 3, 23, 257,
  ]
  rslts = [solver.toHexspeak(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
