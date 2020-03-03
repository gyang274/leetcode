class Solution:
  def getHint(self, secret: str, guess: str) -> str:
    # m: count of exact match between and guess
    m = 0
    # sc, gc: count of 0, .., 0 in secret and guess, when not exact match, respectively
    sc, gc = [0] * 10, [0] * 10
    # process secret and guess, one pass
    for x, y in zip(list(secret), list(guess)):
      if x == y:
        m += 1
      else:
        sc[int(x)] += 1
        gc[int(y)] += 1
    return str(m) + "A" + str(sum([min(x, y) for x, y in zip(sc, gc)])) + "B"
  
if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("1807", "7810"),
    ("1123", "0111"),
  ]
  rslts = [solver.getHint(secret, guess) for secret, guess in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")