import itertools

class Solution:
  def magicalString(self, n: int) -> int:
    s = "1221121221"
    if n > 10:
      i, j = 7, 9
      while j < n:
        s += str(3 - int(s[j])) * int(s[i])
        j += int(s[i])
        i += 1
    return s[:n].count("1")

class Solution:
  def magicalString(self, n: int) -> int:
    """TC: O(N), SC: O(logN), https://arxiv.org/pdf/1110.4228.pdf
      A Space-Efficient Algorithm for Calculating the Digit Distribution in the Kolakoski Sequence
    """
    def generator():
      for x in 1, 2, 2:
        yield x
      for i, x in enumerate(generator()):
        if i > 1:
          for _ in range(x):
            yield i % 2 + 1
    return sum(x & 1 for x in itertools.islice(generator(), n))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1, 2, 3, 5, 8, 42, 85,
  ]
  rslts = [solver.magicalString(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
