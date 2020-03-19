class Solution:
  def toHex(self, num: int) -> str:
    if num == 0:
      return "0"
    # define hex base
    HEX = {i: str(i) for i in range(10)}
    HEX.update({
      10: "a",
      11: "b",
      12: "c",
      13: "d",
      14: "e",
      15: "f",
    })
    # limit num to 32bit
    num &= 0xFFFFFFFF
    # convert num to hex
    s, mask = "", 15
    while num > 0:
      s = HEX[num & mask] + s
      num >>= 4
    return s

if __name__ == '__main__':
  solver = Solution()
  cases = [
    0, 1, -1, 2147483647, -2147483648, 2, 42, 2147483642,
  ]
  rslts = [solver.toHex(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
