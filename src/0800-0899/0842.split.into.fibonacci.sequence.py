from typing import List

class Solution:
  def splitIntoFibonacci(self, S: str) -> List[int]:
    # Key: F[0], F[1] determines the entire sequence.
    M, N = 1 << 31, len(S)
    for i in range(1, min(10, N)):
      if i == 1 or not S[0] == "0":
        for j in range(i + 1, min(i + 10, N)):
          if j == i + 1 or not S[i] == "0":
            f, k = [int(S[:i]), int(S[i:j])], j
            if f[0] < M and f[1] < M:
              while k < N:
                f.append(f[-2] + f[-1])
                if f[-1] < M:
                  n = len(str(f[-1]))
                  if f[-1] == int(S[k:(k+n)]):
                    k += n
                  else:
                    break
                else:
                  break
              if k == N:
                return f
    return []

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "0123",
    "01123",
    "1101111",
    "11235813",
    "112358130",
    "123456579",
    "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511",
  ]
  rslts = [solver.splitIntoFibonacci(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
