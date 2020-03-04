class Solution:
  def isAdditiveNumber(self, num: str) -> bool:
    """backtrack/recursive
    """
    n = len(num)
    if n > 2:  
      # say, 1st num length is i, 2nd num length is j, then sum length is n - i - j
      # n - i - j >= max(i, j), j >= 1, so i <= (n - 1) // 2
      imax = 1 if num[0] == "0" else (n - 1) // 2
      for i in range(1, imax + 1):
        # say, 1st num length is i, 2nd num length is j, then sum length is n - i - j
        # n - i - j >= max(i, j), so j < min((n - i) // 2, n - 2i)
        jmax = 1 if num[i] == "0" else min(n - 2 * i, (n - i) // 2)
        for j in range(1, jmax + 1):
          # k: init index to verify additive property
          k, ki, kj = 0, i, j
          while k < n:
            skikj = str(int(num[k:(k + ki)]) + int(num[(k + ki):(k + ki + kj)]))
            # print(f"{i=}, {j=}, {k=}, {ki=}, {kj=}, {skikj=}, {num[(k + ki + kj):(k + ki + kj + len(skikj))]=}")
            if skikj == num[(k + ki + kj):(k + ki + kj + len(skikj))]:
              # ok this step
              if k + ki + kj + len(skikj) == n:
                # ok over all num
                return True
              else:
                # recursive over num
                k, ki, kj = k + ki, kj, len(skikj)
            else:
              break
    return False

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "",
    "011",
    "012",
    "1023",
    "112358",
    "1123585",
    "199100199",
    "11233444615679",
    "111122335588143",
    "120122436",
  ]
  rslts = [solver.isAdditiveNumber(num) for num in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")