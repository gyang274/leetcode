class Solution:
  def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    m = len(flowerbed)
    if m == 1:
      return n <= flowerbed.count(0)
    i, count = 1, 0
    flowerbed = [0] + flowerbed + [0]
    while i < m + 1:
      if flowerbed[i - 1] == flowerbed[i] == flowerbed[i + 1] == 0:
        count += 1
        i += 2
      elif flowerbed[i] == 1:
        i += 2
      else:
        i += 1
    return n <= count