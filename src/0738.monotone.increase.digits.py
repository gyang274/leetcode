from collections import deque

class Solution:
  def monotoneIncreasingDigits(self, N: int) -> int:
    S = list(str(N))
    i = 1
    while i < len(S) and S[i - 1] <= S[i]:
      i += 1
    while 0 < i < len(S) and S[i - 1] > S[i]:
      S[i - 1] = str(int(S[i - 1]) - 1)
      i -= 1
    S[(i + 1):] = '9' * (len(S) - (i + 1))
    return int("".join(S))

if __name__ == '__main__':
  solver = Solution()
  cases = [
    1,
    10,
    142,
    232,
    1214,
    12142,
    121423,
  ]
  rslts = [solver.monotoneIncreasingDigits(N) for N in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
