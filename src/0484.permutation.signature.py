from typing import List

class Solution:
  def findPermutation(self, s: str) -> List[int]:
    """two pointers
    """
    n = len(s)
    x = [0] * (n + 1)
    i, k = 0, 1
    while i < n:
      if s[i] == "I":
        x[i] = k
        k += 1
      else:
        while i < n and s[i] == "D":
          i += 1
        x[i] = k
        k += 1
        j = i
        while j > 0 and x[j - 1] == 0:
          j -= 1
          x[j] = k
          k += 1
      i += 1
      if i == n:
        x[i] = k
    return x

class Solution:
  def findPermutation(self, s: str) -> List[int]:
    """reverse subarray
    """
    n = len(s)
    x = [i + 1 for i in range(n + 1)]
    i = 0
    while i < n:
      if s[i] == "I":
        i += 1
      else:
        j = i
        while i < n and s[i] == "D":
          i += 1
        k = i
        while j < k:
          x[j], x[k] = x[k], x[j]
          j += 1
          k -= 1
    return x

class Solution:
  def findPermutation(self, s: str) -> List[int]:
    """stack
    """
    n = len(s)
    x, stack = [], []
    i, k = 0, 1
    while i < n:
      stack.append(k)
      k += 1
      if s[i] == "I":
        while stack:
          x.append(stack.pop())
      i += 1
    stack.append(k)
    while stack:
      x.append(stack.pop())
    return x

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "DDI",
    "DDIDIDIDDI",
  ]
  rslts = [solver.findPermutation(s) for s in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")  