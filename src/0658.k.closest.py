from typing import List

class Solution:
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    """O(logN + k), Binary search + Two pointers.
    """
    n = len(arr)
    # binary search, l, s.t. arr.insert(l, x) is sorted.
    l, r = 0, n
    while l < r:
      m = l + (r - l) // 2
      if arr[m] == x:
        l = m
        break
      elif arr[m] < x:
        l = m + 1
      else:
        r = m
    # two pointers to find k closest.
    if l == 0:
      return arr[:k]
    elif l == n:
      return arr[-k:]
    else:
      i, j = l - 1, l
      while j - i < k + 1:
        if i == -1:
          j += 1
        elif j == n:
          i -= 1
        elif abs(arr[i] - x) <= abs(arr[j] - x):
          i -= 1
        else:
          j += 1
      return arr[(i + 1):j]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ([1,2,3,4,5], 4, 3),
    ([1,2,3,4,5], 4, -1),
    ([1,1,1,10,10,10], 2, 9),
    ([1,1,1,10,10,10], 2, 0),
    ([1,1,1,10,10,10], 2, 11),
  ]
  rslts = [solver.findClosestElements(arr, k, x) for arr, k, x in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
