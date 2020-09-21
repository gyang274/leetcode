# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Sea(object):
#   def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
# 
# class Point(object):
# 	def __init__(self, x: int, y: int):
# 		self.x = x
# 		self.y = y

class Solution:
  def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
    # 2D binary search, Q1237.
    count = 0
    queue = [(topRight, bottomLeft)]
    while queue:
      pTR, pBL = queue.pop()
      if sea.hasShips(pTR, pBL):
        if (pTR.x, pTR.y) == (pBL.x, pBL.y):
          count += 1
        elif pTR.x == pBL.x:
          # split on y-axis
          m = pBL.y + (pTR.y - pBL.y) // 2
          queue.append((pTR, Point(pBL.x, m + 1)))
          queue.append((Point(pTR.x, m + 0), pBL))
        else:
          # split on x-axis
          m = pBL.x + (pTR.x - pBL.x) // 2
          queue.append((pTR, Point(m + 1, pBL.y)))
          queue.append((Point(m + 0, pTR.y), pBL))
    return count
