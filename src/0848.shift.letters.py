from typing import List

class Solution:
  def shiftingLetters(self, S: str, shifts: List[int]) -> str:
    n = len(shifts)
    for i in range(n - 2, -1, -1):
      shifts[i] += shifts[i + 1]
    s = list(S)
    for i in range(n):    
      s[i] = chr(ord('a') + ((ord(s[i]) - ord('a') + shifts[i]) % 26))
    return ''.join(s)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("abc", [3,5,8]),
    ("ruu", [26,9,17]),
  ]
  rslts = [solver.shiftingLetters(S, shifts) for S, shifts in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
