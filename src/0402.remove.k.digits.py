class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    i = 1
    while k > 0 and i < len(num):
      if i > 0 and num[i] < num[i - 1]:
        j = i
        if j == 1:
          while j < len(num) and num[j] == "0":
            j += 1
        num = num[:(i - 1)] + num[j:]
        k -= 1
        i -= 1
      else:
        i += 1
    if k > 0:
      num = num[0:(len(num) - k)]
    return num if not num == "" else "0"

class Solution:
  def removeKdigits(self, num: str, k: int) -> str:
    # leave the "0" be at the leading position, remove at the end all at once.
    i = 1
    while k > 0 and i < len(num):
      if i > 0 and num[i] < num[i - 1]:
        num = num[:(i - 1)] + num[i:]
        k -= 1
        i -= 1
      else:
        i += 1
    i = 0
    while i < len(num) and num[i] == "0":
      i += 1
    num = num[i:(len(num) - k)]
    return num if not num == "" else "0"

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("1020", 1),
    ("1020", 2),
    ("102030452", 1),
    ("102030452", 2),
    ("102030452", 3),
    ("102030452", 4),
    ("102030452", 5),
  ]
  rslts = [solver.removeKdigits(num, k) for num, k in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
