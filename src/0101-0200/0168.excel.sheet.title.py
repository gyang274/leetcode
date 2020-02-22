class Solution:
  def convertToTitle(self, n: int) -> str:
    x = ""
    while n > 0:
      # move index from 1-26 to 0-25
      n -= 1
      # get leftmost alphabetical A-Z from number 0-25
      x = chr(n % 26 + 65) + x
      # move to next level to the rightmost alphabeticals
      n //= 26
    return x

class Solution:
  def convertToTitle(self, n: int) -> str:
    x = ""
    while n > 0:
      n -= 1
      x += chr(n % 26 + 65)
      n //= 26
    return x[::-1]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1,
    28,
    52,
    701,
    772,
    2714,
  ]
  rslts = [solver.convertToTitle(n) for n in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")