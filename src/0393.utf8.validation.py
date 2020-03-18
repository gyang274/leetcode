from typing import List

class Solution:
  def validUtf8(self, data: List[int]) -> bool:
    # n: num of following bytes..
    n, b = 0, [1 << i for i in range(8)]
    for d in data:
      if n == 0:
        if (b[7] & d):
          if (b[6] & d):
            if (b[5] & d):
              if (b[4] & d):
                if (b[3] & d):
                  return False
                else:
                  n += 3
              else:
                n += 2
            else:
              n += 1
          else:
            return False
        else:
          continue
      else:
        # is 10xxxxxx?
        if (b[7] & d) and (not (b[6] & d)):
          n -= 1
        else:
          return False
    return n == 0

if __name__ == '__main__':
  solver = Solution()
  cases = [
    [0],
    [1],
    [235],
    [197, 130, 1],
    [235, 140, 4],
  ]
  rslts = [solver.validUtf8(data) for data in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")