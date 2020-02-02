from typing import List


class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
    i, n, x = -1, len(digits), digits.copy()
    while i > - n - 1:
      if x[i] == 9:
        x[i] = 0
        if i == - n:
          x.insert(0, 1)
      else:
        x[i] += 1
        break
      i -= 1
    return x


if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    [0],
    [1],
    [2],
    [9],
    [1, 2, 1],
    [9, 9, 9],
  ]
  rslts = [solver.plusOne(digits) for digits in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")