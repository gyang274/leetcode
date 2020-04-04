class Solution:
  def findComplement(self, num: int) -> int:
    mask, runs = 0, num
    while runs > 0:
      runs >>= 1
      mask = (mask << 1) | 1
    return mask ^ num

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 42, 85
  ]
  rslts = [solver.findComplement(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")    