class Solution:
  def xorOperation(self, n: int, start: int) -> int:
    # TC: O(N), SC: O(1), note it is possible but difficult to complete this in O(1)..
    ans = 0
    for i in range(n):
      ans ^= (start + 2 * i)
    return ans
