class Solution:
  def __init__(self):
    self.memo = {}
    self.memo[1] = [1]
  def beautifulArray(self, N: int) -> List[int]:
    """TC: O(NlogN), SC: O(NlogN), divide and conquer.
    """
    if N not in self.memo:
      L = list(map(lambda x: 2 * x - 1, self.beautifulArray((N + 1) // 2)))
      R = list(map(lambda x: 2 * x, self.beautifulArray(N // 2)))
      self.memo[N] = L + R
    return self.memo[N]

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.beautifulArray(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
