class Solution:
  def isRobotBounded(self, instructions: str) -> bool:
    # d: facing direction, keep turning left, s: (x, y, d)
    s, d = [0, 0, 0], [(0, 1), (-1, 0), (0, -1), (1, 0)]
    for x in instructions:
      if x == "L":
        s[2] = (s[2] + 1) % 4
      elif x == "R":
        s[2] = (s[2] - 1) % 4
      else:
        # if x == "G":
        s[0] += d[s[2]][0]
        s[1] += d[s[2]][1]
    return (s[0], s[1]) == (0, 0) or s[2] != 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "GG",
    "GL",
    "LL",
    "LLGRL",
    "LLGRLL",
    "LLGRLLL",
    "LLGRLLLL",
  ]
  rslts = [solver.isRobotBounded(instructions) for instructions in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
