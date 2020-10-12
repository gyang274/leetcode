class Solution:
  def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
    xc, yc, r = x_center, y_center, radius
    if x1 <= xc <= x2:
      return y1 - r <= yc <= y2 + r
    elif y1 <= yc <= y2:
      return x1 - r <= xc <= x2 + r
    else:
      d11 = (xc - x1) ** 2 + (yc - y1) ** 2
      d12 = (xc - x1) ** 2 + (yc - y2) ** 2
      d21 = (xc - x2) ** 2 + (yc - y1) ** 2
      d22 = (xc - x2) ** 2 + (yc - y2) ** 2
      return min(d11, d12, d21, d22) <= r ** 2

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 0, 0, 1, 0, 0, 1),
    (1, 0, 0, 1, -1, 3, 1),
    (1, 1, 1, -3, -3, 3, 3),
    (1, 1, 1, 1, -3, 2, -1),
  ]
  rslts = [solver.checkOverlap(radius, x_center, y_center, x1, y1, x2, y2) for radius, x_center, y_center, x1, y1, x2, y2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
