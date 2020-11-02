class Solution:
  def kthFactor(self, n: int, k: int) -> int:
    count = 0
    for i in range(1, n + 1):
      if n % i == 0:
        count += 1
        if count == k:
          return i
    return -1

if __name__ == '__main__':
  solver = Solution()
  cases = [
    (1, 1), (4, 4), (7, 2), (8, 5),
  ]
  rslts = [solver.kthFactor(n, k) for n, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
