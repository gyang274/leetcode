class Solution:
  def numberOfSteps (self, num: int) -> int:
    ans = 0
    while num > 1:
      ans += 2 if num & 1 else 1
      num >>= 1
    return ans + num

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2, 3, 5, 8, 23, 42, 85,
  ]
  rslts = [solver.numberOfSteps(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
