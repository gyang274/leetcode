class Solution:
  def recursive(self, i, nums):
    if i == self.N + 1:
      self.count += 1
    else:
      for v in nums:
        if v % i == 0 or i % v == 0:
          self.recursive(i + 1, nums - {v})
  def countArrangement(self, N: int) -> int:
    self.count, self.N = 0, N
    nums = set([i for i in range(1, N + 1)])
    self.recursive(1, nums)
    return self.count

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 10, 15,
  ]
  rslts = [solver.countArrangement(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")