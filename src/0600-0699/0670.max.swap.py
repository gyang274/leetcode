class Solution:
  def maximumSwap(self, num: int) -> int:
    num = list(str(num))
    # rmax: max from right, ridx: max from right 1st seen index
    n = len(num)
    rmax, ridx = [""] * (n + 1), [None] * (n + 1)
    for i in range(n - 1, -1, -1):
      rmax[i], ridx[i] = (num[i], i) if num[i] > rmax[i + 1] else (rmax[i + 1], ridx[i + 1])
    for i in range(n):
      if num[i] < rmax[i]:
        num[i], num[ridx[i]] = num[ridx[i]], num[i]
        break
    return int("".join(num))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    2714, 9985,
  ]
  rslts = [solver.maximumSwap(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
