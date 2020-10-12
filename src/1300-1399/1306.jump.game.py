from typing import List

class Solution:
  def canReach(self, arr: List[int], start: int) -> bool:
    if arr[start] == 0:
      return True
    v, b, e, n = set(), set([start]), set(), len(arr)
    while b or e:
      while b:
        i = b.pop()
        v.add(i)
        for j in [i + arr[i], i - arr[i]]:
          if j >= 0 and j < n and (not (j in v or j in b)):
            if arr[j] == 0:
              return True
            e.add(j)
      e, b = b, e
    return False

class Solution:
  def canReach(self, arr: List[int], start: int) -> bool:
    v, b, e, n = set(), set([start]), set(), len(arr)
    while b or e:
      while b:
        i = b.pop()
        if arr[i] == 0:
          return True
        v.add(i)
        for j in [i + arr[i], i - arr[i]]:
          if j >= 0 and j < n and (not (j in v or j in b)):
            e.add(j)
      e, b = b, e
    return False

if __name__ == '__main__':
  solver = Solution()
  # test cases
  cases = [
    ([0], 0),
    ([4,2,3,0,3,1,2], 5),
    ([4,2,3,0,3,1,2], 0),
    ([3,0,2,1,2], 2),
  ]
  rslts = [solver.canReach(arr, start) for arr, start in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
