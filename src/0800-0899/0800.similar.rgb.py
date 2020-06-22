class Solution:
  def similarRGB(self, color: str) -> str:
    def f(x):
      q, r = divmod(int(x, 16), 17)
      if r > 8:
        q += 1
      return f"{17 * q:02x}"
    return "#" + f(color[1:3]) + f(color[3:5]) + f(color[5:7])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "#09f166",
  ]
  rslts = [solver.similarRGB(color) for color in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
