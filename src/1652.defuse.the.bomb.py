from typing import List

class Solution:
  def decrypt(self, code: List[int], k: int) -> List[int]:
    n = len(code)
    ans = [0] * n
    if k > 0:
      ans[0] = sum(code[1:(k + 1)])
      for i in range(1, n):
        ans[i] = ans[i - 1] + code[(i + k) % n] - code[i]
    elif k < 0:
      ans[0] = sum(code[k:])
      for i in range(1, n):
        ans[i] = ans[i - 1] + code[i - 1] - code[(i - 1 + k) % n]
    return ans
