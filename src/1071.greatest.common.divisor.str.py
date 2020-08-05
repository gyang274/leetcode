class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    # same logic as gcd of numbers, toss and divide
    if len(str1) == len(str2):
      return str1 if str1 == str2 else ""
    if len(str1) < len(str2):
      str1, str2 = str2, str1
    return self.gcdOfStrings(str2, str1[(len(str2)):]) if str1[:(len(str2))] == str2 else ""

if __name__ == '__main__':
  solver = Solution()
  cases = [
    ("LEET", "CODE"),
    ("ABCABC", "ABC"),
    ("ABABAB", "ABAB"),
  ]
  rslts = [solver.gcdOfStrings(str1, str2) for str1, str2 in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
