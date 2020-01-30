from typing import List


class Solution:
  def combine(self, n: int, k: int) -> List[List[int]]:
    """Lexicographic (binary sorted) combinations. YG.
    """
    x = [i for i in range(1, k + 1)]
    y = []
    while True:
      y.append(x.copy())
      x[-1] += 1
      if x[-1] == n + 1:
        x[-1] -= 1
        i = -1
        while x[i] == n + 1 + i:
          i -= 1
          if i < -k:
            return y
        z = x[i]
        for j in range(i, 0):
          x[j] = z - i + j + 1
    return None


# class Solution:
#   def combine(self, n: int, k: int) -> List[List[int]]:
#     """Lexicographic (binary sorted) combinations.
#     """
#     # init first combination
#     x = list(range(1, k + 1)) + [n + 1]
#     y, j = [], 0
#     while j < k:
#       # add current combination
#       y.append(x[:k])
#       # increase first x[j] by one
#       # if x[j] + 1 != x[j + 1]
#       j = 0
#       while j < k and x[j + 1] == x[j] + 1:
#         x[j] = j + 1
#         j += 1
#       x[j] += 1
#     return y


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    (1, 1),
    (4, 2),
    (5, 3),
  ]
  rslts = [solver.combine(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")