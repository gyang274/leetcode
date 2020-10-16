class Solution:
  def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
    croak = {x: i for i, x in enumerate('croak')}
    count = [0, 0, 0, 0, 0]
    frogs = 1
    for x in croakOfFrogs:
      i = croak[x]
      count[i] += 1
      if i > 0 and count[i] > count[i - 1]:
        return -1
      frogs = max(frogs, count[0] - count[-1])
    return -1 if count[0] > count[-1] else frogs

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "croakcroak",
    "crcoakroak",
    "croakcrook",
    "aoocrrackk",
  ]
  rslts = [solver.minNumberOfFrogs(croakOfFrogs) for croakOfFrogs in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
