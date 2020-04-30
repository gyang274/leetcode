from typing import List

class Solution:
  def constructArray(self, n: int, k: int) -> List[int]:
    ans = [0] * n
    if k & 1:
      for i in range(k):
        if i & 1:
          ans[i] = n - i // 2
        else:
          ans[i] = i // 2 + 1
    else:
      for i in range(k):
        if i & 1:
          ans[i] = i // 2 + 1
        else:
          ans[i] = n - i // 2
    for i in range(k, n):
      ans[i] = i - k // 2 + 1
    return ans

class Solution:
  def constructArray(self, n: int, k: int) -> List[int]:
    ans = [0] * n
    for i in range(k):
      if (k & 1) ^ (i & 1):
        ans[i] = i // 2 + 1
      else:
        ans[i] = n - i // 2
    for i in range(k, n):
      ans[i] = i - k // 2 + 1
    return ans

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (3, 1),
    (3, 2),
    (22, 4),
    (22, 5),
  ]
  rslts = [solver.constructArray(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
