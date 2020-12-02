from typing import List

class Solution:
  def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    d = {}
    for j, piece in enumerate(pieces):
      for x in piece:
        d[x] = j
    i = 0
    while i < len(arr):
      if arr[i] not in d:
        return False
      j = d[arr[i]]
      for k in range(len(pieces[j])):
        if i + k >= len(arr):
          return False
        if arr[i + k] != pieces[j][k]:
          return False
      i += len(pieces[j])
    return True

class Solution:
  def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
    d = {x[0]: x for x in pieces}
    ans = []
    for y in arr:
      ans += d.get(y, [])
    return ans == arr
