class Solution:
  def maskPII(self, S: str) -> str:
    if S[0].isalpha():
      name, domain = S.lower().split('@')
      return name[0] + '*' * 5 + name[-1] + '@' + domain
    else:
      s = list(filter(str.isdigit, S))
      return ('+' + '*' * (len(s) - 10) + '-'  if len(s) > 10 else '') + '***-***-' + ''.join(s[-4:])

if __name__ == '__main__':
  solver = Solution()
  cases = [
    "LeetCode@LeetCode.com",
    "AB@qq.com",
    "1(234)567-890",
    "86-(10)12345678",
  ]
  rslts = [solver.maskPII(S) for S in cases]
  for cs, rs in zip(cases, rslts):
    print(f"case: {cs} | solution: {rs}")
