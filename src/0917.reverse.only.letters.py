class Solution:
  def reverseOnlyLetters(self, S: str) -> str:
    i, j, S = 0, len(S) - 1, list(S)
    while i < j:
      while i < j and not S[i].isalpha():
        i += 1
      while i < j and not S[j].isalpha():
        j -= 1
      if i < j:
        S[i], S[j] = S[j], S[i]
        i += 1
        j -= 1
    return ''.join(S)

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "ab-cd",
    "a-bC-dEf-ghIj",
    "Test1ng-Leet=code-Q!",
  ]
  rslts = [solver.reverseOnlyLetters(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
