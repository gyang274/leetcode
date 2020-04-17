class Solution:
  def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    d1, d2 = {}, {}
    for i, x in enumerate(list1):
      d1[x] = i
    for i, x in enumerate(list2):
      d2[x] = i
    imin, xmin = float('inf'), []
    for k in (set(d1) & set(d2)):
      i = d1[k] + d2[k]
      if i < imin:
        imin = i
        xmin = [k]
      elif i == imin:
        xmin.append(k)
    return xmin
        