class Solution:
  def maximumNumberOfOnes(self, width: int, height: int, sideLength: int, maxOnes: int) -> int:
    ms, mr, ns, nr = width // sideLength, width % sideLength, height // sideLength, height % sideLength
    # how many full s x s squre? s = sideLength
    count = ms * ns * maxOnes
    # now, key is how to put 1s on extra rows and extra cols
    # split the s x s into 4 blocks, mr * nr, (s - mr) * nr, mr * (s - nr), (s - mr) * (s - nr)
    x1, x2, x3 = mr * nr, (sideLength - mr) * nr, mr * (sideLength - nr)
    # math
    # put 1s at much as possible on the top-left corner
    if maxOnes <= x1:
      count += (ms + ns + 1) * maxOnes
    elif maxOnes >= x1 + x2 + x3:
      count += x1 + (x1 + x2) * ms + (x1 + x3) * ns
    else:
      # prioritize x2
      y2 = min(maxOnes - x1, x2)
      y3 = maxOnes - x1 - y2
      p2 = x1 + (x1 + y2) * ms + (x1 + y3) * ns
      # prioritize x3
      z3 = min(maxOnes - x1, x3)
      z2 = maxOnes - x1 - z3
      p3 = x1 + (x1 + z2) * ms + (x1 + z3) * ns
      # which one leads more 1s?
      count += max(p2, p3)
    return count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 3, 2, 2),
  ]
  rslts = [solver.maximumNumberOfOnes(width, height, sideLength, maxOnes) for width, height, sideLength, maxOnes in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
