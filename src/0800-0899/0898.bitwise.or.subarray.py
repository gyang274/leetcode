class Solution:
  def subarrayBitwiseORs(self, A: List[int]) -> int:
    n, s = len(A), set()
    for i in range(n):
      x = A[i]
      for j in range(i, n):
        x |= A[j]
        s.add(x)
    return len(s)

class Solution:
  def subarrayBitwiseORs(self, A: List[int]) -> int:
    # maintain a frontier set of A[i] | ... | A[k] for i = 0, .., k - 1
    ans, cur = set(), {0}
    for x in A:
      cur = {y | x for y in cur} | {x}
      ans |= cur
    return len(ans)
